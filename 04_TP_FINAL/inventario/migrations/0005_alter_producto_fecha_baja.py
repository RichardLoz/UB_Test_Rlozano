# Generated by Django 5.0.6 on 2024-06-12 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_rename_categoria_id_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_baja',
            field=models.DateField(blank=True, null=True),
        ),
    ]
