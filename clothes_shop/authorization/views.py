from django.shortcuts import render, redirect

from django.contrib.auth import login, logout
from .forms import RegistrationForm, LoginForm

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('index')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('index')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'registration.html', context)

def logout_user(request):
    logout(request)
    return redirect('index')