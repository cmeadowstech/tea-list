# Generated by Django 4.2.9 on 2024-01-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tealist", "0024_alter_collection_unique_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="unique_id",
            field=models.CharField(default="943a", editable=False, max_length=6),
        ),
        migrations.AlterField(
            model_name="rating",
            name="value",
            field=models.FloatField(
                choices=[
                    (5, "5"),
                    (4.5, "4.5"),
                    (4, "4"),
                    (3.5, "3.5"),
                    (3, "3"),
                    (2.5, "2.5"),
                    (2, "2"),
                    (1.5, "1.5"),
                    (1, "1"),
                    (0.5, "0.5"),
                ]
            ),
        ),
    ]
