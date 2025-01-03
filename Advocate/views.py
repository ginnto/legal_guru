
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import AdvocateRegistration
from home.models import *


def advregister(request):
    if request.method == "POST":

        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        password = request.POST.get('password')
        email = request.POST.get('email')
        specialization = request.POST.get('specialization')
        officename = request.POST.get('officename')
        place = request.POST.get('place')
        state = request.POST.get('state')
        district = request.POST.get('district')
        postoffice = request.POST.get('postoffice')
        pincode = request.POST.get('pincode')
        contactno = request.POST.get('contactno')
        aadharno = request.POST.get('aadharno')
        image = request.FILES.get('image')

        # Password validation and user creation
        # if User.objects.filter(username=username).exists():
        #     messages.error(request, "Username is already taken.")
        #     return redirect("register_advocate")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return redirect("advregister")

        else:
            user = User.objects.create_user(first_name=FirstName,last_name = LastName,username=FirstName,password=password, email=email)
            user.save()

            advocate = AdvocateRegistration.objects.create(
                user=user,
                specialization=specialization,
                officename=officename,
                place=place,
                state=state,
                district=district,
                postoffice=postoffice,
                pincode=pincode,
                contactno=contactno,
                image=image,
                aadharno=aadharno,
            )
            advocate.save()
            messages.success(request, "Registration successful!")
            return redirect('/')
    else:
        return render(request, 'adv_register.html')

def advlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Custom authentication using email
        try:
            user = User.objects.get(email=email)
            user = auth.authenticate(username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        print(email, password, user)

        if user is not None:
            auth.login(request, user)
            return redirect('advdash')
        else:
            messages.info(request, 'Invalid details')
            return redirect('advlogin')
    else:
        return render(request, 'advlogin.html')


def advdash(request):
    return render(request, 'advdash.html')

def advprofile(request):
    advocate = AdvocateRegistration.objects.get(user=request.user)
    return render(request, 'advprofile.html', {'advocate': advocate})

def case_list(request):
    advocate = request.user.advocateregistration
    cases = CaseRequest.objects.filter(lawyer=advocate)
    return render(request, 'advcaselist.html', {'cases': cases})

def advlogout(request):
    auth.logout(request)
    return redirect('/')