from django.test import TestCase, Client

from data_processors.reviews_sentiment import reviews_sentiment

# Create your tests here.
class TestSentimentProcessor(TestCase):

    def setUp(self):
        self.client = Client()

        self.text1 = "This is great"
        self.text2 = "This is terrible, I hate this"

    def test_sentiment_processor_positive_correct(self):
        sentiment = reviews_sentiment(self.text1)
        self.assertTrue(sentiment["positive"])

    def test_sentiment_processor_negative_correct(self):
        sentiment = reviews_sentiment(self.text2)
        self.assertFalse(sentiment["positive"])

    def test_sentiment_processor_polarity_check(self):
        sentiment = reviews_sentiment(self.text1)
        self.assertEqual(sentiment["polarity"], 0.8)

    def test_sentiment_processor_polarity_check(self):
        sentiment = reviews_sentiment(self.text2)
        self.assertEqual(sentiment["polarity"], -0.9)

    def test_sentiment_processor_subjectivity_check(self):
        sentiment = reviews_sentiment(self.text1)
        self.assertEqual(sentiment["subjectivity"], 0.75)

    def test_sentiment_processor_subjectivity_check(self):
        sentiment = reviews_sentiment(self.text2)
        self.assertEqual(sentiment["subjectivity"], 0.95)
