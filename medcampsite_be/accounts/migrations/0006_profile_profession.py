# Generated by Django 4.2.7 on 2023-11-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profession',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]