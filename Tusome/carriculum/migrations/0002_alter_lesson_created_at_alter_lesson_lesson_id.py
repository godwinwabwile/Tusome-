# Generated by Django 4.0.4 on 2022-05-26 08:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('carriculum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 8, 21, 21, 299171, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_id',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
