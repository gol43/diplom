from django.contrib import admin
from users.models import User
from .models import Category, Product, Comment, ShoppingCart
# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(ShoppingCart)
