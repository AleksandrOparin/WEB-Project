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
        questions_with_tag = list(filter(lambda question: tag_name in question['tags'], models.QUESTIONS))
        context = {
            'user_info': models.USER,
            'tag_name': tag_name,
            'questions': questions_with_tag,
            'popular_tags': models.TAGS,
            'best_users': models.BEST_USERS
        }
        return render(request, 'tag.html', context=context)

class Login:
    def login(request):
        context = {
            'popular_tags': models.TAGS,
            'best_users': models.BEST_USERS
        }
        return render(request, 'login.html', context=context)

class Settings:
    def settings(request):
        context = {
            'user_info': models.USER,
            'popular_tags': models.TAGS,
            'best_users': models.BEST_USERS
        }
        return render(request, 'settings.html', context=context)

class Signup:
    def signup(request):
        context = {
            'popular_tags': models.TAGS,
            'best_users': models.BEST_USERS
        }
        return render(request, 'signup.html', context=context)

class HotQuestions:
    def hot_questions(request):
        hot_questions = list(filter(lambda question: question['like_count'] >= 50, models.QUESTIONS))
        context = {
            'user_info': models.USER,
            'questions': hot_questions,
            'popular_tags': models.TAGS,
            'best_users': models.BEST_USERS
        }
        return render(request, 'hot_questions.html', context=context)
