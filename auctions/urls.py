from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listing/<str:item>", views.listing, name="listing"),
    path("placeBid",  views.placeBid, name="placeBid"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createListing", views.createListing, name="createListing"),
    #path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:catName>", views.categoryName, name="categoryName"),
    #path("categoryName/<str:catName>", views.categoryName, name="index"),
]
