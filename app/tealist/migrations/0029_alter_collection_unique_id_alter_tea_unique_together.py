# Generated by Django 4.2.9 on 2024-01-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tealist", "0028_tea_alter_collection_unique_id_teavariant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="unique_id",
            field=models.CharField(default="018b", editable=False, max_length=6),
        ),
        migrations.AlterUniqueTogether(
            name="tea",
            unique_together={("vendor", "handle")},
        ),
    ]
