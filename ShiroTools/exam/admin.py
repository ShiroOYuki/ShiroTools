from django.contrib import admin
from exam.models import Bank, Question, Image, Option, Answer

# Register your models here.

admin.site.register(Bank)
admin.site.register(Question)
admin.site.register(Image)
admin.site.register(Option)
admin.site.register(Answer)