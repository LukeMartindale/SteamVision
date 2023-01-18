from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def reviews_sentiment(review_text):
    value = TextBlob(str(review_text))

    sentiment = {
        "positive": True,
        "polarity": value.sentiment.polarity,
        "subjectivity": value.sentiment.subjectivity
    }

    if value.sentiment.polarity >= 0:
        sentiment["positive"] = True
    else:
        sentiment["positive"] = False

    return sentiment 
