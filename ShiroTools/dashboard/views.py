from django.shortcuts import render, redirect
from libs.utils import createRecents

def index(request):
    context = {}
    with open("static/dashboard/update.txt", "r", encoding="utf-8") as f:
        logs = [line.strip("\n") for line in f.readlines()]
        context = {
            "logs": logs
        }
    with open("static/dashboard/announcement.txt", "r", encoding="utf-8") as f:
        announcement = [line.strip("\n") for line in f.readlines()]
        context["announcement"] = announcement
    resp = createRecents(request, "dashboard.html", "Dashboard", "/", context)
    return resp

def test(request):
    return render(request, "template.html")

def sleepPage(request):
    resp = createRecents(request, "sleep.html", "Sleep", "/sleep")
    return resp

def nipponcolors(request):
    resp = createRecents(request, "nipponcolors.html", "NipponColors", "/nipponcolors")
    return resp

def emoji(request):
    resp = createRecents(request, "emoji.html", "Emoji", "/emoji")
    return resp

def chatGPT(request):
    resp = createRecents(request, "chatGPT.html", "ChatGPT", "/chatGPT")
    return resp

def icons(request):
    resp = createRecents(request, "icons.html", "Icons", "/icons")
    return resp
