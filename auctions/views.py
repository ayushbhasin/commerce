from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from .models import *


def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


@login_required
def createListing(request):
    if request.method == "GET":
        return render(request, 'auctions/createListing.html',)
        # REVIEW: alert box
    else:
        request.method == "POST"
        postTitle = request.POST["postTitle"]
        postDes = request.POST["postDes"]
        startPrice = request.POST["startPrice"]
        userPk = request.user.id  # REVIEW:
        user = User.objects.get(id=userPk)
        newItem = Items(name=postTitle, description=postDes,
                        is_active=True, owner=user, startPrice=startPrice)
        newItem.save()
        return render(request, 'auctions/createListing.html',)


def activeListings():
    return render(request, "auctions/activeListings.html")


"""
def watchlist():
    return render(request, "auctions/watchlist.html")


def activeListings():
    return render(request, "auctions/activeListings.html")


def categories():
    return render(request, "auctions/categories.html")
"""


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
