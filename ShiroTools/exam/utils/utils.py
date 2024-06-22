from django.db.models import QuerySet
from exam.utils.ModelManager import ModelManager

def check_short_answer(user_ans:str, true_ans:str):
    return user_ans == true_ans

def check_single_choice(user_ans:str, true_ans:str):
    return user_ans == true_ans

def check_multiple_choice(user_ans:str, true_ans:str):
    return "".join(sorted(user_ans.split(","))) == "".join(sorted(true_ans)), sorted(user_ans.split(","))

def load_bank(bank_id: str = "52dd48f50328411aafca44b83c5bf907"):
    questions = ModelManager.read_questions(bank_id)
    res = []
    for question in questions:
        question_data = dict()
        if question[1] == "SI": question_data["type"] = "single_choice"
        elif question[1] == "MU": question_data["type"] = "multiple_choice"
        elif question[1] == "SH": question_data["type"] = "short_answer"
        question_data["question"] = question[2]
        
        options = ModelManager.read_options(question[0])
        if question[1] == "SI": options = [option[0] for option in options]
        elif question[1] == "MU": options = [option[0] for option in options]
        elif question[1] == "SH": options = []
        question_data["options"] = options
        
        answer = ModelManager.read_answer(question[0])
        if question[1] == "SI": question_data["answer"] = str(answer[0][1])
        elif question[1] == "MU": question_data["answer"] = [str(ans[1]) for ans in answer]
        elif question[1] == "SH": question_data["answer"] = answer[0][0 ]
        res.append(question_data)
    return res

