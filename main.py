# main.py
# Multi-parameter neural network simulation for top programming languages

import numpy as np

# -----------------------------
# Synthetic "TIOBE-like" dataset
# Features: [popularity, performance, safety, concurrency, simplicity]
# -----------------------------
languages = [
    "Python","C","C++","Java","C#","Go","Rust","JavaScript","TypeScript","Kotlin",
    "Swift","PHP","Ruby","MATLAB","R","Dart","Scala","Julia","Haskell","Objective-C"
]

np.random.seed(42)
X = np.random.rand(len(languages), 5)

# Simulated target score ("TIOBE-like index")
true_weights = np.array([0.4, 0.2, 0.15, 0.15, 0.1])
y = X @ true_weights + 0.05 * np.random.randn(len(languages))

# -----------------------------
# Simple Neural Network
# -----------------------------
class NeuralNet:
    def __init__(self, input_size, hidden_size, output_size):
        self.W1 = np.random.randn(input_size, hidden_size) * 0.1
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.1
        self.b2 = np.zeros((1, output_size))

    def relu(self, x):
        return np.maximum(0, x)

    def relu_deriv(self, x):
        return (x > 0).astype(float)

    def forward(self, X):
        self.z1 = X @ self.W1 + self.b1
        self.a1 = self.relu(self.z1)
        self.z2 = self.a1 @ self.W2 + self.b2
        return self.z2

    def train(self, X, y, lr=0.01, epochs=200):
        for epoch in range(epochs):
            y_pred = self.forward(X)
            loss = np.mean((y_pred - y.reshape(-1,1))**2)

            # Backprop
            dloss = 2*(y_pred - y.reshape(-1,1))/len(X)
            dW2 = self.a1.T @ dloss
            db2 = np.sum(dloss, axis=0, keepdims=True)

            da1 = dloss @ self.W2.T
            dz1 = da1 * self.relu_deriv(self.z1)
            dW1 = X.T @ dz1
            db1 = np.sum(dz1, axis=0, keepdims=True)

            # Update
            self.W1 -= lr * dW1
            self.b1 -= lr * db1
            self.W2 -= lr * dW2
            self.b2 -= lr * db2

            if epoch % 20 == 0:
                print(f"Epoch {epoch} | Loss {loss:.4f}")

# -----------------------------
# Train model
# -----------------------------
model = NeuralNet(input_size=5, hidden_size=8, output_size=1)
model.train(X, y)

# -----------------------------
# Inference
# -----------------------------
predictions = model.forward(X).flatten()

print("\n--- Language Scores (Predicted) ---")
for lang, score in sorted(zip(languages, predictions), key=lambda x: -x[1]):
    print(f"{lang:15s} -> {score:.3f}")
