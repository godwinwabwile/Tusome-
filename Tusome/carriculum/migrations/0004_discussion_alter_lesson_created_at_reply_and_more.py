# Generated by Django 4.0.4 on 2022-05-28 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carriculum', '0003_alter_lesson_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=145)),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
        migrations.AlterField(
            model_name='lesson',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='carriculum.discussion')),
            ],
        ),
        migrations.AddField(
            model_name='discussion',
            name='lesson_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussion', to='carriculum.lesson'),
        ),
    ]
