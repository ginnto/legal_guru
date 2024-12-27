from django.shortcuts import render

# Create your views here.

def clientregister(request):
    return render(request, 'client_register.html')

def clientdash(request):
    return render(request, 'clientdash.html')