# Generated by Django 5.1.4 on 2024-12-26 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_service', '0001_initial'),
        ('shipment_service', '0003_delete_shipment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]