from django.shortcuts import render

# Create your views here.
def compare(request):

    # if request.GET.get("games", False):
    #     games = request.GET.get('games', False).split(",")
    #     print(games)

    return render(request, 'compare/compare.html')
