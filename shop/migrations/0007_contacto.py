# Generated by Django 5.0.6 on 2024-06-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_producto_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]
