from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeveloperList, name='developer-list'),
]
