from django.shortcuts import render
from django.core.paginator import Paginator

from home.models import (
    Game,
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
