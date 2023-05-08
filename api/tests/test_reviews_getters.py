from django.test import TestCase, Client
from rest_framework.test import APITestCase, APIClient

from home.models import (
    Game,
    GameStat,
)

class TestReviewsGetters(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.test_data = {'test_data': 'test_content'}

        # Create game Object
        game = Game(app_id=10)
        game.save()

        # Create GameStat Object
        game_stat = GameStat(app_id=game, reviews_all_time_year=self.test_data)
        game_stat.save()


    def test_reviews_get_data_all_time(self):
        response = self.client.get("/api/get-reviews/all-time-year/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, '{"test_data":"test_content"}')
