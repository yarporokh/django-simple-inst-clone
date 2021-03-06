# Generated by Django 3.2.2 on 2021-07-30 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_date_created'),
        ('posts', '0008_alter_post_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(blank=True, default='admin', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
