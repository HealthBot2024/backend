from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def index(request):
    if request.user.is_authenticated:
        user = request.user
        username = user.username
        display_name = user.display_name
        return render(request, 'index.html', {
            'user': True,
            'username': username,
            'display_name': display_name
        })
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'register.html', context=form.errors)

    return render(request, 'register.html', {})

def loginPage(request):
    form = None
    errors = []
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                errors.append("You may not log in at this time.")
        else:
            errors.append("This user was not found.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'errors': errors})

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/')
    user = request.user
    username = user.username
    display_name = user.display_name

    return render(request, 'dashboard.html', {
            'username': username,
            'display_name': display_name
        })
