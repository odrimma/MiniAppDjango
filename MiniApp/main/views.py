from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import EditUserForm
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    users = User.objects.filter(is_superuser=False)
    return render(request, 'main/index.html', {'users': users, 'title': 'Список пользователей'})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('edit_user', request.user.id)
    return render(request, 'main/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

class Edit_View(LoginRequiredMixin, UpdateView):
    form_class = EditUserForm
    model = User
    template_name = 'main/edit_user.html'
    success_url = '/'
