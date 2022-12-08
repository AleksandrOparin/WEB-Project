from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.contrib import auth
from django.urls import reverse
from django.forms import model_to_dict

from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from . import models
from . import forms


def index(request):
    questions = models.Question.objects.new()
    popular_tags = models.Tag.objects.popular_tags()
    best_users = models.Profile.objects.top_profiles()

    page_questions = paginate(questions, request, 20)

    context = {
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
        'question': question,
        'answers': question_page_answers,
        'popular_tags': popular_tags,
        'best_users': best_users,
    }

    return render(request, 'question.html', context=context)


@login_required(login_url='login', redirect_field_name='continue')
def ask(request):
    popular_tags = models.Tag.objects.popular_tags()
    best_users = models.Profile.objects.top_profiles()

    if request.method == 'GET':
        ask_form = forms.AskForm()

    if request.method == 'POST':
        ask_form = forms.AskForm(request.POST)

        if ask_form.is_valid():
            new_question = models.Question(title = ask_form.cleaned_data['title'], text = ask_form.cleaned_data['text'], author_id = request.user.profile.id)
            new_question.save()

            add_tags_to_question(ask_form.cleaned_data['tags'], new_question)

            print("Before redirect")
            return redirect(reverse("question", args = [new_question.id]))

        else:
            ask_form.add_error(field=None,error="Wrong data!")

    context = {
        'form': ask_form,
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
        'tag_name': tag_name,
        'questions': page_questions_with_tag,
        'popular_tags': popular_tags,
        'best_users': best_users,
    }

    return render(request, 'tag.html', context=context)


def login(request):
    popular_tags = models.Tag.objects.popular_tags()
    best_users = models.Profile.objects.top_profiles()

    if request.method == 'GET':
        user_form = forms.LoginForm()

    if request.method == 'POST':
        user_form = forms.LoginForm(request.POST)

        if user_form.is_valid():
            user = auth.authenticate(request=request, **user_form.cleaned_data)

            if user:
                auth.login(request=request, user=user)
                return redirect(reverse('index'))
            else:
                user_form.add_error(field=None, error="Wrong username or password!")

    context = {
        'form': user_form,
        'popular_tags': popular_tags,
        'best_users': best_users,
    }

    return render(request, 'login.html', context=context)


@login_required(login_url='login', redirect_field_name='continue')
def settings(request):
    popular_tags = models.Tag.objects.popular_tags()
    best_users = models.Profile.objects.top_profiles()

    if request.method == 'GET':
        dict_model_fields = model_to_dict(request.user)
        user_form = forms.SettingsForm(initial=dict_model_fields)

    if request.method == 'POST':
        user_form = forms.SettingsForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
        return redirect(reverse('settings'))

    context = {
        'form': user_form,
        'popular_tags': popular_tags,
        'best_users': best_users,
    }
    return render(request, 'settings.html', context=context)


def signup(request):
    popular_tags = models.Tag.objects.popular_tags()
    best_users = models.Profile.objects.top_profiles()

    if request.method == "GET":
        user_form = forms.SignupForm()

    if request.method == "POST":
        user_form = forms.SignupForm(data = request.POST, files = request.FILES)

        if user_form.is_valid():
            name = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']

            new_user = models.User.objects.create_user(username = name, password = password)
            new_user.save()
            photo = user_form.files.get('avatar', False)

            if photo:
                new_profile = models.Profile(user = new_user, avatar = photo)
            else:
                new_profile = models.Profile(user = new_user)

            new_profile.save()
            user = auth.authenticate(username = name, password = password)

            if user:
                auth.login(request, user)
                return redirect(reverse('index'))
    
    context = {
        'popular_tags': popular_tags,
        'best_users': best_users,
        'form': user_form
    }
    return render(request, "signup.html", context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))


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
        'questions': page_hot_questions,
        'popular_tags': popular_tags,
        'best_users': best_users,
    }

    return render(request, 'hot_questions.html', context=context)


def paginate(objects_list, request, items_per_page = 10):
    paginator = Paginator(objects_list, items_per_page)
    page_number = request.GET.get('page')
    page_items = paginator.get_page(page_number)

    return page_items


def add_tags_to_question(tags, question):
    for tag_name in tags.split(','):
        tag = models.Tag(name = tag_name)
        try:
            tag.save()
            question.tags.add(tag)
        except IntegrityError:
            pass
