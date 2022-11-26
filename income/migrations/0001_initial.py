# Generated by Django 4.0 on 2022-10-23 23:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('source', models.CharField(max_length=250)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.user')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]