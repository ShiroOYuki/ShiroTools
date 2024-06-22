from exam.models import Bank, Question, Option, Answer, Image

class ModelManager:
    @classmethod
    def read_bank(cls, bank_id: str):
        bank = Bank.objects.filter(id=bank_id).values_list("name", "description")
        return bank
    
    @classmethod
    def read_questions(cls, bank_id: str):
        questions = Question.objects.filter(bank_id=bank_id).order_by("question_number").values_list("id", "type", "question_text", "question_number")
        return questions
    
    @classmethod
    def read_options(cls, question_id: str):
        options = Option.objects.filter(question_id=question_id).order_by("option_index").values_list("option_text", "option_index")
        return options
    
    @classmethod
    def read_answer(cls, question_id: str):
        answers = Answer.objects.filter(question_id=question_id).order_by("answer_index").values_list("answer_text", "answer_index")
        return answers