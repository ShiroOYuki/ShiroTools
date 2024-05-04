from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .download_stickers import Sticker
import json
from libs.utils import createRecents

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