from django.shortcuts import render, redirect
from .forms import *


def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('confirm_password')
            if password1 and password2 and password1 == password2:
                user = form.save()
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
    pass


def logout_view(request):
    pass

