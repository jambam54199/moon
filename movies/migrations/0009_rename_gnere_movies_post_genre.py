# Generated by Django 5.1 on 2024-08-28 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0008_alter_movies_post_famousline"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movies_post",
            old_name="gnere",
            new_name="genre",
        ),
    ]
