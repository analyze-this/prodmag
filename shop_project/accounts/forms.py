from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=20, label='Подтверждение пароля', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        help_texts = {'username': ''}
        widgets = {'password': forms.PasswordInput()}


class UserRegForm(UserCreationForm):
    pass
