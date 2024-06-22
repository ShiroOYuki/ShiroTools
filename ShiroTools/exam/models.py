from django.db import models
import uuid

# Create your models here.

class Bank(models.Model):
    id = models.UUIDField(               # PK: bank_id
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )    
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name



class Question(models.Model):
    SINGLE = "SI"
    MULTIPLE = "MU"
    SHORT_ANSWER = "SH"
    
    TYPE_CHOICES = [
        (SINGLE, "single_choice"),
        (MULTIPLE, "multiple_choice"),
        (SHORT_ANSWER, "short_answer"),
    ]
    
    id = models.UUIDField(               # PK: question_id
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    bank_id = models.ForeignKey(         # FK: bank_id
        to = Bank,
        to_field = "id",
        on_delete=models.DO_NOTHING
    )
    type = models.CharField(
        max_length=2,
        choices = TYPE_CHOICES,
        default = SINGLE
    )
    question_text = models.CharField(max_length=200)
    question_number = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.question_text



class Image(models.Model):
    id = models.UUIDField(               # PK: image_id
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )      
    question_id = models.ForeignKey(     # FK: question_id
        to = Question,
        to_field = "id",
        on_delete = models.DO_NOTHING
    )
    image_path = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return "exam.Images"
    
    
    
class Option(models.Model):
    id = models.UUIDField(               # PK: option_id
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    question_id = models.ForeignKey(     # FK: question_id
        to = Question,
        to_field = "id",
        on_delete = models.DO_NOTHING
    )
    option_text = models.CharField(max_length=200, blank=True, null=True)
    option_index = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.option_text if self.option_text != "" or self.option_text != None else "Null"
    
    

class Answer(models.Model):
    id = models.UUIDField(               # PK: answer_id
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    question_id = models.ForeignKey(     # FK: question_id
        to = Question,
        to_field = "id",
        on_delete = models.DO_NOTHING
    )
    answer_text = models.CharField(max_length=50, blank=True, null=True)
    answer_index = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.answer_text if self.answer_text is not None else "Null"