# Generated by Django 4.1.1 on 2022-10-01 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('authorimage', models.ImageField(default='defaultprofile.png', upload_to='profile/')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('bodyimage', models.ImageField(default='default.jpeg', upload_to='body/')),
                ('published_date', models.DateTimeField(default=datetime.datetime(2022, 10, 1, 19, 20, 10, 396179, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
