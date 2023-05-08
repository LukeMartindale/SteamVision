from rest_framework.test import APITestCase, APIClient

from home.models import (
    Game,
    GameStat,
)

from django.utils import timezone

class TestSentimentgetters(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.test_data = [
            {"label": "-1", "value": 0}, 
            {"label": "-0.9", "value": 0}, 
            {"label": "-0.8", "value": 0}, 
            {"label": "-0.7", "value": 0}, 
            {"label": "-0.6", "value": 0}, 
            {"label": "-0.5", "value": 0}, 
            {"label": "-0.4", "value": 0}, 
            {"label": "-0.3", "value": 0},
            {"label": "-0.2", "value": 0},
            {"label": "-0.1", "value": 0},
            {"label": "0", "value": 0},
            {"label": "0.1", "value": 0},
            {"label": "0.2", "value": 0},
            {"label": "0.3", "value": 0},
            {"label": "0.4", "value": 0}, 
            {"label": "0.5", "value": 0}, 
            {"label": "0.6", "value": 0}, 
            {"label": "0.7", "value": 0}, 
            {"label": "0.8", "value": 0}, 
            {"label": "0.9", "value": 0}, 
            {"label": "1", "value": 0}
        ]


        time = timezone.now()

        temp_data = []
        for i in range(0, 12):
            temp_data.append(
                {"year": time.year, 
                 "month": "January", 
                 "sentiment": [
                    {"label": "-1", "value": 0}, 
                    {"label": "-0.9", "value": 0}, 
                    {"label": "-0.8", "value": 0}, 
                    {"label": "-0.7", "value": 0}, 
                    {"label": "-0.6", "value": 0}, 
                    {"label": "-0.5", "value": 0}, 
                    {"label": "-0.4", "value": 0}, 
                    {"label": "-0.3", "value": 0},
                    {"label": "-0.2", "value": 0},
                    {"label": "-0.1", "value": 0},
                    {"label": "0", "value": 0},
                    {"label": "0.1", "value": 0},
                    {"label": "0.2", "value": 0},
                    {"label": "0.3", "value": 0},
                    {"label": "0.4", "value": 0}, 
                    {"label": "0.5", "value": 0}, 
                    {"label": "0.6", "value": 0}, 
                    {"label": "0.7", "value": 0}, 
                    {"label": "0.8", "value": 0}, 
                    {"label": "0.9", "value": 0}, 
                    {"label": "1", "value": 0}
                ]
                }
            )

        # Create game Object
        game = Game(app_id=10)
        game.save()

        # Create GameStat Object
        game_stat = GameStat(
            app_id=game, 
            sentiment_all_time=self.test_data,
            sentiment_all_time_month=temp_data,
            sentiment_past_one_month=self.test_data,
        )
        game_stat.save()

        self.assert_data = '[{"label":"-1","value":0},{"label":"-0.9","value":0},{"label":"-0.8","value":0},{"label":"-0.7","value":0},{"label":"-0.6","value":0},{"label":"-0.5","value":0},{"label":"-0.4","value":0},{"label":"-0.3","value":0},{"label":"-0.2","value":0},{"label":"-0.1","value":0},{"label":"0","value":0},{"label":"0.1","value":0},{"label":"0.2","value":0},{"label":"0.3","value":0},{"label":"0.4","value":0},{"label":"0.5","value":0},{"label":"0.6","value":0},{"label":"0.7","value":0},{"label":"0.8","value":0},{"label":"0.9","value":0},{"label":"1","value":0}]'
        self.month_assert_data = '[{"year":2023,"month":"January","sentiment":[{"label":"-1","value":0},{"label":"-0.9","value":0},{"label":"-0.8","value":0},{"label":"-0.7","value":0},{"label":"-0.6","value":0},{"label":"-0.5","value":0},{"label":"-0.4","value":0},{"label":"-0.3","value":0},{"label":"-0.2","value":0},{"label":"-0.1","value":0},{"label":"0","value":0},{"label":"0.1","value":0},{"label":"0.2","value":0},{"label":"0.3","value":0},{"label":"0.4","value":0},{"label":"0.5","value":0},{"label":"0.6","value":0},{"label":"0.7","value":0},{"label":"0.8","value":0},{"label":"0.9","value":0},{"label":"1","value":0}]},{"year":2023,"month":"January","sentiment":[{"label":"-1","value":0},{"label":"-0.9","value":0},{"label":"-0.8","value":0},{"label":"-0.7","value":0},{"label":"-0.6","value":0},{"label":"-0.5","value":0},{"label":"-0.4","value":0},{"label":"-0.3","value":0},{"label":"-0.2","value":0},{"label":"-0.1","value":0},{"label":"0","value":0},{"label":"0.1","value":0},{"label":"0.2","value":0},{"label":"0.3","value":0},{"label":"0.4","value":0},{"label":"0.5","value":0},{"label":"0.6","value":0},{"label":"0.7","value":0},{"label":"0.8","value":0},{"label":"0.9","value":0},{"label":"1","value":0}]},{"year":2023,"month":"January","sentiment":[{"label":"-1","value":0},{"label":"-0.9","value":0},{"label":"-0.8","value":0},{"label":"-0.7","value":0},{"label":"-0.6","value":0},{"label":"-0.5","value":0},{"label":"-0.4","value":0},{"label":"-0.3","value":0},{"label":"-0.2","value":0},{"label":"-0.1","value":0},{"label":"0","value":0},{"label":"0.1","value":0},{"label":"0.2","value":0},{"label":"0.3","value":0},{"label":"0.4","value":0},{"label":"0.5","value":0},{"label":"0.6","value":0},{"label":"0.7","value":0},{"label":"0.8","value":0},{"label":"0.9","value":0},{"label":"1","value":0}]},{"year":2023,"month":"January","sentiment":[{"label":"-1","value":0},{"label":"-0.9","value":0},{"label":"-0.8","value":0},{"label":"-0.7","value":0},{"label":"-0.6","value":0},{"label":"-0.5","value":0},{"label":"-0.4","value":0},{"label":"-0.3","value":0},{"label":"-0.2","value":0},{"label":"-0.1","value":0},{"label":"0","value":0},{"label":"0.1","value":0},{"label":"0.2","value":0},{"label":"0.3","value":0},{"label":"0.4","value":0},{"label":"0.5","value":0},{"label":"0.6","value":0},{"label":"0.7","value":0},{"label":"0.8","value":0},{"label":"0.9","value":0},{"label":"1","value":0}]},{"year":2023,"month":"January","sentiment":[{"label":"-1","value":0},{"label":"-0.9","value":0},{"label":"-0.8","value":0},{"label":"-0.7","value":0},{"label":"-0.6","value":0},{"label":"-0.5","value":0},{"label":"-0.4","value":0},{"label":"-0.3","value":0},{"label":"-0.2","value":0},{"label":"-0.1","value":0},{"label":"0","value":0},{"label":"0.1","value":0},{"label":"0.2","value":0},{"label":"0.3","value":0},{"label":"0.4","value":0},{"label":"0.5","value":0},{"label":"0.6","value":0},{"label":"0.7","value":0},{"label":"0.8","value":0},{"label":"0.9","value":0},{"label":"1","value":0}]},{"year":2023,"month":"January","sentiment":[{"label":"-1","value":0},{"label":"-0.9","value":0},{"label":"-0.8","value":0},{"label":"-0.7","value":0},{"label":"-0.6","value":0},{"label":"-0.5","value":0},{"label":"-0.4","value":0},{"label":"-0.3","value":0},{"label":"-0.2","value":0},{"label":"-0.1","value":0},{"label":"0","value":0},{"label":"0.1","value":0},{"label":"0.2","value":0},{"label":"0.3","value":0},{"label":"0.4","value":0},{"label":"0.5","value":0},{"label":"0.6","value":0},{"label":"0.7","value":0},{"label":"0.8","value":0},{"label":"0.9","value":0},{"label":"1","value":0}]},{"year":2023,"month":"January","sentiment":[{"label":"-1","value":0},{"label":"-0.9","value":0},{"label":"-0.8","value":0},{"label":"-0.7","value":0},{"label":"-0.6","value":0},{"label":"-0.5","value":0},{"label":"-0.4","value":0},{"label":"-0.3","value":0},{"label":"-0.2","value":0},{"label":"-0.1","value":0},{"label":"0","value":0},{"label":"0.1","value":0},{"label":"0.2","value":0},{"label":"0.3","value":0},{"label":"0.4","value":0},{"label":"0.5","value":0},{"label":"0.6","value":0},{"label":"0.7","value":0},{"label":"0.8","value":0},{"label":"0.9","value":0},{"label":"1","value":0}]},{"year":2023,"month":"January","sentiment":[{"label":"-1","value":0},{"label":"-0.9","value":0},{"label":"-0.8","value":0},{"label":"-0.7","value":0},{"label":"-0.6","value":0},{"label":"-0.5","value":0},{"label":"-0.4","value":0},{"label":"-0.3","value":0},{"label":"-0.2","value":0},{"label":"-0.1","value":0},{"label":"0","value":0},{"label":"0.1","value":0},{"label":"0.2","value":0},{"label":"0.3","value":0},{"label":"0.4","value":0},{"label":"0.5","value":0},{"label":"0.6","value":0},{"label":"0.7","value":0},{"label":"0.8","value":0},{"label":"0.9","value":0},{"label":"1","value":0}]},{"year":2023,"month":"January","sentiment":[{"label":"-1","value":0},{"label":"-0.9","value":0},{"label":"-0.8","value":0},{"label":"-0.7","value":0},{"label":"-0.6","value":0},{"label":"-0.5","value":0},{"label":"-0.4","value":0},{"label":"-0.3","value":0},{"label":"-0.2","value":0},{"label":"-0.1","value":0},{"label":"0","value":0},{"label":"0.1","value":0},{"label":"0.2","value":0},{"label":"0.3","value":0},{"label":"0.4","value":0},{"label":"0.5","value":0},{"label":"0.6","value":0},{"label":"0.7","value":0},{"label":"0.8","value":0},{"label":"0.9","value":0},{"label":"1","value":0}]},{"year":2023,"month":"January","sentiment":[{"label":"-1","value":0},{"label":"-0.9","value":0},{"label":"-0.8","value":0},{"label":"-0.7","value":0},{"label":"-0.6","value":0},{"label":"-0.5","value":0},{"label":"-0.4","value":0},{"label":"-0.3","value":0},{"label":"-0.2","value":0},{"label":"-0.1","value":0},{"label":"0","value":0},{"label":"0.1","value":0},{"label":"0.2","value":0},{"label":"0.3","value":0},{"label":"0.4","value":0},{"label":"0.5","value":0},{"label":"0.6","value":0},{"label":"0.7","value":0},{"label":"0.8","value":0},{"label":"0.9","value":0},{"label":"1","value":0}]},{"year":2023,"month":"January","sentiment":[{"label":"-1","value":0},{"label":"-0.9","value":0},{"label":"-0.8","value":0},{"label":"-0.7","value":0},{"label":"-0.6","value":0},{"label":"-0.5","value":0},{"label":"-0.4","value":0},{"label":"-0.3","value":0},{"label":"-0.2","value":0},{"label":"-0.1","value":0},{"label":"0","value":0},{"label":"0.1","value":0},{"label":"0.2","value":0},{"label":"0.3","value":0},{"label":"0.4","value":0},{"label":"0.5","value":0},{"label":"0.6","value":0},{"label":"0.7","value":0},{"label":"0.8","value":0},{"label":"0.9","value":0},{"label":"1","value":0}]},{"year":2023,"month":"January","sentiment":[{"label":"-1","value":0},{"label":"-0.9","value":0},{"label":"-0.8","value":0},{"label":"-0.7","value":0},{"label":"-0.6","value":0},{"label":"-0.5","value":0},{"label":"-0.4","value":0},{"label":"-0.3","value":0},{"label":"-0.2","value":0},{"label":"-0.1","value":0},{"label":"0","value":0},{"label":"0.1","value":0},{"label":"0.2","value":0},{"label":"0.3","value":0},{"label":"0.4","value":0},{"label":"0.5","value":0},{"label":"0.6","value":0},{"label":"0.7","value":0},{"label":"0.8","value":0},{"label":"0.9","value":0},{"label":"1","value":0}]}]'


    def test_sentiment_get_data_all_time(self):
        response = self.client.get("/api/get-sentiment/all-time/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, self.assert_data)

    def test_sentiment_get_data_all_time_status_code(self):
        response = self.client.get("/api/get-sentiment/all-time/10/")
        self.assertEqual(response.status_code, 200)

    def test_sentiment_get_data_all_time_month(self):
        response = self.client.get("/api/get-sentiment/all-time-month/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, self.month_assert_data)

    def test_sentiment_get_data_all_time_month_status_code(self):
        response = self.client.get("/api/get-sentiment/all-time-month/10/")
        self.assertEqual(response.status_code, 200)

    def test_sentiment_get_data_past_twelve_months(self):
        response = self.client.get("/api/get-sentiment/past-twelve-months/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, self.assert_data)

    def test_sentiment_get_data_past_twelve_months_status_code(self):
        response = self.client.get("/api/get-sentiment/past-twelve-months/10/")
        self.assertEqual(response.status_code, 200)
