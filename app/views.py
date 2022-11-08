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
            'user_info': models.USER,
            'question': question_item,
            'popular_tags': models.TAGS,
            'best_users': models.BEST_USERS,
        }
        return render(request, 'question.html', context=context)

class Ask:
    def ask(request):
        context = {
            'user_info': models.USER,
            'popular_tags': models.TAGS,
            'best_users': models.BEST_USERS
        }
        return render(request, 'ask.html', context=context)

class Tag:
    def tag(request, tag_name: str):
        # tag_item = models.QUESTIONS[]
        # next(item for item in dicts if item["name"] == "Pam")
        # next(question for question in QUESTIONS if question['tags'])
        # list(filter(lambda person: person['name'] == 'Pam', people))
        questions_with_tag = list(filter(lambda question: tag_name in question['tags'], models.QUESTIONS))
        context = {
            'user_info': models.USER,
            'tag': tag_name,
            'questions': questions_with_tag,
            'popular_tags': models.TAGS,
            'best_users': models.BEST_USERS
        }
        return render(request, 'tag.html', context=context)

# def login(request):
#     return render(request, 'login.html')
