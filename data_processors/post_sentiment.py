from home.models import Game, GameStat

def post_sentiment(app):

    game = Game.objects.get(app_id=app)
    print(game)

    return True
