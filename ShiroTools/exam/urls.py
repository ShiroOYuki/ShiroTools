from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('question/<str:qid>', views.question, name="exam"),
    path('question/<str:qid>/ans', views.ans, name="ans")
]