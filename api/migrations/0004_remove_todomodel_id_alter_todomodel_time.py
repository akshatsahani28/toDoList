# Generated by Django 5.0 on 2024-08-26 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_todomodel_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todomodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='time',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
