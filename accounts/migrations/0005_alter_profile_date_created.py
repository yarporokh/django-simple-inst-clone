# Generated by Django 3.2.2 on 2021-07-30 12:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210720_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
