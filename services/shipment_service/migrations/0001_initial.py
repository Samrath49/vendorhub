# Generated by Django 5.1.4 on 2024-12-26 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order_service', '0001_initial'),
        ('product_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tracking_number', models.CharField(blank=True, max_length=100)),
                ('carrier', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order_service.order')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product_service.vendor')),
            ],
            options={
                'indexes': [models.Index(fields=['order'], name='shipment_se_order_i_63231a_idx'), models.Index(fields=['vendor'], name='shipment_se_vendor__e524ca_idx'), models.Index(fields=['status'], name='shipment_se_status_c3a435_idx')],
            },
        ),
    ]