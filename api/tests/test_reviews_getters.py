from django.test import TestCase, Client
from rest_framework.test import APITestCase, APIClient

from home.models import (
    Game,
    GameStat,
)

from django.utils import timezone

class TestReviewsGetters(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.test_data = {'test_data': 'test_content'}

        time = timezone.now()
        self.month_test_data = [
            {"year": time.year, "month": "Janurary"},
            {"year": time.year, "month": "February"},
            {"year": time.year, "month": "March"},
            {"year": time.year, "month": "April"},
            {"year": time.year, "month": "May"},
            {"year": time.year, "month": "June"},
            {"year": time.year, "month": "July"},
            {"year": time.year, "month": "August"},
            {"year": time.year, "month": "September"},
            {"year": time.year, "month": "October"},
            {"year": time.year, "month": "November"},
            {"year": time.year, "month": "December"},
        ]

        # Create game Object
        game = Game(app_id=10)
        game.save()

        # Create GameStat Object
        game_stat = GameStat(
            app_id=game, 
            reviews_all_time_year=self.test_data,
            reviews_all_time_month=self.month_test_data,
        )
        game_stat.save()


    def test_reviews_get_data_all_time(self):
        response = self.client.get("/api/get-reviews/all-time-year/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, '{"test_data":"test_content"}')


    def test_reviews_get_data_past_twelve_months(self):
        response = self.client.get("/api/get-reviews/past-twelve-months/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, '[]')

    def test_reviews_get_data_past_six_months(self):
        response = self.client.get("/api/get-reviews/past-six-months/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, '[]')
