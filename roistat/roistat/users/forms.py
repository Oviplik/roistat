from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import UserData

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    alphanumeric = RegexValidator(r'^[@.+-_\]\[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only alpha characters are allowed.')
    api_key = forms.CharField(required=False, label='API-ключ Roistat')
    username = forms.CharField(required=True, max_length=16, validators=[alphanumeric], label='Логин')
    first_name = forms.CharField(required=True, max_length=16, validators=[alpha], label='Ваше имя')
    password1 = forms.CharField(required=True, label='Пароль')
    password2 = forms.CharField(required=True, label='Подтверждение пароля')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2', 'api_key']


class UserUpdateForm(forms.ModelForm):
    alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only alpha characters are allowed.')
    first_name = forms.CharField(max_length=16, validators=[alpha], label='Ваше имя')
    email = forms.EmailField()
    password = forms.CharField(required=False,label='Новый пароль', widget=forms.widgets.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','email', 'password']

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['api_key']