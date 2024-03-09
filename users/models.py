from django.db import models

from django.contrib.auth.models import AbstractUser

from materials.models import Course, Lesson, NULLABLE

# NULLABLE = {'null': True, 'blank': True}


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


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, max_length=100, verbose_name='пользователь')
    date_of_pay = models.DateField()
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, max_length=100, verbose_name='оплаченый курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, max_length=100, verbose_name='оплаченый урок')
    pay_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    pay_method = models.CharField(max_length=25, verbose_name='метод оплаты')  # cash or bank transfer
