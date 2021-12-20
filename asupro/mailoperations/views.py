from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from mailoperations.models import Follower
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def subscribe(request,followermail):
    follower = Follower.objects.get_or_create(mail=followermail)
    send_mail('Рассылка', 'Спасибо за подписку', settings.EMAIL_HOST_USER, ['followermail'])
    return HttpResponseRedirect('/index')