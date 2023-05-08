from django.test import TestCase, Client

from data_processors.app_emotions import (
    app_emotions,
    app_all_emotions,
    app_emotion_all_time_month,
    app_emotion_all_time_month_all,
    app_emotion_past_one_month,
    app_emotion_past_one_month_all,
    app_emotion_past_two_weeks,
    app_emotion_past_two_weeks_all,
    app_emotion_past_one_week,
    app_emotion_past_one_week_all,
)

from home.models import (
    Game,
    GameStat,
)

# Create your tests here.
class TestSentimentProcessor(TestCase):

    def setUp(self):
        self.client = Client()

        game = Game(app_id=10)
        game.save()

        gamestat = GameStat(app_id=game)
        gamestat.save()

    def test_app_emotions_assert_returns_true(self):
        result = app_emotions(10)
        self.assertTrue(result)

    def test_app_emotions_assert_writes_correct_value(self):
        app_emotions(10)
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.emotion_all_time, {'Happy': 0, 'Angry': 0, 'Surprise': 0, 'Sad': 0, 'Fear': 0})

    def test_app_all_emotions_assert_writes_correct_value(self):
        app_all_emotions()
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.emotion_all_time, {'Happy': 0, 'Angry': 0, 'Surprise': 0, 'Sad': 0, 'Fear': 0})

    def test_app_emotions_all_time_month_assert_writes_correct_value(self):
        app_emotion_all_time_month(10)
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.emotion_all_time, {})

    def test_app_emotions_all_time_month_all_assert_writes_correct_value(self):
        app_emotion_all_time_month_all()
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.emotion_all_time, {})


    def test_app_emotions_past_one_month_assert_writes_correct_value(self):
        app_emotion_past_one_month(10)
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.emotion_all_time, {})

    def test_app_emotions_past_one_month_all_assert_writes_correct_value(self):
        app_emotion_past_one_month_all()
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.emotion_all_time, {})


    def test_app_emotions_past_two_weeks_assert_writes_correct_value(self):
        app_emotion_past_two_weeks(10)
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.emotion_all_time, {})

    def test_app_emotions_past_two_weeks_all_assert_writes_correct_value(self):
        app_emotion_past_two_weeks_all()
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.emotion_all_time, {})

    def test_app_emotions_past_one_week_assert_writes_correct_value(self):
        app_emotion_past_one_week(10)
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.emotion_all_time, {})

    def test_app_emotions_past_one_week_all_assert_writes_correct_value(self):
        app_emotion_past_one_week_all()
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.emotion_all_time, {})