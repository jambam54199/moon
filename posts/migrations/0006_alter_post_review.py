# Generated by Django 5.1 on 2024-08-28 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_post_movies"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="review",
            field=models.TextField(verbose_name="리뷰"),
        ),
    ]