# Generated by Django 4.0 on 2022-10-24 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpreferences', '0003_alter_userpreference_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreference',
            name='currency',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
