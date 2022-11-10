from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.core.paginator import Paginator
from django.shortcuts import render

from . import models


# class Index:
def index(request):
    page_questions = paginate(models.QUESTIONS, request, 4)
    
    context = {
        'user_info': models.USER,
        'questions': page_questions,
        'popular_tags': models.TAGS,
        'best_users': models.BEST_USERS,
        }
    return render(request, 'index.html', context=context)

# class Question:
def question(request, question_id: int):
    question_item = None
    if any(question['id'] == question_id for question in models.QUESTIONS):
        question_item = models.QUESTIONS[question_id]
    else:
        raise Http404

    question_page_answers = paginate(question_item['answers'], request, 4)

    context = {
        'user_info': models.USER,
        'question': question_item,
        'answers': question_page_answers,
        'popular_tags': models.TAGS,
        'best_users': models.BEST_USERS,
    }
    return render(request, 'question.html', context=context)

# class Ask:
def ask(request):
    context = {
        'user_info': models.USER,
        'popular_tags': models.TAGS,
        'best_users': models.BEST_USERS
    }
    return render(request, 'ask.html', context=context)

# class Tag:
def tag(request, tag_name: str):
    questions_with_tag = list(filter(lambda question: tag_name in question['tags'], models.QUESTIONS))
    if not any(questions_with_tag):
        raise Http404

    page_questions_with_tag = paginate(questions_with_tag, request, 4)

    context = {
        'user_info': models.USER,
        'tag_name': tag_name,
        'questions': page_questions_with_tag,
        'popular_tags': models.TAGS,
        'best_users': models.BEST_USERS
    }
    return render(request, 'tag.html', context=context)

# class Login:
def login(request):
    context = {
        'popular_tags': models.TAGS,
        'best_users': models.BEST_USERS
    }
    return render(request, 'login.html', context=context)

# class Settings:
def settings(request):
    context = {
        'user_info': models.USER,
        'popular_tags': models.TAGS,
        'best_users': models.BEST_USERS
    }
    return render(request, 'settings.html', context=context)

# class Signup:
def signup(request):
    context = {
        'popular_tags': models.TAGS,
        'best_users': models.BEST_USERS
    }
    return render(request, 'signup.html', context=context)

# class HotQuestions:
def hot_questions(request):
    hot_questions = list(filter(lambda question: question['like_count'] >= 50, models.QUESTIONS))
    if not any(hot_questions):
        raise Http404

    context = {
        'user_info': models.USER,
        'questions': hot_questions,
        'popular_tags': models.TAGS,
        'best_users': models.BEST_USERS
    }
    return render(request, 'hot_questions.html', context=context)

def error_404(request, exception):
    data = {}
    return render(request, 'errors/404.html', data)

def paginate(objects_list, request, items_per_page=10):
    paginator = Paginator(objects_list, items_per_page)
    page_number = request.GET.get('page')
    page_items = paginator.get_page(page_number)

    return page_items