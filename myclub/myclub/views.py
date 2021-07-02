from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
def home(request):
    return render(request, 'index.html')

def inquiry(request):
    if request.method == 'POST':
            emailto = settings.EMAIL_HOST_USER
            name = request.POST['name']
            subject = request.POST['subject']
            message = request.POST['message']
            email_from = request.POST['email']
            recipient = [emailto,]
            send_mail(subject,message,email_from,recipient)
            mg = 'Inquiry sent!'
            return render(request, 'index.html', {mg : 'mg'})

    else:
        return render(request, 'index.html')
