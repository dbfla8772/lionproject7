from django.shortcuts import redirect, render
from django.core.mail import EmailMessage

def send_mail(request):
    if request.method == 'POST' :
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        mail = EmailMessage(subject, message, to=[email])
        mail.send()
        return redirect('home')
    return render(request, 'mail.html')
