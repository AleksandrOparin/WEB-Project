from django.http import HttpResponse
from django.shortcuts import render

from . import models

class Index:
    def index(request):
        context = {
            'questions': models.QUESTIONS,
            'popular_tags': models.TAGS,
            }
        return render(request, 'index.html', context=context)

class Question:
    def question(request, question_id: int):
        question_item = models.QUESTIONS[question_id]
        context = {'question': question_item}
        return render(request, 'question.html', context=context)

# def ask(request):
#     return render(request, 'ask.html')

# def login(request):
#     return render(request, 'login.html')
