# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.urls import path
from .views import home, redirect_to_login, cadastro

urlpatterns = [
    path('', redirect_to_login),
    path('home/', home, name='home'),
    path('cadastro/', cadastro, name='cadastro')
]

