from textblob import TextBlob
import pandas as pd

url = 'test_files/10_CounterStrike.csv'

def get_sentiment(url):
    data = pd.read_csv(url)

    sentiment = []

    for i in range(len(data.index)):
        text = data['review'][i]

        value = TextBlob(str(text))
        sentiment.append(round(value.sentiment.polarity, 1))

    sentiment_data = [
        { 'label': '-1', 'value': sentiment.count(-1) },
        { 'label': '-0.9', 'value': sentiment.count(-0.9) },
        { 'label': '-0.8', 'value': sentiment.count(-0.8) },
        { 'label': '-0.7', 'value': sentiment.count(-0.7) },
        { 'label': '-0.6', 'value': sentiment.count(-0.6) },
        { 'label': '-0.5', 'value': sentiment.count(-0.5) },
        { 'label': '-0.4', 'value': sentiment.count(-0.4) },
        { 'label': '-0.3', 'value': sentiment.count(-0.3) },
        { 'label': '-0.2', 'value': sentiment.count(-0.2) },
        { 'label': '-0.1', 'value': sentiment.count(-0.1) },
        { 'label': '0', 'value': sentiment.count(0) },
        { 'label': '0.1', 'value': sentiment.count(0.1) },
        { 'label': '0.2', 'value': sentiment.count(0.2) },
        { 'label': '0.3', 'value': sentiment.count(0.3) },
        { 'label': '0.4', 'value': sentiment.count(0.4) },
        { 'label': '0.5', 'value': sentiment.count(0.5) },
        { 'label': '0.6', 'value': sentiment.count(0.6) },
        { 'label': '0.7', 'value': sentiment.count(0.7) },
        { 'label': '0.8', 'value': sentiment.count(0.8) },
        { 'label': '0.9', 'value': sentiment.count(0.9) },
        { 'label': '1', 'value': sentiment.count(1) },
    ]

    return sentiment_data
