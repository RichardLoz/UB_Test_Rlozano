# Generated by Django 5.0.6 on 2024-06-15 01:34

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0007_alter_producto_fecha_alta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('fecha_alta', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('fecha_baja', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.categoria'),
        ),
    ]
