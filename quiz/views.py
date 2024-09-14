# quiz/views.py
from django.shortcuts import render
from .models import Question, Result

def start_quiz(request):
    return render(request, 'quiz/start.html')

def quiz_question(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'quiz/question.html', {'question': question})

def quiz_result(request, result_id):
    result = Result.objects.get(id=result_id)
    return render(request, 'quiz/result.html', {'result': result})
