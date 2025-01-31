# Generated by Django 5.1.5 on 2025-01-31 20:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0001_initial'),
        ('produto', '0010_itemestoque'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItensPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0)),
                ('item_estoque', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='produto.itemestoque')),
                ('pedido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carrinho.pedido')),
            ],
        ),
    ]
