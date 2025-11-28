from django.db import models
from django.utils import timezone


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

QUESTION_TYPES = [
("single", "Single Choice"),
# could add 'multiple' in future
]


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default='single')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.quiz.title} - Q{self.id}: {self.text[:50]}"

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.question.id} - {self.text[:40]}"

class UserSubmission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200)
    score = models.FloatField()
    submitted_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.user_name} - {self.quiz.title} - {self.score}"

class UserAnswer(models.Model):
    submission = models.ForeignKey(UserSubmission, on_delete=models.CASCADE, related_name='user_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=500)
    is_correct = models.BooleanField()


    def __str__(self):
        return f"{self.submission.user_name} - Q{self.question.id} - {self.is_correct}"

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return f"{self.title} on {self.date}"