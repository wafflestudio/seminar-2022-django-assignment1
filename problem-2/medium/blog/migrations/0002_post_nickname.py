# Generated by Django 4.1.1 on 2022-10-01 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="nickname",
            field=models.CharField(max_length=50, null="True"),
            preserve_default="True",
        ),
    ]