# Generated by Django 4.2.9 on 2024-01-12 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tealist", "0032_alter_collection_unique_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="unique_id",
            field=models.CharField(default="5d3e", editable=False, max_length=6),
        ),
        migrations.AlterField(
            model_name="teavariant",
            name="tea",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tea_variant",
                to="tealist.tea",
            ),
        ),
    ]
