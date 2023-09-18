from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('question/<str:qid>', views.question, name="exam"),
    path('question/<str:qid>/submit', views.pair_ans, name="pair_ans"),
    path('question/<str:qid>/answer', views.ans, name="pair_ans")
]