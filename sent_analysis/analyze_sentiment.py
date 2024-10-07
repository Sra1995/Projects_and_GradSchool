# analyze_sentiment.py

import joblib

# Load the saved model and vectorizer
vectorizer = joblib.load('/Users/sajjadalsaffar/Documents/Coding/Python/sent_analysis/vectorizer.pkl')
classifier = joblib.load('/Users/sajjadalsaffar/Documents/Coding/Python/sent_analysis/sentiment_model.pkl')

# Function for sentiment analysis
def analyze_sentiment(text):
    text_vectorized = vectorizer.transform([text])
    sentiment = classifier.predict(text_vectorized)
    return sentiment[0]

if __name__ == "__main__":
    # Example usage
    sample_text = "MAYDAY?"
    result = analyze_sentiment(sample_text)
    print(f"Sentiment: {result}")


# Neatural sentence for test = The weather today is neither good nor bad.