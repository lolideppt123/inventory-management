# Generated by Django 4.0 on 2022-11-07 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_sales_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='product_name',
        ),
    ]
