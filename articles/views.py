from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from articles.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from articles.models import Profile, Article


def show_articles(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    return render(
        request,
        'articles.html',
        context
    )


def show_article(request, id):
    article = Article.objects.get(id=id)
    subscription = False
    if request.user.is_authenticated:
        subscription = request.user.profile.subscription

    context = {
        'article': article,
        'subscription': subscription
    }
    return render(
        request,
        'article.html',
        context
    )


def subscribe(request):
    msg = None
    if request.method == 'POST':
        if request.user.is_authenticated:
            this_user = request.user
            this_user.profile.subscription = True
            this_user.profile.save()
            msg = f'{this_user.username}, Вы успешно оформили подписку!'
        else:
            msg = 'Чтобы оформить подписку, необходимо авторизоваться.'
    context = {
        'msg': msg
    }
    return render(
        request,
        'subscribe.html',
        context
    )


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    username = None

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, password=password)
            Profile.objects.create(user=user)
            form = None
    else:
        form = RegistrationForm()

    context = {
        'form': form,
        'username': username
    }

    return render(
        request,
        'signup.html',
        context
    )


def login(request):
    msg = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('/')
                else:
                    form = LoginForm()
                    msg = 'Пользователь с такими данными не зарегистрирован'
            else:
                form = LoginForm()
                msg = 'Данные для входа введены неправильно'
    else:
        form = LoginForm()

    context = {
        'form': form,
        'msg': msg
    }

    return render(
        request,
        'login.html',
        context
    )


def logout(request):
    auth.logout(request)

    return render(
        request,
        'logout.html'
    )
