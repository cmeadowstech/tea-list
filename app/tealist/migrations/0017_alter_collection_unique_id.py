# Generated by Django 4.1.6 on 2023-11-13 18:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tealist", "0016_alter_collection_unique_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="unique_id",
            field=models.CharField(default="ea6c", editable=False, max_length=6),
        ),
    ]
