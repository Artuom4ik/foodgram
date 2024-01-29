# Generated by Django 4.2.9 on 2024-01-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_diametr_alter_product_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=100, null=True, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='', verbose_name='Изображение'),
        ),
    ]
