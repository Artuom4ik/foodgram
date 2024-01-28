from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self) -> str:
        return self.title


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='groups',
        verbose_name='Секция')
    
    def __str__(self) -> str:
        return self.title
    

class Subgroup(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='subgroups',
        verbose_name='Группа')
    
    def __str__(self) -> str:
        return self.title


class Card(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    subgroup = models.ForeignKey(
        Subgroup,
        on_delete=models.CASCADE,
        related_name='cards',
        verbose_name='Подгруппа')
    
    def __str__(self) -> str:
        return self.title
