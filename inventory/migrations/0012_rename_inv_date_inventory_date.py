# Generated by Django 4.0 on 2022-11-15 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_alter_currenttotalinventory_current_inventory_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='inv_date',
            new_name='date',
        ),
    ]