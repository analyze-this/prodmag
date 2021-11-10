from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .forms import *


def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('confirm_password')
            if password1 and password2 and password1 == password2:
                user = form.save(commit=False)
                user.set_password(password1)
                user.save()
                return redirect('main_app:main')
            else:
                warning = 'Проверьте введенный пароль'
                return render(request, template_name='registration.html', context={'form': form, 'warning': warning})
    else:
        form = UserRegistrationForm()
    return render(request, template_name='registration.html', context={'form': form})


def login_view(request):
    url = request.GET['next']
    print(url)
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                if user.check_password(password):
                    login(request, user)
                    return redirect(url)
                return render(request, template_name='login.html', context={'form': form, 'warning': 'Неверный пароль'})
            else:
                warning = 'Такой пользователь не зарегистрирован в системе'
                return render(request, template_name='login.html', context={'form': form, 'warning': warning})

    return render(request, template_name='login.html', context={'form': form})


def logout_view(request):
    url = request.GET['url_logout']
    logout(request)
    return redirect(url)

