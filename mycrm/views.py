from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            messages.success(request, 'You have login succesfully!')
            return redirect('home')
        else:
            messages.success(request,
                             "We couldn't find an account with that username. Try another, or get a new  account.")
            return redirect('home')
    else:
        return render(request, 'home.html')

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logout succesfully")
    return redirect('home')

def register(request):
    form=SignUpForm()
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have succesfully Register.")
            return redirect('home')
        else:
            messages.success(request, "You must writ correct data!!!")
            return redirect('Register')
    else:
        form = SignUpForm()
        return render(request, 'Register.html', {'form': form})

    return render(request, 'Register.html')



