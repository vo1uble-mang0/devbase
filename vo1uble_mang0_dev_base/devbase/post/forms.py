from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control', 'autocomplete':"off"}))

class AddPostForm(forms.Form):
    user_email = forms.CharField(label='Email для ответа', widget=forms.EmailInput(attrs={'class':'form-control', 'autocomplete':"off"}))
    subject = forms.CharField(label='Название поста', widget=forms.TextInput(attrs={'class':'form-control', 'autocomplete':"off"}))
    text = forms.CharField(label='Текст поста', widget=forms.Textarea(attrs={'class':'form-control', 'autocomplete':"off"}))

class UserRegisterForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control', 'autocomplete':"off"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control', 'autocomplete':"off"}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class':'form-control', 'autocomplete':"off"}))
    user_email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control', 'autocomplete':"off"}))
    comment = forms.CharField(label='Комментарий(откуда узнали о проекте, для каких целей нужен доступ и пр.)', widget=forms.Textarea(attrs={'class':'form-control', 'autocomplete':"off"}))

