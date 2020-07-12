from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class Items(models.Model):
    item_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200, null=True)
    is_active = models.BooleanField()
    item_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="UserItems")
    # REVIEW:
    item_category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET(Category), related_name='CategoryItems')
    start_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return self.item_name
# REVIEW: if there are no bids return current price
# if there are bids iternate over bids and get the highest number


class UserItems(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id}: ({self.item_id})"

    class Meta:
        verbose_name_plural = "User Items"


class Bid(models.Model):
    item_id = models.ForeignKey(
        Items, on_delete=models.CASCADE, related_name="ItemBids")
    bid_price = models.DecimalField(max_digits=8, decimal_places=2)
    bid_creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Comments(models.Model):
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.comment_text
