# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUsuario
from django import forms


class CustomUsuarioCreateForm(UserCreationForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'telefone', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user


class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'telefone')


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Endereço de e-mail')

    class Meta:
        model = CustomUsuario
        fields = ('email', 'password')

