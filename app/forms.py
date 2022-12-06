from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError
import re

from app import models


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)

    def clean_password(self):
        data = self.cleaned_data["password"]

        if not re.fullmatch("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$", data):
            raise ValidationError("The password must contain at least one lowercase and uppercase letter and one numeric value!")
        
        return self.cleaned_data["password"]


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=8,widget=forms.PasswordInput)
    password_repeat = forms.CharField(min_length=8, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        password_1 = self.cleaned_data['password']
        password_2 = self.cleaned_data['password_repeat']
        
        if password_1 != password_2:
            raise ValidationError("Passwords do not match!")
        user = User.objects.filter(username=self.cleaned_data['username'])

        if user:
            raise ValidationError("This username is already exist!")
        email = User.objects.filter(email=self.cleaned_data['email'])

        if email:
            raise ValidationError("User with this email is already exist!")

        return self.cleaned_data

    def save(self):
        self.cleaned_data.pop('password_repeat')

        return User.objects.create_user(**self.cleaned_data)


class SettingsForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'avatar')
        
    def save(self, commit=True):
        user = super().save()

        profile = user.profile
        profile.avatar = self.cleaned_data['avatar']

        if profile.avatar:
            profile.save()

        return user


class AskForm(forms.ModelForm):
    title = forms.CharField(min_length=6,max_length=255)
    text = forms.CharField(min_length=25, widget=forms.Textarea)
    tags = forms.CharField()

    class Meta:
        model = models.Question
        fields = ('title', 'text', 'tags')

    def save(self):
        tag_names = self.cleaned_data['tags']
        tags = []

        for tag_name in tag_names:
            tag, created = models.Tag.objects.get_or_create(value=tag_name)
            tags.append(tag)

        question = models.Question.objects.create(title=self.cleaned_data['title'], text=self.cleaned_data['text'])
        
        for tag in tags:
            question.tags.add(tag)

        return question
