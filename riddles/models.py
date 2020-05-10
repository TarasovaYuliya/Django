from django.db import models


# создание таблицы в БД Riddle, где будет содержаться загадка
class Riddle(models.Model):
    riddle_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')


# создание таблицы в БД Option — один из возможных ответов на загадку
class Option(models.Model):
    riddle = models.ForeignKey(Riddle, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
