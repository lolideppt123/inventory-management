# Generated by Django 4.0 on 2022-10-11 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_alter_category_options_alter_expense_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
