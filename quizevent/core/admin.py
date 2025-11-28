from django.contrib import admin
from .models import Quiz, Question, Answer, Event, UserSubmission, UserAnswer

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Event)
admin.site.register(UserSubmission)
admin.site.register(UserAnswer)
