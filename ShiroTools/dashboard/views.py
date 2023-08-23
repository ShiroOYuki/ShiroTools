from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def createRecents(request, resp_url, name, url, context={}):
    if request.COOKIES.get("history"):
        hist = json.loads(request.COOKIES["history"])
    else:
        hist = []
    if name != "Dashboard" and (len(hist) == 0 or hist[0][0]) != name:
        hist.insert(0, [name, url])
    if len(hist) > 20:
        hist = hist[:20]
    context["history"] = hist
    resp = render(
        request, 
        resp_url,
        context=context
    )
    resp.set_cookie("history", json.dumps(hist))
    return resp

def index(request):
    with open("static/dashboard/update.txt", "r", encoding="utf-8") as f:
        logs = [line.strip("\n") for line in f.readlines()]
        context = {
            "logs": logs
        }
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
