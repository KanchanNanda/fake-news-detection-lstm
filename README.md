# Fake News Detection Using LSTM

## Overview
A deep learning project that classifies news text as Fake News or Real News
using an LSTM neural network built with TensorFlow and Keras.

## Dataset
Fake.csv and True.csv.
Labels: Fake News = 0, Real News = 1.

## Model
- TextVectorization
- Embedding
- LSTM
- Dropout
- Dense layers
- Sigmoid output

## Dataset Split
- Training: 35,413 articles
- Validation: 4,427 articles
- Testing: 4,427 articles

## Test Results
- Accuracy: 95.50%
- Fake News F1-score: 95.64%
- Real News F1-score: 95.37%

## Limitations
Performance is measured on this dataset. It may not generalize to
all real-world news. Predictions should not be treated as fact verification.

## Run
Load the saved .keras model in a compatible TensorFlow environment.
