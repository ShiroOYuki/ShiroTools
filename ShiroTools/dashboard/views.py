from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "dashboard.html")

def test(request):
    return render(request, "template.html")

def sleepPage(request):
    return render(request, "sleep.html")