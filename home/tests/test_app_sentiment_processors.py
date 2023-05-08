from django.test import TestCase, Client

from data_processors.app_sentiment import (
    app_sentiment,
    app_all_sentiment,
    app_sentiment_all_time_month,
    app_sentiment_all_time_month_all,
    app_sentiment_past_one_month,
    app_sentiment_past_one_month_all,
    app_sentiment_past_two_weeks,
    app_sentiment_past_two_weeks_all,
    app_sentiment_past_one_week,
    app_sentiment_past_one_week_all,
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

        self.assert_data = [
        { 'label': '-1', 'value': 0 },
        { 'label': '-0.9', 'value': 0 },
        { 'label': '-0.8', 'value': 0 },
        { 'label': '-0.7', 'value': 0 },
        { 'label': '-0.6', 'value': 0 },
        { 'label': '-0.5', 'value': 0 },
        { 'label': '-0.4', 'value': 0 },
        { 'label': '-0.3', 'value': 0 },
        { 'label': '-0.2', 'value': 0 },
        { 'label': '-0.1', 'value': 0 },
        { 'label': '0', 'value': 0 },
        { 'label': '0.1', 'value': 0 },
        { 'label': '0.2', 'value': 0 },
        { 'label': '0.3', 'value': 0 },
        { 'label': '0.4', 'value': 0 },
        { 'label': '0.5', 'value': 0 },
        { 'label': '0.6', 'value': 0 },
        { 'label': '0.7', 'value': 0 },
        { 'label': '0.8', 'value': 0 },
        { 'label': '0.9', 'value': 0 },
        { 'label': '1', 'value': 0 },
    ]

    #ALL TIME 
    def test_app_sentiment_assert_writes_correct_value(self):
        app_sentiment(10)
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.sentiment_all_time, self.assert_data)

    def test_app_all_sentiment_assert_writes_correct_value(self):
        app_all_sentiment()
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.sentiment_all_time, self.assert_data)

    #ALL TIME MONTH
    def test_app_sentiment_all_time_month_assert_writes_correct_value(self):
        app_sentiment_all_time_month(10)
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.sentiment_all_time, {})

    def test_app_sentiment_all_time_month_all_assert_writes_correct_value(self):
        app_sentiment_all_time_month_all()
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.sentiment_all_time, {})

    # PAST ONE MONTH
    def test_app_sentiment_past_one_month_assert_writes_correct_value(self):
        app_sentiment_past_one_month(10)
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.sentiment_all_time, {})

    def test_app_sentiment_past_one_month_all_assert_writes_correct_value(self):
        app_sentiment_past_one_month_all()
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.sentiment_all_time, {})

    # PAST TWO WEEKS
    def test_app_sentiment_past_two_weeks_assert_writes_correct_value(self):
        app_sentiment_past_two_weeks(10)
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.sentiment_all_time, {})

    def test_app_sentiment_past_two_weeks_all_assert_writes_correct_value(self):
        app_sentiment_past_two_weeks_all()
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.sentiment_all_time, {})

    # PAST ONE WEEK
    def test_app_sentiment_past_one_week_assert_writes_correct_value(self):
        app_sentiment_past_one_week(10)
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.sentiment_all_time, {})

    def test_app_sentiment_past_one_week_all_assert_writes_correct_value(self):
        app_sentiment_past_one_week_all()
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.sentiment_all_time, {})