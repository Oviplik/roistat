from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, AccountUpdateForm
from .models import UserData, User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            api_key = form.cleaned_data.get('api_key')
            UserData.objects.create(user=user, api_key=api_key)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} успешно создан!')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def account(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        a_form = AccountUpdateForm(request.POST, instance=request.user.userdata)
        if u_form.is_valid() and a_form.is_valid():
            username = request.user
            password = u_form.cleaned_data.get('password')
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            a_form.save()
            messages.success(request, f'Ваш аккаунт успешно обновлен.')
            return redirect('account')

    else:
        u_form = UserUpdateForm(instance=request.user)
        a_form = AccountUpdateForm(instance=request.user.userdata)

    context = {
        'u_form': u_form,
        'a_form': a_form
    }

    return render(request, 'users/account.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'web/index.html')