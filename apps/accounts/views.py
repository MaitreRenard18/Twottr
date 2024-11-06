from django.shortcuts import HttpResponse, render

from .models import User, get_user_from_username


def account_view(request, username: str) -> HttpResponse:
    return render(request, 'account.html', {'user': get_user_from_username(username)})


def login(request) -> HttpResponse:
    return render(request, 'login.html', {})


def signup(request) -> HttpResponse:
    return render(request, 'signup.html', {})
