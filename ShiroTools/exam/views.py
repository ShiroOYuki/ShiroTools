from django.shortcuts import render, HttpResponse, redirect
from django.http.response import JsonResponse
from django.http.request import HttpRequest
import json
from libs.utils import createRecents

from exam.utils import utils


QuestionsData = list[dict[
    "type": str,
    "question": str,
    "option": list[str],
    "answer": str | list[str]
]]

# ---------------------- exam homepage ----------------------

def index(request):
    bank_data = utils.load_bank()
    print(bank_data)
    # return JsonResponse(bank_data, safe=False)
    return createRecents(request, "exam.html", "Shiro's Exam", "/exam")

# ---------------------- question page ----------------------

def question(request, qid="52dd48f50328411aafca44b83c5bf907"):
    questions = utils.load_bank(qid)
    return render(
        request,
        "question.html",
        context={
            "questions": questions,
        }
    )

def submit_answers(request, qid="52dd48f50328411aafca44b83c5bf907"):
    if request.method == "POST":
        http_res = request.POST.getlist("ans[]")
        
        resp = HttpResponse(request)
        resp.set_cookie("user_ans", json.dumps(http_res))
        return resp

# ---------------------- answer page ----------------------

def check_answers(request, qid="52dd48f50328411aafca44b83c5bf907"):
    if request.COOKIES.get("user_ans"):
        http_res = json.loads(request.COOKIES.get("user_ans"))
        questions_res = utils.load_bank(qid)
        answer_res = [q["answer"] for q in questions_res]
        
        total = len(questions_res)
        ret_ans = [False]*total
        
        for i, ans in enumerate(http_res):
            if questions_res[i]["type"] == "short_answer":
                ret_ans[i] = utils.check_short_answer(ans, answer_res[i])
            elif questions_res[i]["type"] == "single_choice":
                ret_ans[i] = utils.check_single_choice(ans, answer_res[i])
            elif questions_res[i]["type"] == "multiple_choice":
                ret_ans[i], http_res[i] = utils.check_multiple_choice(ans, answer_res[i])
        
        goods = len(list(filter(lambda x: x, ret_ans)))
        score = [goods, total, round(goods/total*100, 1)]
        
        return render(
            request,
            "answer.html",
            context = {
                "questions": questions_res,
                "user_ans": http_res,
                "true_ans": answer_res,
                "score": score
            }
        )

# ---------------------- create page ----------------------

def creating_page(request: HttpRequest):
    return render(request, "create.html")
