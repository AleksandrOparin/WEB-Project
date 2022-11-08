from django.http import HttpResponse
from django.shortcuts import render

from . import models

class Index:
    def index(request):
        context = {
            'user_info': models.USER,
            'questions': models.QUESTIONS,
            'popular_tags': models.TAGS,
            'best_users': models.BEST_USERS,
            }
        return render(request, 'index.html', context=context)

class Question:
    def question(request, question_id: int):
        question_item = models.QUESTIONS[question_id]
        context = {
            'question': question_item,
            'popular_tags': models.TAGS,
            'best_users': models.BEST_USERS,
        }
        return render(request, 'question.html', context=context)

class Ask:
    def ask(request):
        context = {}
        return render(request, 'ask.html', context=context)

# def ask(request):
#     return render(request, 'ask.html')

# def login(request):
#     return render(request, 'login.html')
