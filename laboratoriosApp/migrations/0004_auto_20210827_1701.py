# Generated by Django 3.2.6 on 2021-08-27 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratoriosApp', '0003_alter_laboratorio_ubicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorio',
            name='descripcion',
            field=models.CharField(max_length=100, unique=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='ubicacion',
            field=models.CharField(max_length=100, verbose_name='Ubicacion'),
        ),
    ]
