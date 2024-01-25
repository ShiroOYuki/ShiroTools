from django.shortcuts import render
from downloadMusic import Downloader
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

def pymusicMainpage(request):
    return createRecents(request, "pymusic.html", "YT Music Downloader", "/pymusic", context={})

def downloadMusic(request):
    INSTALLPATH = "static/pymusic/download/"
    TEMPPATH = "static/pymusic/temp/"
    
    url = request.POST.get("url")
    timestamp = request.POST.get("timestamp")
    
    downloader = Downloader(installPath=INSTALLPATH, tempPath=TEMPPATH, batch=timestamp)
    downloader.check_folder_exist()
    downloader.check_is_list(url)
    
# if __name__ == "__main__":
#     INSTALLPATH = "static/pymusic/download/"
#     TEMPPATH = "static/pymusic/temp/"
    
#     url = "https://www.youtube.com/watch?v=t3kOeUsnocg"
#     timestamp = "test"
    
#     downloader = Downloader(installPath=INSTALLPATH, tempPath=TEMPPATH, batch=timestamp)
#     downloader.check_folder_exist()
#     downloader.check_is_list(url)