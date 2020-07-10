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
    imageUrl = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # REVIEW:
    category = models.ForeignKey(Category, on_delete=models.SET(Category))
    startPrice = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return f"{self.id}{self.name}{self.description}{self.is_active}"
        "{self.owner} {self.category} {self.startPrice}"


class UserItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Item = models.ForeignKey(Items, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}{self.user}{self.Item}"

    class Meta:
        verbose_name_plural = "User Items"


class Bid(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    bid_price = models.DecimalField(max_digits=8, decimal_places=2)
    bidOwner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id, self.item, self.bid_price, self.bidOwner


class Comments(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.id, self.item, self.text, self.user