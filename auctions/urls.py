from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listing/<str:item>", views.listing, name="listing"),
    path("placeBid", views.fetch_bid, name="fetchBid"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createListing", views.create_listing, name="create_listing"),
    #path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:cat_name>", views.category_name, name="category_name"),
    #path("categoryName/<str:catName>", views.categoryName, name="index"),
]
