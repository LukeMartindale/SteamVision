from home.models import Game, GameStat, Developer

def get_developers(id):
    game = Game.objects.get(app_id=id)
    
    for developer in game.developer:

        # Check if this developer already exists
        if not Developer.objects.filter(name=developer).exists():
            dev = Developer()
            dev.name = developer
            dev_games = []
        else:
            dev = Developer.objects.get(name=developer)
            dev_games = dev.games

        # Check if game already in dev_games
        # Check if dev_games is empty
        if not dev_games:
            dev_games.append({"app_id": game.app_id, "name": game.name, "role": "developer"})
        else:
            for dg in dev_games:
                if game.app_id not in dg.values():
                    dev_games.append({"app_id": game.app_id, "name": game.name, "role": "developer"})

        dev.games = dev_games
        dev.save()

def get_developers_all():
    games = Game.objects.all()

    for game in games:
        for developer in game.developer:

            # Check if this developer already exists
            if not Developer.objects.filter(name=developer).exists():
                dev = Developer()
                dev.name = developer
                dev_games = []
            else:
                dev = Developer.objects.get(name=developer)
                dev_games = dev.games

            # Check if game already in dev_games
            # Check if dev_games is empty
            if not dev_games:
                dev_games.append({"app_id": game.app_id, "name": game.name, "role": "developer"})
            else:
                for dg in dev_games:
                    if game.app_id not in dg.values():
                        dev_games.append({"app_id": game.app_id, "name": game.name, "role": "developer"})

            dev.games = dev_games
            dev.save()

def order_developer_games_all():
    developers = Developer.objects.all()
    stats = GameStat.objects.all().order_by("-current_review_score")

    for developer in developers:
        ordered_games = []
        for stat in stats:
            for dev_game in developer.games:
                if stat.app_id.app_id == dev_game["app_id"]:
                    ordered_games.append(dev_game)

        developer.games = ordered_games
        developer.save()

def developer_common_genres_find_all():
    developers = Developer.objects.all()
    
    for developer in developers:

        print(developer)

        ids = []
        for app in developer.games:
            ids.append(app["app_id"])

        games = Game.objects.filter(app_id__in=ids)

        genres = {}

        for game in games:
            print(game)
            for genre in game.genres:
                genres[genre] = genres.get(genre, 0) + 1

        if len(genres) > 5:
            common = sorted(genres, key=genres.get, reverse=True)[:5]
        else:
            common = sorted(genres, key=genres.get, reverse=True)[:len(genres)]

        developer.common_genres = common
        developer.save()
