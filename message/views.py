from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404  
from .models import Message
from .forms import MessageForm
from django.utils import timezone

def inbox(request):
    messages = Message.objects.filter(receiverID = request.user)
    return render(request, "inbox.html", {'messages':messages})

def send_box(request):
    messages = Message.objects.filter(senderID = request.user) 
    return render(request, "send_box.html", {'messages':messages})

def detail_message(request, id):
    message = get_object_or_404(Message, pk = id)
    return render(request, 'detail_message.html', {'message':message})

def new_message(request):
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            new_message = message_form.save(commit=False)  # 임시저장
            message_form.send_date = timezone.now()
            new_message.save()
            return redirect('send_box')
    else:
        message_form = MessageForm()
        return render(request, 'new_message.html', {'message_form':message_form})



