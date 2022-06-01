# Generated by Django 4.0.4 on 2022-05-14 22:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0006_remove_faculty_user_remove_student_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('avatars', models.ImageField(default='default_faculty.jpg', upload_to='faculties')),
                ('date_of_birth', models.DateField(blank=True, default=datetime.datetime(2022, 5, 15, 3, 59, 36, 437868))),
                ('date_of_joining', models.DateField(blank=True, default=datetime.datetime(2022, 5, 15, 3, 59, 36, 437868))),
                ('email', models.EmailField(default='email', max_length=30)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ], default='MALE', max_length=30)),
                ('branch', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('usn', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('avatars', models.ImageField(default='default_student.jpg', upload_to='students')),
                ('date_of_birth', models.DateField(blank=True, default=datetime.datetime(2022, 5, 15, 3, 59, 36, 439863))),
                ('date_of_joining', models.DateField(blank=True, default=datetime.datetime(2022, 5, 15, 3, 59, 36, 439863))),
                ('email', models.EmailField(default='email', max_length=30)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ], default='MALE', max_length=10)),
                ('branch', models.CharField(choices=[(1, 'E & C'), (2, 'MECHANICAL'), (3, 'COMPUTER SCIENCE')], max_length=30)),
                ('division', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ], max_length=30)),
                ('sem', models.IntegerField(choices=[(1, '1 SEM'), (2, '2 SEM'), (3, '3 SEM'), (4, '4 SEM'), (5, '5 SEM'), (6, '1 SEM'), (7, '1 SEM'), (8, '1 SEM')])),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_name', models.CharField(default='add first name', max_length=30)),
                ('sem', models.IntegerField(choices=[(1, '1 SEM'), (2, '2 SEM'), (3, '3 SEM'), (4, '4 SEM'), (5, '5 SEM'), (6, '1 SEM'), (7, '1 SEM'), (8, '1 SEM')])),
            ],
        ),
    ]
