from home.models import Game, GameStat, Review
from datetime import datetime, timedelta
import calendar

def app_emotions(app):

    game = Game.objects.get(app_id=app)
    reviews = Review.objects.filter(app_id=game)

    emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}
    for i in range(len(reviews)):
        for emotion, score in reviews[i].emotion_scores.items():
            emotions[emotion] += score
    
    #Try to get the Gamestats object for this game
    try:
        game_stats = GameStat.objects.get(app_id=game)
    except GameStat.DoesNotExist:
        #If does not exist create
        game_stats = GameStat()
        game_stats.app_id = game

    game_stats.emotion_all_time = emotions
    
    game_stats.save()

    return True

def app_all_emotions():

    games = Game.objects.all()

    for game in games:

        reviews = Review.objects.filter(app_id=game)

        emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}
        for i in range(len(reviews)):
            for emotion, score in reviews[i].emotion_scores.items():
                emotions[emotion] += score

        #Try to get the Gamestats object for this game
        try:
            game_stats = GameStat.objects.get(app_id=game)
        except GameStat.DoesNotExist:
            #If does not exist create
            game_stats = GameStat()
            game_stats.app_id = game

        game_stats.emotion_all_time = emotions
        
        game_stats.save()

def app_emotion_all_time_month(id):
    game = Game.objects.get(app_id=id)
    years = [y.year for y in Review.objects.filter(app_id__app_id__contains=id).dates('time_created', 'year')]

    app_emotion = []

    for year in years:
        for i in range(1, 13):
            reviews = Review.objects.filter(app_id__app_id__contains=id, time_created__year=year, time_created__month=i).order_by("time_created")
            emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}

            for review in reviews:
                for emotion, score in review.emotion_scores.items():
                    emotions[emotion] += score

            app_emotion.append({
                "label": (str(year) + " " + str(calendar.month_name[i])),
                "year": year,
                "month": calendar.month_name[i],
                "emotion": emotions,
                })
    
    #Try to get the Gamestats object for this game
    try:
        game_stats = GameStat.objects.get(app_id=game)
    except GameStat.DoesNotExist:
        #If does not exist create
        game_stats = GameStat()
        game_stats.app_id = game

    game_stats.emotion_all_time_month = app_emotion
    game_stats.save()

def app_emotion_all_time_month_all():
    games = Game.objects.all()


    for game in games:
        years = [y.year for y in Review.objects.filter(app_id=game).dates('time_created', 'year')]
        app_emotion = []

        for year in years:
            for i in range(1, 13):
                reviews = Review.objects.filter(app_id=game, time_created__year=year, time_created__month=i).order_by("time_created")
                emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}

                for review in reviews:
                    for emotion, score in review.emotion_scores.items():
                        emotions[emotion] += score

                app_emotion.append({
                    "label": (str(year) + " " + str(calendar.month_name[i])),
                    "year": year,
                    "month": calendar.month_name[i],
                    "emotion": emotions,
                    })
        
        #Try to get the Gamestats object for this game
        try:
            game_stats = GameStat.objects.get(app_id=game)
        except GameStat.DoesNotExist:
            #If does not exist create
            game_stats = GameStat()
            game_stats.app_id = game

        game_stats.emotion_all_time_month = app_emotion
        game_stats.save()

def app_emotion_past_one_month(id):
    start_date = datetime.now() + timedelta(days=-30)
    end_date = datetime.now()

    reviews = Review.objects.filter(app_id__app_id__contains=id, time_created__range=[start_date, end_date]).order_by('time_created')

    emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}

    for review in reviews:
        for emotion, score in review.emotion_scores.items():
            emotions[emotion] += score

    stats = GameStat.objects.get(app_id__app_id__contains=id)
    stats.emotion_past_one_month = emotions
    stats.save()

def app_emotion_past_one_month_all():
    games = Game.objects.all()

    for game in games:
        start_date = datetime.now() + timedelta(days=-30)
        end_date = datetime.now()

        reviews = Review.objects.filter(app_id=game, time_created__range=[start_date, end_date]).order_by('time_created')

        emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}

        for review in reviews:
            for emotion, score in review.emotion_scores.items():
                emotions[emotion] += score

        stats = GameStat.objects.get(app_id=game)
        stats.emotion_past_one_month = emotions
        stats.save()

def app_emotion_past_two_weeks(id):
    start_date = datetime.now() + timedelta(days=-14)
    end_date = datetime.now()

    reviews = Review.objects.filter(app_id__app_id__contains=id, time_created__range=[start_date, end_date]).order_by('time_created')

    emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}

    for review in reviews:
        for emotion, score in review.emotion_scores.items():
            emotions[emotion] += score

    stats = GameStat.objects.get(app_id__app_id__contains=id)
    stats.emotion_past_two_weeks = emotions
    stats.save()

def app_emotion_past_two_weeks_all():
    games = Game.objects.all()

    for game in games:
        start_date = datetime.now() + timedelta(days=-14)
        end_date = datetime.now()

        reviews = Review.objects.filter(app_id=game, time_created__range=[start_date, end_date]).order_by('time_created')

        emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}

        for review in reviews:
            for emotion, score in review.emotion_scores.items():
                emotions[emotion] += score

        stats = GameStat.objects.get(app_id=game)
        stats.emotion_past_two_weeks = emotions
        stats.save()

def app_emotion_past_one_week(id):
    start_date = datetime.now() + timedelta(days=-7)
    end_date = datetime.now()

    reviews = Review.objects.filter(app_id__app_id__contains=id, time_created__range=[start_date, end_date]).order_by('time_created')

    emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}

    for review in reviews:
        for emotion, score in review.emotion_scores.items():
            emotions[emotion] += score

    stats = GameStat.objects.get(app_id__app_id__contains=id)
    stats.emotion_past_one_week = emotions
    stats.save()

def app_emotion_past_one_week_all():
    games = Game.objects.all()

    for game in games:
        start_date = datetime.now() + timedelta(days=-7)
        end_date = datetime.now()

        reviews = Review.objects.filter(app_id=game, time_created__range=[start_date, end_date]).order_by('time_created')

        emotions = {"Happy": 0, "Angry": 0, "Surprise": 0, "Sad": 0, "Fear": 0}

        for review in reviews:
            for emotion, score in review.emotion_scores.items():
                emotions[emotion] += score

        stats = GameStat.objects.get(app_id=game)
        stats.emotion_past_one_week = emotions
        stats.save()
