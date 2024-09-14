# quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_quiz, name='start_quiz'),
    path('question/<int:question_id>/', views.quiz_question, name='quiz_question'),
    path('result/<int:result_id>/', views.quiz_result, name='quiz_result'),
]
