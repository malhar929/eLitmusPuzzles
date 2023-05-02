from django.shortcuts import render, redirect

# Create your views here.


from .forms import CreateUserForm
from django.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def home(request):
    return render(request, 'index.html')


# @login_required(login_url='/accounts/login/')
def puzzle1(request):
    return render(request, 'puzzle1.html')


# @login_required(login_url='/accounts/login/')
def puzzle2(request):
    return render(request, 'puzzle2.html')


# @login_required(login_url='/accounts/login/')
def puzzle3(request):
    return render(request, 'puzzle3.html')


# ############################## LOGIN


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # authenticate user

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='login')
def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(
                    request, 'Account Created successfully for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'register.html', context)

# ##############################
