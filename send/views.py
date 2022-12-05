from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from django.conf import settings


# from .forms import EmailForm

# Create your views here.
def index(request):
    # Send regular email
    # message = send_mail('Hello from PMNotes Contracts Management System',
    #                     'Hello there, This is an automated message from PMNotes Contracts Management System',
    #                     'john.hinson@consutekllc.com', ['johnhinson@ufit15.com', 'JohnHHinsonIII@gmail.com'],
    #                     fail_silently=False),

    # Send attachments
    msg = EmailMessage('PMNotes Contracts Management System',
                       'Hello there, This is an automated message from PMNotes Contracts Management System',
                       'john.hinson@consutekllc.com', ['johnhinson@ufit15.com', 'JohnHHinsonIII@gmail.com'])
    msg.content_subtype = "html"
    msg.attach_file('media/contract-docs/1657545543482.pdf')
    msg.send()

    return render(request, 'send/index.html')
