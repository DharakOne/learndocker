# Generated by Django 3.1.4 on 2020-12-15 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='entregado',
            field=models.BooleanField(),
        ),
    ]