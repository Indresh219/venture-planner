# Generated by Django 4.1.4 on 2023-05-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TravelPlan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(max_length=100)),
                ("lastname", models.CharField(max_length=100)),
                ("destination", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("contact_number", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("budget", models.IntegerField()),
                ("places", models.CharField(max_length=500)),
                ("no_of_adults", models.IntegerField()),
                ("no_of_children", models.IntegerField()),
                ("no_of_events", models.IntegerField()),
                ("booked_before", models.BooleanField()),
                ("find", models.CharField(max_length=100)),
            ],
        ),
    ]
