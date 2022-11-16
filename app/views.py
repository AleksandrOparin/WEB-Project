from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render

from . import models

def index(request):
    questions = models.Question.objects.new()
    popular_tags = models.Tag.objects.popular_tags()
    best_users = models.Profile.objects.top_profiles()

    page_questions = paginate(questions, request, 20)

    context = {
        # 'user_info': models.USER,
        'questions': page_questions,
        'popular_tags': popular_tags,
        'best_users': best_users,
    }

    return render(request, 'index.html', context=context)


def question(request, question_id: int):
    question = None
    try:
        question = models.Question.objects.get(id = question_id)
    except models.Question.DoesNotExist:
        return render(request, 'errors/404.html')
    
    answers = models.Answer.objects.ordered_answers(question_id)
    popular_tags = models.Tag.objects.popular_tags()
    best_users = models.Profile.objects.top_profiles()

    question_page_answers = paginate(answers, request, 20)

    context = {
        # 'user_info': models.USER,
        'question': question,
        'answers': question_page_answers,
        'popular_tags': popular_tags,
        'best_users': best_users,
    }

    return render(request, 'question.html', context=context)


def ask(request):
    popular_tags = models.Tag.objects.popular_tags()
    best_users = models.Profile.objects.top_profiles()

    context = {
        # 'user_info': models.USER,
        'popular_tags': popular_tags,
        'best_users': best_users,
    }

    return render(request, 'ask.html', context=context)


def tag(request, tag_id: int):
    questions_with_tag = None
    try:
        questions_with_tag = models.Question.objects.tag(tag_id)
    except models.Question.DoesNotExist:
        return render(request, 'errors/404.html')

    tag_name = models.Tag.objects.get(id = tag_id).name
    popular_tags = models.Tag.objects.popular_tags()
    best_users = models.Profile.objects.top_profiles()

    page_questions_with_tag = paginate(questions_with_tag, request, 20)

    context = {
        # 'user_info': models.USER,
        'tag_name': tag_name,
        'questions': page_questions_with_tag,
        'popular_tags': popular_tags,
        'best_users': best_users,
    }

    return render(request, 'tag.html', context=context)


def login(request):
    popular_tags = models.Tag.objects.popular_tags()
    best_users = models.Profile.objects.top_profiles()

    context = {
        'popular_tags': popular_tags,
        'best_users': best_users,
    }

    return render(request, 'login.html', context=context)


def settings(request):
    popular_tags = models.Tag.objects.popular_tags()
    best_users = models.Profile.objects.top_profiles()

    context = {
        #'user_info': models.USER,
        'popular_tags': popular_tags,
        'best_users': best_users,
    }

    return render(request, 'settings.html', context=context)


def signup(request):
    popular_tags = models.Tag.objects.popular_tags()
    best_users = models.Profile.objects.top_profiles()

    context = {
        'popular_tags': popular_tags,
        'best_users': best_users,
    }

    return render(request, 'signup.html', context=context)


def hot_questions(request):
    hot_questions = None
    try:
        hot_questions = models.Question.objects.top()
    except models.Question.DoesNotExist:
        return render(request, 'errors/404.html')

    popular_tags = models.Tag.objects.popular_tags()
    best_users = models.Profile.objects.top_profiles()

    page_hot_questions = paginate(hot_questions, request, 20)

    context = {
        # 'user_info': models.USER,
        'questions': page_hot_questions,
        'popular_tags': popular_tags,
        'best_users': best_users,
    }

    return render(request, 'hot_questions.html', context=context)


def paginate(objects_list, request, items_per_page=10):
    paginator = Paginator(objects_list, items_per_page)
    page_number = request.GET.get('page')
    page_items = paginator.get_page(page_number)

    return page_items
