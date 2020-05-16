from django.db import models
# встроенная модель пользователя
# нужна для авторов сообщений
from django.contrib.auth.models import User
# тип "временнАя зона" для получения текущего времени
from django.utils import timezone


# создание таблицы в БД Riddle, где будет содержаться загадка
class Riddle(models.Model):
    riddle_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')


# создание таблицы в БД Option — один из возможных ответов на загадку
class Option(models.Model):
    riddle = models.ForeignKey(Riddle, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)


class Message(models.Model):
    chat = models.ForeignKey(
        Riddle,
        verbose_name='Чат под загадкой',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.TextField('Сообщение')
    pub_date = models.DateTimeField(
        'Дата сообщения',
        default=timezone.now)
