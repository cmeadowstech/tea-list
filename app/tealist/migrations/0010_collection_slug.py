# Generated by Django 4.1.6 on 2023-03-20 22:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tealist", "0009_collection_rating_alter_collection_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="collection",
            name="slug",
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]
