# Generated by Django 4.0 on 2022-11-16 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_alter_inventory_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='current_inventory',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]
