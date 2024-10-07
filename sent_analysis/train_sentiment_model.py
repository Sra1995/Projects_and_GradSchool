import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load the IMDB dataset
df_imdb = pd.read_csv('/Users/sajjadalsaffar/Documents/Coding/Python/sent_analysis/IMDB Dataset.csv')

# Load the new dataset (replace 'train.csv' with the path to your dataset)
df_new = pd.read_csv('/Users/sajjadalsaffar/Documents/Coding/Python/sent_analysis/train.csv', encoding='latin1')

# Data Preprocessing for the IMDB dataset
df_imdb = df_imdb[['review', 'sentiment']]
df_imdb.columns = ['text', 'sentiment']

# Data Preprocessing for the new dataset
df_new = df_new[['text', 'sentiment']]
df_new.dropna(subset=['text', 'sentiment'], inplace=True)

# Combine both datasets
df_combined = pd.concat([df_imdb, df_new], ignore_index=True)

X = df_combined['text']
y = df_combined['sentiment']

# Model Selection
vectorizer = TfidfVectorizer()
classifier = MultinomialNB()

# Model Training
X_vectorized = vectorizer.fit_transform(X)
classifier.fit(X_vectorized, y)

# Save the model and vectorizer to files
joblib.dump(vectorizer, '/Users/sajjadalsaffar/Documents/Coding/Python/sent_analysis/vectorizer.pkl')
joblib.dump(classifier, '/Users/sajjadalsaffar/Documents/Coding/Python/sent_analysis/sentiment_model.pkl')

print("Model training and saving complete.")
