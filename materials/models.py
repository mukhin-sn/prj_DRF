from django.db import models

# import users.models

# from users.models import User

# from users.models import NULLABLE
NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='название курса')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='courses/preview/', verbose_name='превью', **NULLABLE)
    master = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='название урока')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='lessons/preview/', verbose_name='превью', **NULLABLE)
    link_to_video = models.CharField(max_length=255, verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, max_length=100, verbose_name='курс')
    master = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class UpdateSubscription(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, max_length=100, verbose_name='курс')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
