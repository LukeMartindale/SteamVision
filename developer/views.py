from django.shortcuts import render
from django.core.paginator import Paginator

from home.models import (
    Game,
    Developer
)

# Create your views here.
def DeveloperList(request):

    developers = Developer.objects.all().order_by('name')
    games = Game.objects.all()

    # print(request.GET.getlist('test'))
    # if(request.GET.getlist('test')):
    #     print("test not empty")
    # print(developer[0].pk)
    
    context = {"developers": developers, "games": games}

    return render(request, 'developer/developer-list.html', context)
