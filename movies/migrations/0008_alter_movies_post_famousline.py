# Generated by Django 5.1 on 2024-08-28 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0007_alter_movies_post_famousline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movies_post",
            name="famousline",
            field=models.TextField(blank=True, null=True, verbose_name="명대사"),
        ),
    ]
