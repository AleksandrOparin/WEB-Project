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
    