# Generated by Django 4.1.1 on 2022-09-26 07:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_date_post_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 26, 7, 7, 5, 507449, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
