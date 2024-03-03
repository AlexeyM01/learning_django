import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Класс описания Вопроса"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    ans_amount = models.IntegerField(default=0)

    def __str__(self):
        """ Переопределение метода отображения информации об объекте"""
        return self.question_text

    def was_published_recently(self):
        """ Функция возвращающая вопросы, которые были опубликованы за последний день"""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """ Класс описания Выбора для класса Вопроса"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """ Переопределение метода отображения информации об объекте"""
        return self.choice_text
