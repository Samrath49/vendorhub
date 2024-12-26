# Generated by Django 5.1.4 on 2024-12-26 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_is_vendor'),
        ('product_service', '0002_delete_product_delete_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='low_stock_threshold',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_service.category'),
        ),
    ]
