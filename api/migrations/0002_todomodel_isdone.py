# Generated by Django 5.0 on 2024-08-26 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='isDone',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
