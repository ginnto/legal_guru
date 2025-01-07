from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User,auth

from .forms import *
from .models import ClientRegistration, Feedback
from django.contrib.auth.decorators import login_required
from Advocate.models import *
from home.models import *

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
            # Check if the authenticated user is of type 'client'
            try:
                client = ClientRegistration.objects.get(user=user)
                if client.type == 'client':
                    # User is a client, log them in
                    auth.login(request, user)
                    messages.success(request, "Login successful!")
                    return redirect('clientdash')
                else:
                    # User is not a client
                    messages.error(request, "You are not authorized to log in as a client.")
                    return redirect('userlogin')
            except ClientRegistration.DoesNotExist:
                # ClientRegistration not found, handle it (e.g., show error)
                messages.error(request, "Client registration not found.")
                return redirect('userlogin')
        else:
            # Invalid email or password
            messages.error(request, "Invalid email or password.")
            return redirect('userlogin')
    else:
        return render(request, 'client_login.html')


def clientcase(request):
    advocates = AdvocateRegistration.objects.all()  # Fetch all advocates for the dropdown

    if request.method == "POST":
        lawyer_id = request.POST.get('lawyer')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        case_des = request.POST.get('case_des')

        if lawyer_id and name and email and phone and case_des:
            lawyer = AdvocateRegistration.objects.get(id=lawyer_id)  # Get the selected lawyer
            # Create a new CaseRequest object
            CaseRequest.objects.create(
                lawyer=lawyer,
                name=name,
                email=email,
                phone=phone,
                case_des=case_des,
            )
            messages.success(request, "Your case request has been submitted successfully!")
            return redirect('clientcase')  # Redirect to the same page or elsewhere
        else:
            messages.error(request, "Please fill in all fields correctly!")

    return render(request, 'clientcase.html',{'advocates': advocates})

def clientprofile(request):
    client = get_object_or_404(ClientRegistration, user=request.user)
    return render(request, 'clientprofile.html', {'client': client})

def clientcaselist(request):
    cases = CaseRequest.objects.all()
    return render(request, 'clientcaselist.html', {'cases': cases})

def clientdash(request):
    advocates = AdvocateRegistration.objects.all()
    return render(request, 'clientdash.html', {'advocates': advocates})






@login_required
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedback = form.save(commit=False)
            Feedback.user = request.user
            Feedback.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'submit_feedback.html', {'form': form})

@login_required
def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks})


def payment_page(request, case_id):
    # Fetch the case based on case_id
    case = get_object_or_404(CaseRequest, req_id=case_id)

    # Check if it's an unpaid case and process the payment
    if request.method == 'POST':
        # Fetch payment data from the form
        account_number = request.POST.get('account_number')
        cvv = request.POST.get('cvv')
        expiry_date = request.POST.get('expiry_date')
        amount_paid = request.POST.get('amount_paid')

        # Store payment data in the Payment model (create one if needed)
        # You can also perform any validation or save other details as needed.
        payment = Payment.objects.create(
            case=case,  # Link the payment to the case
            account_number=account_number,
            cvv=cvv,
            expiry_date=expiry_date,
            amount_paid=amount_paid,
            payment_date=datetime.now(),
            user = request.user
        )

        # Update the payment approval status of the case
        case.payment_approval = 'Paid'
        case.save()

        # Redirect to a confirmation page or back to the case list page
        return redirect('clientcaselist')  # You can replace with the appropriate URL

    return render(request, 'payment_page.html', {'case': case})