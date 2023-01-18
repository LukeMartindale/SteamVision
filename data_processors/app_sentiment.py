from home.models import Game, GameStat, Review

def app_sentiment(app):

    game = Game.objects.get(app_id=app)
    reviews = Review.objects.filter(app_id=game)

    sentiment = []
    for i in range(len(reviews)):
        sentiment.append(round(reviews[i].sentiment_polarity, 1))

    #Try to get the Gamestats object for this game
    try:
        game_stats = GameStat.objects.get(app_id=game)
    except GameStat.DoesNotExist:
        #If does not exist create
        game_stats = GameStat()
        game_stats.app_id = game

    app_sentiment = rounded_sentiment(sentiment)
    game_stats.sentiment = app_sentiment

    game_stats.save()

    return app_sentiment

def rounded_sentiment(data):

    sentiment = [
        { 'label': '-1', 'value': data.count(-1) },
        { 'label': '-0.9', 'value': data.count(-0.9) },
        { 'label': '-0.8', 'value': data.count(-0.8) },
        { 'label': '-0.7', 'value': data.count(-0.7) },
        { 'label': '-0.6', 'value': data.count(-0.6) },
        { 'label': '-0.5', 'value': data.count(-0.5) },
        { 'label': '-0.4', 'value': data.count(-0.4) },
        { 'label': '-0.3', 'value': data.count(-0.3) },
        { 'label': '-0.2', 'value': data.count(-0.2) },
        { 'label': '-0.1', 'value': data.count(-0.1) },
        { 'label': '0', 'value': data.count(0) },
        { 'label': '0.1', 'value': data.count(0.1) },
        { 'label': '0.2', 'value': data.count(0.2) },
        { 'label': '0.3', 'value': data.count(0.3) },
        { 'label': '0.4', 'value': data.count(0.4) },
        { 'label': '0.5', 'value': data.count(0.5) },
        { 'label': '0.6', 'value': data.count(0.6) },
        { 'label': '0.7', 'value': data.count(0.7) },
        { 'label': '0.8', 'value': data.count(0.8) },
        { 'label': '0.9', 'value': data.count(0.9) },
        { 'label': '1', 'value': data.count(1) },
    ]

    return sentiment
