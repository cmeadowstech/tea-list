# Generated by Django 4.1.6 on 2023-02-06 20:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tealist", "0002_alter_vendor_established"),
    ]

    operations = [
        migrations.AddField(
            model_name="vendor",
            name="url",
            field=models.URLField(blank=True, help_text="URL for this vendor's store"),
        ),
    ]
