from django.shortcuts import render
from django.core.paginator import Paginator

from home.models import (
    Developer
)

# Create your views here.
def DeveloperList(request):

    developer = Developer.objects.all().order_by('name')
    print(request.GET.getlist('test'))

    if(request.GET.getlist('test')):
        print("test not empty")

    print(developer[0].pk)

    return render(request, 'developer/developer-list.html')
