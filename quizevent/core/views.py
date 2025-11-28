from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Answer, UserSubmission, UserAnswer, Event
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'core/home.html')


def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'core/quiz_list.html', {'quizzes': quizzes})




def quiz_attempt(request, id):
    quiz = get_object_or_404(Quiz, id=id)
    questions = Question.objects.filter(quiz=quiz)

    if request.method == "POST":
        name = request.POST.get('name')
        score = 0

        submission = UserSubmission.objects.create(
            quiz=quiz,
            user_name=name,
            score=0
        )

        for q in questions:
            selected_answer_id = request.POST.get(str(q.id))

            # SAFETY CHECK
            if not selected_answer_id:
                continue

            try:
                selected_answer = Answer.objects.get(id=selected_answer_id)
            except Answer.DoesNotExist:
                continue

            if selected_answer.is_correct:
                score += 1

            UserAnswer.objects.create(
                submission=submission,
                question=q,
                answer=selected_answer.text,
                is_correct=selected_answer.is_correct
            )

        submission.score = score
        submission.save()

        return render(request, 'core/result.html', {
            'score': score,
            'total': questions.count()
        })

    return render(request, 'core/quiz_attempt.html', {
        'quiz': quiz,
        'questions': questions
    })


def events(request):
    events = Event.objects.all()
    return render(request, 'core/events.html', {'events': events})
    
# LOGIN
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid username or password'})

    return render(request, 'core/login.html')


# REGISTER
def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'core/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'core/register.html', {'error': 'Username already exists'})

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'core/register.html')


# LOGOUT
def logout_user(request):
    logout(request)
    return redirect('login')


# HOME
@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def event_list(request):
    events = Event.objects.all().order_by('date')

    return render(request, 'core/events.html', {'events': events})
