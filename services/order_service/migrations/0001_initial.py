# Generated by Django 5.1.4 on 2024-12-26 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.IntegerField()),
                ('status', models.CharField(default='pending', max_length=20)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'indexes': [models.Index(fields=['user'], name='order_servi_user_62e17f_idx'), models.Index(fields=['status'], name='order_servi_status_9e40f6_idx')],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_service.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product_service.product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product_service.vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]