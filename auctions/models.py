from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    imageUrl = models.URLField(max_length=200, null=True)
    is_active = models.BooleanField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="UserItems")
    # REVIEW:
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET(Category), related_name='CategoryItems')
    start_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name
# REVIEW: if there are no bids return current price
# if there are bids iternate over bids and get the highest number


class UserItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Item = models.ForeignKey(Items, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: ({self.Item})"

    class Meta:
        verbose_name_plural = "User Items"


class Bid(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    bid_price = models.DecimalField(max_digits=8, decimal_places=2)
    bidOwner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bid_price


class Comments(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.text
