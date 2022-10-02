# Generated by Django 4.1.1 on 2022-10-01 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_description_post_content_post_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='example@example.com', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=50),
            preserve_default=False,
        ),
    ]