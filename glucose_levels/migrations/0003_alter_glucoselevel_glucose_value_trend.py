# Generated by Django 5.2 on 2025-05-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("glucose_levels", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="glucoselevel",
            name="glucose_value_trend",
            field=models.IntegerField(blank=True, db_comment="mg/dL", null=True),
        ),
    ]
