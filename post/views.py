from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Message
from django.http import HttpResponseRedirect
from django.template import loader
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# @login_required
# def create_message(request):


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
        login(request, new_user)
        return HttpResponseRedirect("/post/")
    else:
        form = UserCreationForm()
        return render(request, "registration/register.html", {'form': form,
                                                                  })


def login_page(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return (request, 'post/index.html')
        else:
            return ("error message: the user is not active")
    else:
        return ("invalid login error message")


def index(request):
    messages = Message.objects.all()
    timeNow = datetime.datetime.now()
    context = {"messages": messages, "time_now": timeNow}
    return render(request, 'post/index.html', context)


def create_message(request):
    my_title = request.POST.get("title")
    my_content = request.POST.get("content")
    my_author = request.POST.get("author")
    msg = Message.objects.create(title=my_title, content=my_content, author=my_author)
    msg.save()
    return redirect("/post")
