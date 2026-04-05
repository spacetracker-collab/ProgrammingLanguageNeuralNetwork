# ProgrammingLanguageNeuralNetwork

Epoch 0 | Loss 0.1883
Epoch 20 | Loss 0.0809
Epoch 40 | Loss 0.0367
Epoch 60 | Loss 0.0188
Epoch 80 | Loss 0.0119
Epoch 100 | Loss 0.0094
Epoch 120 | Loss 0.0084
Epoch 140 | Loss 0.0081
Epoch 160 | Loss 0.0079
Epoch 180 | Loss 0.0078

--- Language Scores (With Science & Technology) ---
C               -> 0.470
Go              -> 0.467
TypeScript      -> 0.462
Objective-C     -> 0.461
PHP             -> 0.453
Julia           -> 0.452
Python          -> 0.450
C#              -> 0.448
Dart            -> 0.443
JavaScript      -> 0.441
R               -> 0.440
Haskell         -> 0.436
Kotlin          -> 0.435
Ruby            -> 0.433
C++             -> 0.433
Swift           -> 0.432
Scala           -> 0.421
MATLAB          -> 0.419
Rust            -> 0.418
Java            -> 0.418

--- Top 5 Languages ---
C               -> 0.470
Go              -> 0.467
TypeScript      -> 0.462
Objective-C     -> 0.461
PHP             -> 0.453

--- Bottom 5 Languages ---
Swift           -> 0.432
Scala           -> 0.421
MATLAB          -> 0.419
Rust            -> 0.418
Java            -> 0.418


# Programming Language Neural Model (Extended)

## Overview
This project builds a **multi-parameter neural network model** to rank the top 20 programming languages using a synthetic TIOBE-like scoring system.

## Features (Input Parameters)
Each programming language is represented by:

- Popularity
- Performance
- Safety
- Concurrency
- Simplicity
- Science & Technology Impact (NEW)

## Key Idea
The addition of **science & technology** captures:
- Use in research (AI, physics, math)
- Academic adoption
- Scientific computing ecosystems

## Model Architecture
- Input layer: 6 features
- Hidden layer: 10 neurons (ReLU)
- Output: 1 score (ranking)

## Training
- Loss: Mean Squared Error
- Optimizer: Gradient Descent
- Epochs: 200

## Sample Output

