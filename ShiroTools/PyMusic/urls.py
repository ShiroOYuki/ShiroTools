from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.pymusicMainpage, name="pymusic"),
    path('download', views.downloadMusic, name="downloadMusic")
]