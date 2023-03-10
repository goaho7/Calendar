from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime

User = get_user_model()
def default_datetime(): return datetime.now().date


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class NameExercise(models.Model):
    title = models.CharField(max_length=200, verbose_name='Упражнение')
    slug = models.SlugField(unique=True)
    is_present = models.BooleanField(default=False)

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='exercises',
        verbose_name='Мышечная группа',
        help_text='Название мышечной группы'
    )

    def __str__(self):
        return self.title


class Day(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='exercises'
    )

    pub_date = models.DateTimeField(
        default=default_datetime,
        verbose_name='Дата тренировки')

    weight_body = models.FloatField(
        default=80.5,
        verbose_name='Вес тела',
        blank=True,
        null=True,)


class Exercise(models.Model):
    day = models.ForeignKey(
        Day,
        on_delete=models.CASCADE,
        related_name='exercises'
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name='Мышечная группа',
        help_text='Название мышечной группы'
    )

    name_exercise = models.ForeignKey(
        NameExercise,
        on_delete=models.CASCADE,
        verbose_name='Упражнение',
        help_text='Название упражнения'
    )

    comment = models.TextField(
        'Комментарий',
        help_text='Оставьте комментарий',
        blank=True,
        null=True,)


class Set(models.Model):
    weight = models.FloatField(default=0, verbose_name='Вес снаряда',)
    reps = models.IntegerField(default=8, verbose_name='Количество повторений')

    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='sets',
        verbose_name='Упражнение'
    )
