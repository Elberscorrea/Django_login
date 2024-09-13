from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUsuarioCreateForm, CustomLoginForm
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = CustomLoginForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect('home')
        return super().get(request, *args, **kwargs)


@login_required
def home(request):
    return render(request, 'home.html')


def cadastro(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = CustomUsuarioCreateForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'usuario cadastrado com sucesso!')
                return redirect('login')
            else:
                print(form.errors)
        else:
            form = CustomUsuarioCreateForm()
    else:
        return redirect('home')
    return render(request, 'registration/cadastro.html', {'form': form})


def redirect_to_login(request):
    return redirect('login')



