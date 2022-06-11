# Generated by Django 4.0.4 on 2022-06-11 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_faculty_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='user_id',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='user_id',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 6, 11, 22, 23, 9, 598629)),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='date_of_joining',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 6, 11, 22, 23, 9, 598629)),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 6, 11, 22, 23, 9, 599671)),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_joining',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 6, 11, 22, 23, 9, 599671)),
        ),
    ]
