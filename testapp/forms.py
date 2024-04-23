from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import MyUser


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Минимум 8 символов. Обязательно должна быть хотя бы одна цифра и специальный символ.',
    )

    class Meta:
        model = MyUser
        fields = ('username','email','password1', 'password2',)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
