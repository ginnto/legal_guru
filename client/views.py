from django.shortcuts import render

# Create your views here.


def clientdash(request):
    return render(request, 'clientdash.html')