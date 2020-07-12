from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from .models import *


def index(request):
    items = Items.objects.all()
    return render(request, "auctions/index.html", {
        "items": items,
    })


def listing(request, item):
    get_item = Items.objects.get(item_name=item)
    return render(request, "auctions/listing.html", {
        "get_item": get_item,
        "get_item_name": get_item.item_name
    })


@login_required
def fetch_bid(request):
    if request.method == "POST":
        listing_name = request.POST["listing_name"]
        bid_price = request.POST["bid_price"]
        bid_item = Items.objects.get(item_name=listing_name)
        bid_item_id = bid_item.id
        user = request.user.id
        createBid = Bid(item_id=bid_item_id,
                        bid_price=bid_price, bid_creator_id=user)
        createBid.save()

        #bid(item, bid_price, user)
    else:
        return render(request, "auctions/listing.html", {

        })


def categories(request):
    get_categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        "list_categories": get_categories
    })


def category_name(request, cat_name):
    get_cat = Category.objects.get(category_name=cat_name)
    list_items = get_cat.CategoryItems.all()
    return render(request, "auctions/categoryName.html", {
        "cat_name": cat_name,
        "list_items": list_items
    })


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
def create_listing(request):
    if request.method == "GET":
        return render(request, 'auctions/createListing.html',)
        # REVIEW: alert box
    else:
        request.method == "POST"
        postTitle = request.POST["postTitle"]
        postDes = request.POST["postDes"]
        startPrice = request.POST["startPrice"]
        imgUrl = request.POST["imgUrl"]
        cat_name = request.POST["catgyName"]
        userPk = request.user.id  # REVIEW:
        user = User.objects.get(id=userPk)
        newItem = Items(item_name=postTitle, description=postDes,
                        is_active=True, image_url=imgUrl, item_owner=user, start_price=startPrice)
        itmID = newItem.id
    #    userItem = UserItems(user=user, Item=itmID) # REVIEW:
        catAdd = Category(category_name=cat_name)
        newItem.save()
        # userItem.save()
        catAdd.save()
        return render(request, 'auctions/createListing.html',)


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
