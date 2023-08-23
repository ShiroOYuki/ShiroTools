from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('test', views.test, name="test"),
    path('sleep', views.sleepPage, name="sleep"),
    path('nipponcolors', views.nipponcolors, name="nipponcolors"),
    path('emoji', views.emoji, name="emoji"),
    path('chatGPT', views.chatGPT, name="chatGPT"),
    path('icons', views.icons, name="icons")
]