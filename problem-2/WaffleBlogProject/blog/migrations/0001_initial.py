# Generated by Django 4.1.1 on 2022-10-02 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("author_name", models.CharField(max_length=50)),
                ("author_email", models.EmailField(max_length=254)),
                ("author_image", models.ImageField(blank=True, upload_to="")),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("reading_duration", models.DurationField(blank=True)),
            ],
        ),
    ]
