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
        self.months_test_data = [
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

        temp_data = []
        for i in range(0, 14):
            temp_data.append(
                {'test_data': 'test_content'}
            )

        self.month_test_data = temp_data

        # Create game Object
        game = Game(app_id=10)
        game.save()

        # Create GameStat Object
        game_stat = GameStat(
            app_id=game, 
            reviews_all_time_year=self.test_data,
            reviews_all_time_month=self.months_test_data,
            reviews_past_one_month=temp_data,
        )
        game_stat.save()


    def test_reviews_get_data_all_time(self):
        response = self.client.get("/api/get-reviews/all-time-year/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, '{"test_data":"test_content"}')

    def test_reviews_get_data_all_time_status_code(self):
        response = self.client.get("/api/get-reviews/all-time-year/10/")
        self.assertEqual(response.status_code, 200)

    def test_reviews_get_data_past_twelve_months(self):
        response = self.client.get("/api/get-reviews/past-twelve-months/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, '[]')

    def test_reviews_get_data_past_twelve_months_status_code(self):
        response = self.client.get("/api/get-reviews/past-twelve-months/10/")
        self.assertEqual(response.status_code, 200)

    def test_reviews_get_data_past_six_months(self):
        response = self.client.get("/api/get-reviews/past-six-months/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, '[]')

    def test_reviews_get_data_past_six_months_status_code(self):
        response = self.client.get("/api/get-reviews/past-six-months/10/")
        self.assertEqual(response.status_code, 200)

    def test_reviews_get_data_past_one_month(self):
        response = self.client.get("/api/get-reviews/past-one-month/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, content)

    def test_reviews_get_data_past_one_month_status_code(self):
        response = self.client.get("/api/get-reviews/past-one-month/10/")
        self.assertEqual(response.status_code, 200)

    def test_reviews_get_data_past_two_weeks_status_code(self):
        response = self.client.get("/api/get-reviews/past-two-weeks/10/")
        self.assertEqual(response.status_code, 200)

    def test_reviews_get_data_past_one_week_status_code(self):
        response = self.client.get("/api/get-reviews/past-one-week/10/")
        self.assertEqual(response.status_code, 200)
