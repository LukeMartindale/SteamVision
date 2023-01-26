from home.models import Game, GameStat, Review

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

    game_stats.emotion = emotions
    
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

        game_stats.emotion = emotions
        
        game_stats.save()
