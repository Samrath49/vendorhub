# Generated by Django 5.1.4 on 2024-12-26 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipment_service', '0002_alter_shipment_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shipment',
        ),
    ]
