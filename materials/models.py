from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='courses/preview/', verbose_name='превью', **NULLABLE)

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='lessons/preview/', verbose_name='превью', **NULLABLE)
    link_to_video = models.CharField(max_length=255, verbose_name='ссылка на видео', **NULLABLE)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
