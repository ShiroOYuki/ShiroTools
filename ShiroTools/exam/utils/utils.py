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
        options = ModelManager.read_options(question[0])
        answer = ModelManager.read_answer(question[0])
        
        question_data = {
            "type": type_factory(question),
            "question": question[2],
            "options": option_factory(question, options),
            "answer": answer_factory(question, answer)
        }
        
        res.append(question_data)
        
    return res

def type_factory(question: QuerySet):
    if question[1] == "SI": return "single_choice"
    elif question[1] == "MU": return "multiple_choice"
    elif question[1] == "SH": return "short_answer"
    
def option_factory(question: QuerySet, options: QuerySet):
    if question[1] == "SI": return [option[0] for option in options]
    elif question[1] == "MU": return [option[0] for option in options]
    elif question[1] == "SH": return []
    
def answer_factory(question: QuerySet, answer: QuerySet):
    if question[1] == "SI": return str(answer[0][1])
    elif question[1] == "MU": return [str(ans[1]) for ans in answer]
    elif question[1] == "SH": return answer[0][0]

