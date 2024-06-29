from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('question/<str:qid>', views.question, name="exam"),
    path('question/<str:qid>/submit', views.submit_answers, name="submit_answers"),
    path('question/<str:qid>/answer', views.check_answers, name="check_answers"),
    path('create', views.creating_page, name="creating")
]