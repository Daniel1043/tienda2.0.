# Generated by Django 4.1.13 on 2024-01-22 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_remove_valoracion_producto_remove_valoracion_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='valoracion',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.cliente'),
        ),
    ]
