from django.shortcuts import render
from django.db.models import Max
from home.models import Game, GameStat, PlayerCount

from django.core.paginator import Paginator

# Create your views here.

def Charts(request):
    games = Game.objects.all()

    games_sorted = []
    games_subject = "player_count"
    games_type = "current"

    if request.method == 'POST':
        print("POST")
        if(request.POST["subject"] == "player-count"):

            print(request.POST["subject"])

            # Get List of current most played games
            for game in games:

                current = {}
                player_count = PlayerCount.objects.filter(app_id=game).last()

                current["app"] = game
                current["player_count"] = player_count.player_count
                games_sorted.append(current)

            games_sorted = sorted(games_sorted, key=lambda x:x['player_count'], reverse=True)
            games_subject = "player_count"
            games_type = "current"
            
        elif (request.POST["subject"] == "reviews"):

            print(request.POST["subject"])

            # Get List of current most played games
            for game in games:

                current = {}
                review_percentage = GameStat.objects.get(app_id=game).current_review_score

                current["app"] = game
                current["reviews_percentage"] = review_percentage
                games_sorted.append(current)

            games_sorted = sorted(games_sorted, key=lambda x:x['reviews_percentage'], reverse=True)
            games_subject = "reviews"
            games_type = "current"

    else:
        print("ELSE")
        # Get List of current most played games
        for game in games:

            current = {}
            player_count = PlayerCount.objects.filter(app_id=game).last()

            current["app"] = game
            current["player_count"] = player_count.player_count
            games_sorted.append(current)

        games_sorted = sorted(games_sorted, key=lambda x:x['player_count'], reverse=True)

    paginator = Paginator(games_sorted, 10)
    page_number = request.GET.get('page')
    paginated_games = paginator.get_page(page_number)
    sub_num = 10*(paginated_games.number-1)

    context = {"games": paginated_games, "games_subject": games_subject, "games_type": games_type, "sub_num": sub_num}

    return render(request, 'charts/charts.html', context)