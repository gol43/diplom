from django.db import models
from django.contrib.auth import get_user_model
from users.models import User


class Category(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.TextField(max_length=50)
    cost = models.PositiveIntegerField()
    description = models.TextField(max_length=500)
    image = models.ImageField(
        'Картинка',
        upload_to='products/',
        blank=True
    )
    amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart_user')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='shopping_cart_product')

    def __str__(self):
        return f'{self.user} добавил "{self.product}" в список покупок'


class Comment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='comments')

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',)

    text = models.TextField(
        max_length=500)

    created = models.DateTimeField(
        verbose_name='Дата коммента',
        auto_now_add=True,)
    
    def __str__(self):
        return self.text
