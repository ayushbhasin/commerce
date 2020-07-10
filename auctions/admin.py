from django.contrib import admin

from .models import User, Category, Items, UserItems, Bid, Comments

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Items)
admin.site.register(UserItems)
admin.site.register(Bid)
admin.site.register(Comments)
