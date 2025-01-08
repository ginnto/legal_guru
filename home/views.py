from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from Advocate.models import *
from client.models import *
from .models import *
# Create your views here.


def index(request):
    return render(request,'index.html')




@login_required
def send_message(request, id):
    case = get_object_or_404(CaseRequest, req_id=id)
    receiver = get_object_or_404(AdvocateRegistration,id=case.lawyer.id)
    receiver_user = receiver.user
    print("Receiver User ID:", receiver_user.id)  # This will print the User ID

    if request.method == 'POST':
        message_content = request.POST.get('message')

        if message_content:  # Check if the message content exists
            # Create and save the message in ChatMessage model
            chat_message = ChatMessage.objects.create(
                sender=request.user,
                receiver=receiver_user,
                content=message_content
            )
            chat_message.save()

            # Optionally, redirect or return to a chat page
            return redirect('chat_list')  # Replace with your desired redirect

    # Render the form or page where the message will be sent (if GET method)
    return render(request, 'send_message.html', {'receiver': receiver})

def chat_list(request):
    chats = ChatMessage.objects.filter(sender=request.user)
    return render(request, 'chat_list.html', {'chats': chats})


def advchat_list(request):
    chats = ChatMessage.objects.filter(receiver=request.user)
    if request.method == "POST":
        chat_id = request.POST.get("chat_id")
        message_content = request.POST.get("message")
        if chat_id and message_content:
            # Fetch the chat object or return a 404 if not found
            chat = get_object_or_404(ChatMessage, id=chat_id)

            chat.reply_to = message_content
            chat.save()

            # Optionally, add a success message or redirect
            messages.success(request, "Reply sent successfully.")
        else:
            # Optionally, add an error message if the input is incomplete
            messages.error(request, "Failed to send reply. Please ensure all fields are filled.")
    return render(request, 'advchatlist.html', {'chats': chats})

def logout(request):
    auth.logout(request)
    return redirect('/')
