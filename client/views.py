from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User,auth

from .models import ClientRegistration  # Import ClientRegistration model

def clientregister(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        hname = request.POST.get('hname')
        place = request.POST.get('place')
        state = request.POST.get('state')
        district = request.POST.get('district')
        postoffice = request.POST.get('postoffice')
        pin = request.POST.get('pin')
        contactno = request.POST.get('contactno')
        aadharno = request.POST.get('aadharno')
        image = request.FILES.get('image')

        print(password)

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("clientregister")

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters.")
            return redirect("clientregister")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return redirect("clientregister")

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=email,  # Use email as the username
            password=password,
            email=email
        )
        print(user)
        user.save()

        client = ClientRegistration.objects.create(
            user=user,
            name=first_name + " " + last_name,  # Full name as first and last name combined
            gender=gender,
            hname=hname,
            place=place,
            state=state,
            district=district,
            postoffice=postoffice,
            pin=pin,
            contactno=contactno,
            image=image,
            aadharno=aadharno
        )
        client.save()

        messages.success(request, "Registration successful!")
        return redirect('/')
    else:
        return render(request, 'client_register.html')

def clientlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = auth.authenticate(request, username=email, password=password)

        if user is not None:
            # If authentication is successful, log the user in
            auth.login(request, user)
            messages.success(request, "Login successful!")
            return redirect('clientdash')  # Redirect to the client dashboard after login
        else:
            # If authentication fails
            messages.error(request, "Invalid email or password.")
            return redirect('userlogin')  # Redirect back to login page if authentication fails
    else:
        return render(request, 'client_login.html')


def clientdash(request):
    return render(request, 'clientdash.html')