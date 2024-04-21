from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from .forms import LoginForm


User = get_user_model()


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            user = authenticate(request, username=username, password=raw_password)
            messages.success(request, f'Создан аккаунт {username}!')
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

    if form.is_valid():
        if '@' in form.cleaned_data['username']:
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
        else:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('')

    return render(request, 'login.html', {'form': form})


def logout(request):
    logout(request)
    return redirect('')
