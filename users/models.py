from django.db import models

from django.contrib.auth.models import AbstractUser

from materials.models import Course, Lesson, NULLABLE


# NULLABLE = {'null': True, 'blank': True}
class Roles(models.TextChoices):
    USER = "user"
    MODERATOR = "moderator"


class User(AbstractUser):
    username = None
    role = models.CharField(max_length=25, choices=Roles.choices, default=Roles.USER)
    first_name = models.CharField(max_length=100, verbose_name='имя')
    middle_name = models.CharField(max_length=100, verbose_name='отчество', **NULLABLE)
    last_name = models.CharField(max_length=100, verbose_name='фамилия', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=16, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, max_length=100, verbose_name='пользователь')
    date_of_pay = models.DateField(verbose_name='дата оплаты', **NULLABLE)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    pay_amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    pay_method = models.CharField(max_length=25, verbose_name='метод оплаты')  # cash or bank transfer
