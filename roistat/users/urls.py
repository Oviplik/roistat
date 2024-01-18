"""
URL configuration for roistat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

urlpatterns = [
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('password-reset/', PasswordResetView.as_view(template_name="users/password_reset_form.html",
                                                      email_template_name="users/password_reset_email.html",
                                                      success_url=reverse_lazy("password-reset-done")),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name = "users/password_reset_done.html"), name='password-reset-done'),
    path('password-reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html",
                                                                             success_url=reverse_lazy("password-reset-complete")),
         name='password-reset-confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name='password-reset-complete'),

]
