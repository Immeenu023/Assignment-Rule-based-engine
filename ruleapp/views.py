from django.shortcuts import render
from .models import AddRule
from django.contrib.auth import *
from django.http.response import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

"""
    function to add a new rule in database from template and show it on template.
"""


def addrule(request):
    data = AddRule.objects.all()
    print(data)
    if request.method == 'POST':
        rulename = request.POST.get('rulename')
        campaign = request.POST.get('campaign')
        schedule = request.POST.get('schedule')
        action = request.POST.get('action')
        status = request.POST.get('status')
        a = AddRule(ruleName=rulename, campaign=campaign, schedule=schedule, action=action, status=status)
        a.save()
        data = AddRule.objects.all()
        print(data)

        return render(request, 'ruleapp/home.html', {'data': data})
    else:
        return render(request, 'ruleapp/home.html')


"""
    function to do verification a user.
"""


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'ruleapp/home.html')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'ruleapp/login.html')


"""
    function to send email .
"""


def email(request):
    subject = 'Rule status info'
    message = 'Rule status is changed'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['msaini023@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse('Check your mail')
