# Generated by Django 4.0.4 on 2022-05-25 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import userinfo.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=200)),
                ('profilepic', models.ImageField(blank=True, upload_to=userinfo.models.renameprofile, verbose_name='Profile Picture')),
                ('usertype', models.CharField(choices=[('teacher', 'teacher'), ('student', 'student'), ('parent', 'parent')], default='student', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]