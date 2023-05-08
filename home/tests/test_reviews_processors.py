from django.test import TestCase, Client

from data_processors.reviews import (
    reviews_all_time_year,
    reviews_all_time_year_all,
    reviews_all_time_month,
    reviews_all_time_month_all,
    reviews_past_month,
    reviews_past_month_all,
)

from home.models import (
    Game,
    GameStat,
    Review,
)

from django.utils import timezone
import calendar

# Create your tests here.
class TestSentimentProcessor(TestCase):

    def setUp(self):
        self.client = Client()

        game = Game(app_id=10)
        game.save()

        gamestat = GameStat(app_id=game, reviews_all_time_year=[], reviews_all_time_month=[])
        gamestat.save()

        review = Review(app_id=game, review_text="test_text", voted_up=True)
        review.save()

    # ALL TIME YEAR
    def test_reviews_all_time_year_assert_returns_true(self):
        reviews_all_time_year(10)
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.reviews_all_time_year, [{'label': 2023, 'percentage': 100.0, 'number_of_reviews': 1}])

    def test_reviews_all_time_year_all_assert_writes_correct_value(self):
        reviews_all_time_year_all()
        gs = GameStat.objects.get(app_id__app_id=10)
        self.assertEqual(gs.reviews_all_time_year, [])

    # ALL TIME MONTH
    def test_reviews_all_time_month_assert_returns_true(self):
        reviews_all_time_month(10)
        gs = GameStat.objects.get(app_id__app_id=10)
        time = timezone.now()
        label = str(time.year) + " " + calendar.month_name[time.month]
        self.assertEqual(gs.reviews_all_time_month, [{'label': label, 'year': time.year, 'month': calendar.month_name[time.month], 'percentage': 100.0, 'number_of_reviews': 1}])

    def test_reviews_all_time_month_all_assert_writes_correct_value(self):
        reviews_all_time_month_all()
        gs = GameStat.objects.get(app_id__app_id=10)
        time = timezone.now()
        label = str(time.year) + " " + calendar.month_name[time.month]
        self.assertEqual(gs.reviews_all_time_month, [{'label': label, 'year': time.year, 'month': calendar.month_name[time.month], 'percentage': 100.0, 'number_of_reviews': 1}])
