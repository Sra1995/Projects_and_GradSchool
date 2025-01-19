# Sentiment Analysis Project

## Project Overview

This project aims to build a sentiment analysis model that can classify text reviews as either positive or negative. The project involves training a machine learning model using the IMDB dataset and an additional dataset, and then using the trained model to analyze the sentiment of new text inputs.

## Project Structure

The project directory contains the following files:

- `analyze_sentiment.py`: Script to load the trained model and vectorizer and perform sentiment analysis on new text inputs.
- `IMDB Dataset.csv`: The IMDB dataset containing movie reviews and their corresponding sentiments.
- `readme.md`: Project documentation.
- `sent_an.py`: Script to create a machine learning model for sentiment analysis using the IMDB dataset.
- `sentiment_model.pkl`: The trained sentiment analysis model.
- `train_sentiment_model.py`: Script to train the sentiment analysis model using both the IMDB dataset and an additional dataset.
- `train.csv`: An additional dataset containing text reviews and their corresponding sentiments.
- `vectorizer.pkl`: The trained vectorizer used to transform text data into numerical features.

## Goal

The goal of this project is to create a machine learning model that can accurately classify text reviews as positive or negative. The model is trained using the IMDB dataset and an additional dataset, and it is evaluated based on its accuracy on a test set.

## Algorithm

The project uses the Naive Bayes algorithm for sentiment analysis. Specifically, the `MultinomialNB` classifier from the `sklearn.naive_bayes` module is used. The text data is transformed into numerical features using the `TfidfVectorizer` and `CountVectorizer` from the `sklearn.feature_extraction.text` module.

## Steps

### 1. Data Preprocessing

The data preprocessing steps are performed in the `train_sentiment_model.py` and `sent_an.py` scripts.

- Load the IMDB dataset and the additional dataset.
- Convert the sentiment labels to binary values (1 for positive, 0 for negative).
- Combine the datasets into a single DataFrame.
- Split the combined dataset into training and testing sets.

### 2. Feature Extraction

The text data is transformed into numerical features using the `TfidfVectorizer` and `CountVectorizer`.

- In `train_sentiment_model.py`, the `TfidfVectorizer` is used to transform the text data.
- In `sent_an.py`, the `CountVectorizer` is used to create a bag-of-words representation of the text data.

### 3. Model Training

The `MultinomialNB` classifier is trained on the transformed text data.

- In `train_sentiment_model.py`, the classifier is trained on the combined dataset.
- In `sent_an.py`, the classifier is trained on the IMDB dataset.

### 4. Model Evaluation

The trained classifier is evaluated on the testing data using the `accuracy_score` from the `sklearn.metrics` module.

- In `sent_an.py`, the accuracy of the classifier is printed.

### 5. Model Saving

The trained model and vectorizer are saved to files using the `joblib` module.

- In `train_sentiment_model.py`, the model and vectorizer are saved to `sentiment_model.pkl` and `vectorizer.pkl`, respectively.

### 6. Sentiment Analysis

The `analyze_sentiment.py` script loads the trained model and vectorizer and performs sentiment analysis on new text inputs.

- The `analyze_sentiment` function transforms the input text using the vectorizer and predicts the sentiment using the classifier.
- The script prints the sentiment of a sample text input.

## Usage

### Training the Model

To train the sentiment analysis model, run the `train_sentiment_model.py` script:

```sh
python train_sentiment_model.py
 ```

### Conclusion
This project demonstrates how to build a sentiment analysis model using the Naive Bayes algorithm and the IMDB dataset. The trained model can be used to classify text reviews as positive or negative, providing valuable insights into the sentiment of the text.
