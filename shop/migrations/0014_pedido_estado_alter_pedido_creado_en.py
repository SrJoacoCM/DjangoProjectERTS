# Generated by Django 5.0.6 on 2024-06-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_pedido_pedidoitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('DESPACHO', 'En Despacho'), ('TRANSITO', 'En Tránsito'), ('ENTREGADO', 'Entregado')], default='PENDIENTE', max_length=20),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='creado_en',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]