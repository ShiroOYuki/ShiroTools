from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .download_stickers import Sticker

# Create your views here.

def line_stickers_mainpage(request):
    return render(
        request, 
        "line_stickers.html", 
        context = {"stickers": []}
    )

def get_stickers(request):
    if request.method == "POST":
        url = request.POST.get("name")
        stickers = Sticker()
        res = stickers.download(url)
        if res:
            return JsonResponse({"title": res[0], "author": res[1], "names": res[2], "zip": res[3]})
    return JsonResponse({"msg": "Error"})