from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.line_stickers_mainpage, name="line_stickers"),
    path('get_stickers', views.get_stickers, name="get_stickers")
]