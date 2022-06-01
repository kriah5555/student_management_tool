# Generated by Django 4.0.4 on 2022-05-14 22:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_faculty_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 15, 4, 8, 2, 124666)),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='date_of_joining',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 15, 4, 8, 2, 124666)),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 15, 4, 8, 2, 125667)),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_joining',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 15, 4, 8, 2, 125667)),
        ),
    ]
