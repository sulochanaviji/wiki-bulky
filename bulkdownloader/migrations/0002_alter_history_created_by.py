# Generated by Django 4.1.7 on 2023-02-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bulkdownloader", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="history",
            name="created_by",
            field=models.CharField(max_length=500, null=True),
        ),
    ]
