# Generated by Django 5.1 on 2024-08-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_rename_country_movies_post_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movies_post",
            name="year",
            field=models.CharField(max_length=10, verbose_name="개봉년도"),
        ),
    ]
