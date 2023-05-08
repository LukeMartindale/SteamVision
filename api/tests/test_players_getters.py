from rest_framework.test import APITestCase, APIClient

from home.models import (
    Game,
    GameStat,
    PlayerCount,
)

from django.utils import timezone

class TestPlayersgetters(APITestCase):

    def setUp(self):
        self.client = APIClient()

        # Create game Object
        game = Game(app_id=10)
        game.save()

        self.time = timezone.now()

        players = PlayerCount(app_id=game, player_count=1, timestamp=self.time)
        players.save()

        self.assert_data = players

    def test_player_get_data_all_time(self):
        response = self.client.get("/api/get-player-count/all-time/10/")
        content = response.content.decode('utf-8')
        self.assertIsNotNone(content)

    def test_player_get_data_all_time_status_code(self):
        response = self.client.get("/api/get-player-count/all-time/10/")
        self.assertEqual(response.status_code, 200)

    def test_player_get_data_past_one_month(self):
        response = self.client.get("/api/get-player-count/past-one-month/10/")
        content = response.content.decode('utf-8')
        self.assertIsNotNone(content)

    def test_player_get_data_past_one_month_status_code(self):
        response = self.client.get("/api/get-player-count/past-one-month/10/")
        self.assertEqual(response.status_code, 200)

    def test_player_get_data_past_two_weeks(self):
        response = self.client.get("/api/get-player-count/past-two-weeks/10/")
        content = response.content.decode('utf-8')
        self.assertIsNotNone(content)

    def test_player_get_data_past_two_weeks_status_code(self):
        response = self.client.get("/api/get-player-count/past-two-weeks/10/")
        self.assertEqual(response.status_code, 200)

    def test_player_get_data_past_one_week(self):
        response = self.client.get("/api/get-player-count/past-one-week/10/")
        content = response.content.decode('utf-8')
        self.assertIsNotNone(content)

    def test_player_get_data_past_one_week_status_code(self):
        response = self.client.get("/api/get-player-count/past-one-week/10/")
        self.assertEqual(response.status_code, 200)

    def test_player_get_data_past_72_hours(self):
        response = self.client.get("/api/get-player-count/past-72-hours/10/")
        content = response.content.decode('utf-8')
        self.assertIsNotNone(content)

    def test_player_get_data_past_72_hours_status_code(self):
        response = self.client.get("/api/get-player-count/past-72-hours/10/")
        self.assertEqual(response.status_code, 200)

    def test_player_get_data_past_48_hours(self):
        response = self.client.get("/api/get-player-count/past-48-hours/10/")
        content = response.content.decode('utf-8')
        self.assertIsNotNone(content)

    def test_player_get_data_past_48_hours_status_code(self):
        response = self.client.get("/api/get-player-count/past-48-hours/10/")
        self.assertEqual(response.status_code, 200)

    def test_player_get_data_past_24_hours(self):
        response = self.client.get("/api/get-player-count/past-24-hours/10/")
        content = response.content.decode('utf-8')
        self.assertIsNotNone(content)

    def test_player_get_data_past_24_hours_status_code(self):
        response = self.client.get("/api/get-player-count/past-24-hours/10/")
        self.assertEqual(response.status_code, 200)

