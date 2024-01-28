from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='groups',
        verbose_name='Секция')