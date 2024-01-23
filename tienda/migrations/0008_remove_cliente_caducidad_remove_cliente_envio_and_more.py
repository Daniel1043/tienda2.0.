# Generated by Django 4.1.13 on 2024-01-23 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0007_producto_puntaje_valoracion_delete_valoracion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Caducidad',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='envio',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='facturacion',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nombre_ID',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='titular',
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ID', models.CharField(max_length=30, null=True, unique=True)),
                ('tipo', models.CharField(max_length=30)),
                ('titular', models.CharField(max_length=30, null=True)),
                ('Caducidad', models.CharField(help_text='Formato: 00/00', max_length=5, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.cliente')),
            ],
            options={
                'verbose_name_plural': 'Tarjetas',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('envio', models.CharField(max_length=30, null=True)),
                ('facturacion', models.CharField(max_length=30, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.cliente')),
            ],
            options={
                'verbose_name_plural': 'Direcciones',
            },
        ),
    ]
