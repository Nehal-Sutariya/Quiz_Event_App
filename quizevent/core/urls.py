from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='home'),

     path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),

    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quiz/<int:id>/', views.quiz_attempt, name='quiz_attempt'),
    path('events/', views.events, name='events'),
    path('events/', views.event_list, name='event_list'),
]
