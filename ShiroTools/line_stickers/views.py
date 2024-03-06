from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .download_stickers import Sticker
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

def line_stickers_mainpage(request):
    return createRecents(request, "line_stickers.html", "Line Stickers", "/line_stickers", context={})

def get_stickers(request):
    if request.method == "POST":
        url = request.POST.get("name")
        res = Sticker.download(url)
        if res:
            return JsonResponse({"title": res[0], "author": res[1], "names": res[2], "zip": res[3]})
    if request.method == "GET":
        pct = Sticker.get_progress_bar()
        print(pct)
        return JsonResponse(round(pct), safe=False)
        
    return JsonResponse({"msg": "Error"})