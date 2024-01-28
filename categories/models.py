from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=200, verbose_name='')
    description = models.TextField(blank=True, null=True, verbose_name='')


