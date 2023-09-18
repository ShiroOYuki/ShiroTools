from django.shortcuts import render
import json
import os

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
    return createRecents(request, "exam.html", "Shiro's Exam", "/exam")

def question(request, qid="test"):
    questions, answer = read_question(qid)
    return render(
        request,
        "question.html",
        context={
            "questions": questions,
            "answer": answer
        }
    )

def read_question(qid):
    path = f"static/exam/questions/{qid}.json"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as jfile:
            jdata = json.load(jfile)
            questions = jdata["questions"]
            answers = jdata["answers"]
            return questions, answers
    return None, None

def ans(request, qid="test"):
    return render(request, "exam.html")