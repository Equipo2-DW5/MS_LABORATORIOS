# Generated by Django 3.2.6 on 2021-08-27 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratoriosApp', '0004_auto_20210827_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorio',
            name='descripcion',
            field=models.CharField(max_length=100, verbose_name='Descripcion'),
        ),
    ]