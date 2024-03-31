from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .constants import USER_EMAIL_MAX_LEN, USER_NAME_MAX_LEN

letters_only = RegexValidator(
    r'^[a-zA-Zа-яА-Я]*$',
    'В логине только буквы допустимы.'
)

class User(AbstractUser):
    username = models.CharField(
        verbose_name='Логин',
        max_length=USER_NAME_MAX_LEN,
        unique=True,
        blank=False,
        validators=[letters_only]
    )   
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=USER_EMAIL_MAX_LEN,
        unique=True
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
