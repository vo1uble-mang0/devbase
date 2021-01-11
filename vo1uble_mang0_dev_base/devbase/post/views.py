from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import F
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import MyMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.core.mail import send_mail
from django.contrib import messages


def user_logout(request):
    logout(request)
    return redirect('home')


class Home(LoginRequiredMixin, ListView):
    # class Home(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    login_url = '/login/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'vo1uble.mang0'
        return context


class GetPost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post/single.html'
    context_object_name = 'post'
    login_url = '/login/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()

        return context


class Search(LoginRequiredMixin, ListView):
    template_name = 'post/search.html'
    context_object_name = 'posts'
    paginate_by = 10
    login_url = '/login/'

    def get_queryset(self):
        # if "Adventure":
        #     ready = ready.filter(tags__slug="Adventure")
        # ready = ready.filter(tags__slug="Adventure")
        #
        # ready = Post.objects.filter(tags__title__icontains='Beauty')
        # ready = Post.objects.filter(title__icontains='did')

        ready = Post.objects.filter(title__icontains=self.request.GET.get('s1'))
        ready = ready.filter(title__icontains=self.request.GET.get('s2'))

        if self.request.GET.get("Bootstrap") == "on": ready = ready.filter(tags__title__icontains='Bootstrap')
        if self.request.GET.get("CSS") == "on": ready = ready.filter(tags__title__icontains='CSS')
        if self.request.GET.get("DataScience") == "on": ready = ready.filter(tags__title__icontains='DataScience')
        if self.request.GET.get("Django") == "on": ready = ready.filter(tags__title__icontains='Django')
        if self.request.GET.get("HTML") == "on": ready = ready.filter(tags__title__icontains='HTML')
        if self.request.GET.get("Junior") == "on": ready = ready.filter(tags__title__icontains='Junior')
        if self.request.GET.get("Middle") == "on": ready = ready.filter(tags__title__icontains='Middle')
        if self.request.GET.get("Python") == "on": ready = ready.filter(tags__title__icontains='Python')
        if self.request.GET.get("SQL") == "on": ready = ready.filter(tags__title__icontains='SQL')
        if self.request.GET.get("Senior") == "on": ready = ready.filter(tags__title__icontains='Senior')
        if self.request.GET.get("Задача") == "on": ready = ready.filter(tags__title__icontains='Задача')
        if self.request.GET.get("Описание") == "on": ready = ready.filter(tags__title__icontains='Описание')
        if self.request.GET.get("Пример") == "on": ready = ready.filter(tags__title__icontains='Пример')
        if self.request.GET.get("Числа") == "on": ready = ready.filter(tags__title__icontains='Числа')
        if self.request.GET.get("Строки") == "on": ready = ready.filter(tags__title__icontains='Строки')
        if self.request.GET.get("Массивы") == "on": ready = ready.filter(tags__title__icontains='Массивы')
        if self.request.GET.get("Списки") == "on": ready = ready.filter(tags__title__icontains='Списки')
        if self.request.GET.get("Кортежи") == "on": ready = ready.filter(tags__title__icontains='Кортежи')
        if self.request.GET.get("Словари") == "on": ready = ready.filter(tags__title__icontains='Словари')
        if self.request.GET.get("Рекурсия") == "on": ready = ready.filter(tags__title__icontains='Рекурсия')

        return ready

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s1'] = f"s1={self.request.GET.get('s1')}&"
        context['s2'] = f"s2={self.request.GET.get('s2')}&"
        context['Bootstrap'] = f"Bootstrap={self.request.GET.get('Bootstrap')}&"
        context['CSS'] = f"CSS={self.request.GET.get('CSS')}&"
        context['DataScience'] = f"DataScience={self.request.GET.get('DataScience')}&"
        context['Django'] = f"Django={self.request.GET.get('Django')}&"
        context['HTML'] = f"HTML={self.request.GET.get('HTML')}&"
        context['Junior'] = f"Junior={self.request.GET.get('Junior')}&"
        context['Middle'] = f"Middle={self.request.GET.get('Middle')}&"
        context['Python'] = f"Python={self.request.GET.get('Python')}&"
        context['SQL'] = f"SQL={self.request.GET.get('SQL')}&"
        context['Senior'] = f"Senior={self.request.GET.get('Senior')}&"
        context['Задача'] = f"Задача={self.request.GET.get('Задача')}&"
        context['Описание'] = f"Описание={self.request.GET.get('Описание')}&"
        context['Пример'] = f"Пример={self.request.GET.get('Пример')}&"
        context['Числа'] = f"Числа={self.request.GET.get('Числа')}&"
        context['Строки'] = f"Строки={self.request.GET.get('Строки')}&"
        context['Массивы'] = f"Массивы={self.request.GET.get('Массивы')}&"
        context['Кортежи'] = f"Кортежи={self.request.GET.get('Кортежи')}&"
        context['Словари'] = f"Словари={self.request.GET.get('Словари')}&"
        context['Рекурсия'] = f"Рекурсия={self.request.GET.get('Рекурсия')}&"
        return context


class AddPostClass(LoginRequiredMixin, ListView):
    template_name = 'post/add_post.html'
    login_url = '/login/'

    def addpost(request):
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                message = form.cleaned_data['user_email'] + '\n' + form.cleaned_data['text'] + '\n' + form.cleaned_data[
                    'subject']
                mail = send_mail('Заявка на публикацию', message,
                                 'vo1uble.mang0.devbase@yandex.ru', ['vo1uble.mang0.devbase@yandex.ru'],
                                 fail_silently=False)
                if mail:
                    messages.success(request, 'Пост отправлен, ожидайте решения о публикации')
                    return redirect('add_post')
                else:
                    messages.error(request, 'Ошибка отправки')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            form = AddPostForm()
        return render(request, 'post/add_post.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('mainpage')
    else:
        form = UserLoginForm()
    # return render(request, 'post/login.html', {"form": form})
    return render(request, 'inc/_login.html', {"form": form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['username'] \
                      + '\n' + form.cleaned_data['password1'] \
                      + '\n' + form.cleaned_data['password2'] \
                      + '\n' + form.cleaned_data['user_email'] \
                      + '\n' + form.cleaned_data['comment']
            mail = send_mail('Заявка на регистрацию', message,
                             'vo1uble.mang0.devbase@yandex.ru', ['vo1uble.mang0.devbase@yandex.ru'],
                             fail_silently=False)
            if mail:
                messages.success(request, 'Заявка отправлена, ожидайте ответа на почту')
                return redirect('register')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка отправки')
    else:
        form = UserRegisterForm()
    return render(request, 'post/register.html', {"form": form})
