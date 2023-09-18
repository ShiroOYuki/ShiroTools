from django.shortcuts import render, HttpResponse
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
            "questions": questions
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

def pair_ans(request, qid="test"):
    questions, answer = read_question(qid)
    if request.method == "POST":
        user_ans = request.POST.getlist("ans[]")
        if answer:
            correct = 0
            for i in range(len(answer)):
                if answer[i] == user_ans[i]:
                    correct += 1
            print(correct)
            print(answer)
        print(user_ans)
    
    resp = HttpResponse(request)
    resp.set_cookie("user_ans", json.dumps(user_ans))
    return resp

def ans(request, qid="test"):
    if request.COOKIES.get("user_ans"):
        questions, answer = read_question(qid)
        user_ans = json.loads(request.COOKIES["user_ans"])
        data = []
        tot = len(questions)
        correct = 0
        for i in range(len(questions)):
            data.append({
                "question": questions[i],
                "answer": answer[i],
                "user_ans": user_ans[i]
            })
            if answer[i] == user_ans[i]:
                correct += 1
        return render(
            request,
            "answer.html",
            context = {
                "data": data,
                "score": str(correct) + "/" + str(tot)
            }
        )