from django.db import models

from django.contrib.auth.models import AbstractUser


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    middle_name = models.CharField(max_length=100, verbose_name='Отчество', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=16, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

