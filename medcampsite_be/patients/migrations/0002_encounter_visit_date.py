# Generated by Django 4.2.7 on 2024-01-09 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='encounter',
            name='visit_date',
            field=models.DateField(auto_now=True),
        ),
    ]
