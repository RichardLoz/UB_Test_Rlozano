# Generated by Django 5.0.6 on 2024-06-15 03:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0009_remove_categoria_fecha_alta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.categoria'),
        ),
    ]
