from rest_framework.test import APITestCase, APIClient

from home.models import (
    Game,
    GameStat,
)

from django.utils import timezone
import calendar

class TestEmotiongetters(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.test_data = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}

        time = timezone.now()

        temp_data = []
        for i in range(1, 13):
            temp_data.append(
                {"year": time.year, 
                 "month": calendar.month_name[i], 
                 "emotion": {"Happy":0,"Angry":0,"Surprise":0,"Sad":0,"Fear":0}
                }
            )

        # Create game Object
        game = Game(app_id=10)
        game.save()

        # Create GameStat Object
        game_stat = GameStat(
            app_id=game, 
            emotion_all_time=self.test_data,
            emotion_all_time_month=temp_data,
            emotion_past_one_month=self.test_data,
            emotion_past_two_weeks=self.test_data,
            emotion_past_one_week=self.test_data,
        )
        game_stat.save()

        self.assert_data = '{"Happy":0,"Angry":0,"Surprise":0,"Sad":0,"Fear":0}'
        self.month_assert_data = '[{"year":2023,"month":"January","emotion":{"Happy":0,"Angry":0,"Surprise":0,"Sad":0,"Fear":0}},{"year":2023,"month":"February","emotion":{"Happy":0,"Angry":0,"Surprise":0,"Sad":0,"Fear":0}},{"year":2023,"month":"March","emotion":{"Happy":0,"Angry":0,"Surprise":0,"Sad":0,"Fear":0}},{"year":2023,"month":"April","emotion":{"Happy":0,"Angry":0,"Surprise":0,"Sad":0,"Fear":0}},{"year":2023,"month":"May","emotion":{"Happy":0,"Angry":0,"Surprise":0,"Sad":0,"Fear":0}},{"year":2023,"month":"June","emotion":{"Happy":0,"Angry":0,"Surprise":0,"Sad":0,"Fear":0}},{"year":2023,"month":"July","emotion":{"Happy":0,"Angry":0,"Surprise":0,"Sad":0,"Fear":0}},{"year":2023,"month":"August","emotion":{"Happy":0,"Angry":0,"Surprise":0,"Sad":0,"Fear":0}},{"year":2023,"month":"September","emotion":{"Happy":0,"Angry":0,"Surprise":0,"Sad":0,"Fear":0}},{"year":2023,"month":"October","emotion":{"Happy":0,"Angry":0,"Surprise":0,"Sad":0,"Fear":0}},{"year":2023,"month":"November","emotion":{"Happy":0,"Angry":0,"Surprise":0,"Sad":0,"Fear":0}},{"year":2023,"month":"December","emotion":{"Happy":0,"Angry":0,"Surprise":0,"Sad":0,"Fear":0}}]'

    def test_emotion_get_data_all_time(self):
        response = self.client.get("/api/get-emotion/all-time/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, self.assert_data)

    def test_emotion_get_data_all_time_status_code(self):
        response = self.client.get("/api/get-emotion/all-time/10/")
        self.assertEqual(response.status_code, 200)

    def test_emotion_get_data_all_time_month(self):
        response = self.client.get("/api/get-emotion/all-time-month/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, self.month_assert_data)

    def test_emotion_get_data_all_time_month_status_code(self):
        response = self.client.get("/api/get-emotion/all-time-month/10/")
        self.assertEqual(response.status_code, 200)

    def test_emotion_get_data_all_time_month(self):
        response = self.client.get("/api/get-emotion/all-time-month/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, self.month_assert_data)

    def test_emotion_get_data_all_time_month_status_code(self):
        response = self.client.get("/api/get-emotion/all-time-month/10/")
        self.assertEqual(response.status_code, 200)

    def test_emotion_get_data_past_twelve_months_month(self):
        response = self.client.get("/api/get-emotion/past-twelve-months/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, self.assert_data)

    def test_emotion_get_data_past_twelve_months_status_code(self):
        response = self.client.get("/api/get-emotion/past-twelve-months/10/")
        self.assertEqual(response.status_code, 200)

    def test_emotion_get_data_past_six_months(self):
        response = self.client.get("/api/get-emotion/past-six-months/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, self.assert_data)

    def test_emotion_get_data_past_six_months_status_code(self):
        response = self.client.get("/api/get-emotion/past-six-months/10/")
        self.assertEqual(response.status_code, 200)

    def test_emotion_get_data_past_one_month(self):
        response = self.client.get("/api/get-emotion/past-one-month/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, self.assert_data)

    def test_emotion_get_data_past_one_month_status_code(self):
        response = self.client.get("/api/get-emotion/past-one-month/10/")
        self.assertEqual(response.status_code, 200)

    def test_emotion_get_data_past_two_weeks(self):
        response = self.client.get("/api/get-emotion/past-two-weeks/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, self.assert_data)

    def test_emotion_get_data_past_two_weeks_status_code(self):
        response = self.client.get("/api/get-emotion/past-two-weeks/10/")
        self.assertEqual(response.status_code, 200)

    def test_emotion_get_data_past_one_week(self):
        response = self.client.get("/api/get-emotion/past-one-week/10/")
        content = response.content.decode('utf-8')
        self.assertEqual(content, self.assert_data)

    def test_emotion_get_data_past_one_week_status_code(self):
        response = self.client.get("/api/get-emotion/past-one-week/10/")
        self.assertEqual(response.status_code, 200)
    