# sentiment_analyzer.py

from textblob import TextBlob

class SentimentAnalyzer:
    def analyze(self, text):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        return polarity
