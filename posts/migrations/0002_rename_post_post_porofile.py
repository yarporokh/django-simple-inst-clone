# Generated by Django 3.2.2 on 2021-07-15 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='porofile',
        ),
    ]
