# Generated by Django 4.2.9 on 2024-02-08 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='subgroup',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
    ]
