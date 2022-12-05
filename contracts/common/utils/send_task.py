from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from django.conf import settings

# from .forms import EmailForm
from django.http import HttpResponse


# Create your views here.
def send_task_notification(request):
    # Send regular email
    # message = send_mail('Hello from PMNotes Contracts Management System',
    #                     'Hello there, This is an automated message from PMNotes Contracts Management System',
    #                     'john.hinson@consutekllc.com', ['johnhinson@ufit15.com', 'JohnHHinsonIII@gmail.com'],
    #                     fail_silently=False),

    # Send attachments

    # subject = request.POST.get('subject', '')
    # message = request.POST.get('message', '')
    # from_email = request.POST.get('from_email', '')

    msg = EmailMessage('PMNotes Contracts Management System',
                       'Hello there, This is an automated message from PMNotes Contracts Management System',
                       'john.hinson@consutekllc.com', ['johnhinson@ufit15.com', 'JohnHHinsonIII@gmail.com'])
    msg.content_subtype = "html"
    # msg.attach_file('tasks.pdf')
    msg.send()

    return HttpResponse('Tasks Sent!')
# return render(request, 'tasks.html')
