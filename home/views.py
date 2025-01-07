from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request,'index.html')

@login_required
def chat_list(request):
    return render(request, 'chat_list.html')

@login_required
def chat_detail(request):
    return render(request, 'chat_detail.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
