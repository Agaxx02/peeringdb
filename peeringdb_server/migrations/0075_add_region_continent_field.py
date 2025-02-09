# Generated by Django 3.2.7 on 2021-09-21 15:50

import django.core.validators
import django_inet.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0074_facility_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="facility",
            name="region_continent",
            field=models.CharField(
                blank=True,
                choices=[
                    ("North America", "North America"),
                    ("Asia Pacific", "Asia Pacific"),
                    ("Europe", "Europe"),
                    ("South America", "South America"),
                    ("Africa", "Africa"),
                    ("Australia", "Australia"),
                    ("Middle East", "Middle East"),
                ],
                max_length=255,
                null=True,
                verbose_name="Continental Region",
            ),
        ),
    ]
