from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages


def home(request):
    return render(request, "chatapp/html/home.html")

def login(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Login successfully")
    else:
        form = UserCreationForm()
    return render(request, "chatapp/html/login.html", {'form':form})
    
    