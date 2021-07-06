from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def Home(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        send_mail(
        f'{subject} from {name} email: {email}',
        f'{message}',
        'phantomkingpk12@gmail.com',
        ['Parjanya789@gmail.com'],
        fail_silently=False,
        )
        messages.success(request,"Message Sent!")
        return redirect('/')
    return render(request, 'index.html')
