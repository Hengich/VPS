from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .consts import (MIN_CPU_COUNT, MAX_CPU_COUNT,
                     MIN_RAM_SIZE, MAX_RAM_SIZE,
                     MIN_HDD_SIZE, MAX_HDD_SIZE)


class VPS(models.Model):
    STATUS_CHOICES = [
        ('started', 'Started'),
        ('blocked', 'Blocked'),
        ('stopped', 'Stopped')
    ]

    uid = models.AutoField(primary_key=True)
    cpu = models.IntegerField(
        verbose_name='Количество процессорных ядер',
        validators=[
            MinValueValidator(MIN_CPU_COUNT,
                              message='Не менее одного ядра!'),
            MaxValueValidator(MAX_CPU_COUNT,
                              message='Превышено максимальное кол-во ядер!'),
        ],
    )
    ram = models.IntegerField(
        verbose_name='Объем оперативной памяти',
        validators=[
            MinValueValidator(MIN_RAM_SIZE,
                              message='Не менее 1 гигабайта!'),
            MaxValueValidator(MAX_RAM_SIZE,
                              message='Не более 64 гигабайт!'),
        ],
    )
    hdd = models.IntegerField(
        verbose_name='Объем дискового пространства',
        validators=[
            MinValueValidator(
                MIN_HDD_SIZE,
                message='Не менее 128 гигабайт!'
            ),
            MaxValueValidator(
                MAX_HDD_SIZE,
                message='Не более 2048 гигабайт!'
            ),
        ],
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='stopped'
    )

    class Meta:
        verbose_name = 'Сервер'
        verbose_name_plural = 'Серверы'
        ordering = ('uid'),

    def __str__(self):
        return f"VPS {self.uid}: {self.status}"
