from django.contrib.auth.views import LoginView
from django.urls import path
from django import forms
from .views import home, register
from . import views
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

]
