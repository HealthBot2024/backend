from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import User

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
    return render(request, 'index.html', {
            'user': False,
        })

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/log-in')
        else:
            return render(request, 'register.html', {
                **form.erros,
                'user': False
            })

    return render(request, 'register.html',  {
            'user': False,
        })

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
                return redirect('/dashboard')
            else:
                errors.append("You may not log in at this time.")
        else:
            errors.append("This user was not found.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'errors': errors, 'user': False})

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

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def delete_user(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('/')

def find_user(request):
    if request.method == 'GET':
        username = request.GET.get('u')
        password = request.GET.get('p')

        user = authenticate(request, username=username, password=password)
        if user:
            return JsonResponse({
                'ok': True,
                'display_name': user.display_name
            })
        else:
            return JsonResponse({
                'ok': False
            })
    else:
        return redirect('/')

def myDriving(request):
    if request.user.is_authenticated:
        return render(request, 'driving.html', {
            'ranking': request.user.ranking,
            'display_name': request.user.display_name,
            'score': request.user.score,
            'drives': request.user.drives
        })
    else:
        return redirect('/')

def boards(request):
    if request.user.is_authenticated:
        qset = User.objects.all().order_by('score')
        context = [{
            'display_name': user.display_name,
            'username': user.username,
            'ranking': user.ranking,
            'score': user.score,
            'place': i + 1
        } for i, user in enumerate(qset)]

        return render(request, 'boards.html', {
            'ordered': context,
            'username': request.user.username
        })
    else:
        return redirect('/')
