# Generated by Django 4.2.1 on 2023-07-22 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_rename_no_of_visitors_travelplan_no_of_adults'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travelplan',
            old_name='no_of_adults',
            new_name='no_of_visitors',
        ),
    ]
