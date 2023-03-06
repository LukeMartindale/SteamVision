from django.shortcuts import render
from django.core.paginator import Paginator
from functools import reduce
from operator import or_
from django.db.models import Q

from home.models import (
    Game,
    Review,
    Developer
)

# Create your views here.
def DeveloperList(request):

    games = Game.objects.all()
    pass_search = False

    if request.method == 'POST':
        developers = Developer.objects.filter(name__icontains=request.POST["search"]).order_by('name')
        pass_search = True
        search_text = request.POST["search"]
    elif request.GET.get('search_text', False):
        developers = Developer.objects.filter(name__icontains=request.GET.get('search_text', False)).order_by('name')
        pass_search = True
        search_text = request.GET.get('search_text', False) 
    else:
        search_text = ""
        developers = Developer.objects.all().order_by('name')

    paginator = Paginator(developers, 9)
    page_number = request.GET.get('page')
    paginated_developers = paginator.get_page(page_number)
    
    context = {"developers": paginated_developers, "games": games, "pass_search": pass_search, "text_search": search_text}

    return render(request, 'developer/developer-list.html', context)

def DeveloperDetail(request, pk):

    developer = Developer.objects.get(id=pk)

    dev_games = []
    dev_games_id = [646270]
    for dev_game in developer.games:
        game = Game.objects.get(app_id=dev_game["app_id"])
        dev_games.append(game)
        dev_games_id.append(dev_game["app_id"])

    filters = [developer.name, "developer", "dev"]
    # reviews = Review.objects.all()

    # for filter in filters:
    reviews = Review.objects.filter(reduce(or_, [Q(review_text__icontains=developer.name) for q in filters]), app_id__app_id__in=dev_games_id).order_by('-time_created')

    print(reviews)

    # for review in reviews:
    #     print(review.review_text)

    if(reviews):

        if(len(reviews) > 15):
            print("Not Yet Implemented")
        else:
            print("Not Yet Implemented")

        print(reviews)
        print(len(reviews))

        print(reviews[0].time_created)


    context = {"developer": developer, "games": dev_games}

    return render(request, 'developer/developer-detail.html', context)
