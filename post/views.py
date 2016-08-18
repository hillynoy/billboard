from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Message
from django.http import HttpResponse
from django.template import loader
import datetime


def index(request):
    messages = Message.objects.all()
    timeNow = datetime.datetime.now()
    context = {"messages":messages,"time_now":timeNow}
    return render(request, 'post/index.html',context)


def create_message(request):
    my_title = request.POST.get("title")
    my_content = request.POST.get("content")
    my_author = request.POST.get("author")
    msg = Message.objects.create(title=my_title,content=my_content,author=my_author)
    msg.save()
    return redirect("/post")


