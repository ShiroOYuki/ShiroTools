import json
from django.shortcuts import render

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