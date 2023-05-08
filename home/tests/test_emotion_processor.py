from django.test import TestCase, Client

from data_processors.reviews_emotions import reviews_emotions

# Create your tests here.
class TestSentimentProcessor(TestCase):

    def setUp(self):
        self.client = Client()

        self.text = "I love this so much, but I am kinda worried about the future"

    def test_emotion_processor_happy_score_check(self):
        emotions = reviews_emotions(self.text)
        self.assertEqual(emotions["scores"]["Happy"], 0.5)

    def test_emotion_processor_angry_score_check(self):
        emotions = reviews_emotions(self.text)
        self.assertEqual(emotions["scores"]["Angry"], 0.0)

    def test_emotion_processor_surprise_score_check(self):
        emotions = reviews_emotions(self.text)
        self.assertEqual(emotions["scores"]["Surprise"], 0.0)

    def test_emotion_processor_sad_score_check(self):
        emotions = reviews_emotions(self.text)
        self.assertEqual(emotions["scores"]["Sad"], 0.5)

    def test_emotion_processor_fear_score_check(self):
        emotions = reviews_emotions(self.text)
        self.assertEqual(emotions["scores"]["Fear"], 0.0)

    def test_emotion_processor_prominent_emotion_check(self):
        emotions = reviews_emotions(self.text)
        self.assertEqual(emotions["prominent"], ["Happy", "Sad"])
