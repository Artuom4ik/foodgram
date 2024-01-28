from django.db import models

from categories.models import Card


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    scope_of_application = models.CharField(max_length=200, verbose_name='Сфера применения')
    diametr = models.FloatField(verbose_name='Диаметр')
    length = models.FloatField(verbose_name='Длинна')
    image = models.ImageField(null=True, default='', verbose_name='Изображение')
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='карточка'
    )

    def __str__(self) -> str:
        return self.title