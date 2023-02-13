from home.models import Game, GameStat, Review
from django.utils import timezone

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

def app_all_sentiment():

    games = Game.objects.all()

    for game in games:
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

def calc_sentiment_score(app):

    game = Game.objects.get(app_id=app)
    pos_labels = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1"]
    neg_labels = ["-0.1", "-0.2", "-0.3", "-0.4", "-0.5", "-0.6", "-0.7", "-0.8", "-0.9", "-1"]

    stats = GameStat.objects.get(app_id=game)

    pos_total = 0
    neg_total = 0
    neu_total = 0

    # Calculate each total for type of sentiment
    for sentiment in stats.sentiment:
        if sentiment["label"] in pos_labels:
            pos_total += sentiment["value"]
        if sentiment["label"] in neg_labels:
            neg_total += sentiment["value"]
        if sentiment["label"] == "0":
            neu_total += sentiment["value"]

    net_total = pos_total - neg_total
    sub_total = pos_total + neg_total + neu_total

    # Check is not zero so dont try to divide by zero
    if sub_total > 0:
        net_percent = round(net_total / sub_total, 3)
    else:
        net_percent = 0

    # Update the current sentiment of the game stats
    stats.current_sentiment_score = net_percent

    # Check if current sentiment is higher than highest alltime sentiment score
    if net_percent > stats.highest_sentiment_score:
        stats.highest_sentiment_score = round(net_percent, 3)
        stats.highest_sentiment_score_date = timezone.now()

    # Save Stats
    stats.save()



def calc_sentiment_score_all():

    games = Game.objects.all()
    pos_labels = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1"]
    neg_labels = ["-0.1", "-0.2", "-0.3", "-0.4", "-0.5", "-0.6", "-0.7", "-0.8", "-0.9", "-1"]

    for game in games:
        stats = GameStat.objects.get(app_id=game)

        pos_total = 0
        neg_total = 0
        neu_total = 0

        # Calculate each total for type of sentiment
        for sentiment in stats.sentiment:
            if sentiment["label"] in pos_labels:
                pos_total += sentiment["value"]
            if sentiment["label"] in neg_labels:
                neg_total += sentiment["value"]
            if sentiment["label"] == "0":
                neu_total += sentiment["value"]

        net_total = pos_total - neg_total
        sub_total = pos_total + neg_total + neu_total

        # Check is not zero so dont try to divide by zero
        if sub_total > 0:
            net_percent = round(net_total / sub_total, 3)
        else:
            net_percent = 0

        # Update the current sentiment of the game stats
        stats.current_sentiment_score = net_percent

        # Check if current sentiment is higher than highest alltime sentiment score
        if net_percent > stats.highest_sentiment_score:
            stats.highest_sentiment_score = round(net_percent, 3)
            stats.highest_sentiment_score_date = timezone.now()

        # Save Stats
        stats.save()
