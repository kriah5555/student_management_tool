# Generated by Django 4.0.4 on 2022-05-24 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_faculty_created_date_student_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_usn',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='avatars',
            field=models.ImageField(blank=True, null=True, upload_to='faculties/'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 25, 3, 14, 16, 772769)),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='date_of_joining',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 25, 3, 14, 16, 772769)),
        ),
        migrations.AlterField(
            model_name='student',
            name='avatars',
            field=models.ImageField(blank=True, null=True, upload_to='students/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 25, 3, 14, 16, 772769)),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_joining',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 25, 3, 14, 16, 772769)),
        ),
        migrations.AlterField(
            model_name='student',
            name='division',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=30),
        ),
    ]
