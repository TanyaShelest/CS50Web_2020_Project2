from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User, Listing, Watchlist
from .forms import ListingForm, CommentForm


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
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


@login_required
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.author = request.user
            listing.save()
            return HttpResponseRedirect(reverse('index'))
    
    form = ListingForm()
    return render(request, "auctions/create_listing.html", {
        "form": form
    })


def show_listing(request, id):
    listing = Listing.objects.get(pk=id)
    comments = listing.comments.all()
    if request.user.is_authenticated:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.listing = listing
                comment.save()
                return HttpResponseRedirect(reverse('show_listing', kwargs={
                    "id": id
                }))
    
    return render(request, "auctions/show_listing.html", {
        "listing": listing,
        "comments": comments, 
        "comment_form": CommentForm()
    })


@login_required(login_url='login')
def show_watchlist(request):
    watchlist = Watchlist.objects.get(user=request.user)
    return render(request, "auctions/show_watchlist.html", {
        "watchlist": watchlist
    })


@login_required(login_url='login')
def add_to_watchlist(request, id):
    item = Listing.objects.get(pk=id)
    if Watchlist.objects.filter(user=request.user, items=id).exists():
        messages.add_message(request, messages.ERROR, 'You\'ve already added this item to your watchlist.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    watchlist, created = Watchlist.objects.get_or_create(user=request.user)
    watchlist.items.add(item)

    messages.add_message(request, messages.SUCCESS, 'Successfully added to your watchlist!')
    return HttpResponseRedirect(reverse('show_watchlist'))


@login_required
def remove_from_watchlist(request, id):
    watchlist = Watchlist.objects.get(user=request.user)
    item = watchlist.items.get(pk=id)
    watchlist.items.remove(item)
    messages.add_message(request, messages.SUCCESS, 'Removed from your watchlist!')
    return HttpResponseRedirect(reverse('show_watchlist'))


