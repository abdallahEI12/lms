from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormMixin,UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from lms.models import *
import decimal

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            if "next" in request.POST:
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "lms/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "lms/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        age = request.POST["age"]
        user_type = request.POST["user_type"]
        if user_type.strip().lower() == "teacher" or user_type.strip().lower() == "student":
            user_type_map = {
                'student': 1,
                'teacher': 2,
            }
            user_type = user_type_map[user_type.strip().lower()]
        else:
            return render(request, "lms/register.html", {
                "message": "Invalid user type."
            })
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "lms/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username = username,
                                            email = email,
                                            password = password,
                                            age = age,
                                            user_type = user_type)
            user.save()
            if user_type == 1:
                Student.objects.create(user=user)
            else:
                Teacher.objects.create(user=user)
        except IntegrityError:
            return render(request, "lms/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "lms/register.html")


def index(request):
    return render(request, "lms/index.html")