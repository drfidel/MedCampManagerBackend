# Generated by Django 4.2.7 on 2024-01-19 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_alter_encounter_visit_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='encounter',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='encounter',
            name='labrequest',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddIndex(
            model_name='encounter',
            index=models.Index(fields=['identity'], name='patients_en_identit_09e60a_idx'),
        ),
    ]