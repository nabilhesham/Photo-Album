from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages


def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                messages.success(request, ('Username Has Already Been Taken..'))
                return render(request, 'signup.html', {})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                messages.success(request, "WELCOME,,")
                return redirect('home')
        else:
            messages.success(request, ('Passwords MUST Match !!'))
            return render(request, 'signup.html', {})
    else:
        # User wants to enter info
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None :
            auth.login(request,user)
            messages.success(request, "WELCOME BACK,,")
            return redirect('home')
        else :
            messages.success(request, ('Username OR Password is INCORRECT !!'))
            return render(request, 'login.html', {})
    else :
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "BYE,,")
        return redirect('home')
