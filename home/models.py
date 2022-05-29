from __future__ import division
from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

"""
pip install pillow
pip install django-rest_framework
"""
GENDER_CHOUCE   = (('MALE','MALE'), ('FEMALE','FEMALE'), ('GAY','GAY'))
SUBJECT_CHOUCE  = (('MALE','MALE'), ('FEMALE','FEMALE'), ('GAY','GAY'))
BRANCH_CHOUCE   = (('E & C','E & C'), ('MECHANICAL','MECHANICAL'), ('COMPUTER SCIENCE','COMPUTER SCIENCE'))
SEM_CHOUCE      = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8),)
DIVISION_CHOUCE = (('A', 'A'), ('B', 'B'), ('C', 'C'))

class Faculty(models.Model):
    fid             = models.AutoField(primary_key=True)
    first_name      = models.CharField(max_length = 30, default='')
    last_name       = models.CharField(max_length = 30, default='')
    avatars         = models.ImageField(upload_to='faculties/', null = True, blank = True)
    date_of_birth   = models.DateField(default=datetime.now(), blank = True)
    date_of_joining = models.DateField(default=datetime.now(), blank = True)
    email           = models.EmailField(max_length = 30, default = 'email',)
    gender          = models.CharField(max_length = 30, default = 'MALE', choices = GENDER_CHOUCE)
    branch          = models.CharField(max_length = 30,  choices = BRANCH_CHOUCE)
    created_date    = models.DateField(auto_now_add = True)
    status          = models.BooleanField(default = 0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse("faculties")
        # return reverse("faculties", args = (str(self.id)))
    


class Student(models.Model):
    usn             = models.AutoField(primary_key=True)
    student_usn     = models.CharField(max_length = 30, unique = True)
    first_name      = models.CharField(max_length = 30, default='')
    last_name       = models.CharField(max_length = 30, default='')
    avatars         = models.ImageField(upload_to='students/', null = True, blank = True)
    date_of_birth   = models.DateField(default=datetime.now(), blank=True)
    date_of_joining = models.DateField(default=datetime.now(), blank=True)
    email           = models.EmailField(max_length = 30, default='email',)
    gender          = models.CharField(max_length = 10, default = 'MALE', choices = GENDER_CHOUCE)
    branch          = models.CharField(max_length = 30, choices = BRANCH_CHOUCE)
    division        = models.CharField(max_length = 30, choices = DIVISION_CHOUCE)
    sem             = models.IntegerField(choices = SEM_CHOUCE)
    created_date    = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse("students1")



class Subject(models.Model):
    id       = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length = 30, default='add first name')
    sem      = models.IntegerField( choices = SEM_CHOUCE)

class StudentAttendences(models.Model):
    id          = models.AutoField(primary_key=True)
    student_usn = models.CharField(max_length = 30, unique = True)
    status      = models.BooleanField()
    branch      = models.CharField(max_length = 30, choices = BRANCH_CHOUCE)
    division    = models.CharField(max_length = 30, choices = DIVISION_CHOUCE)
    subject     = models.CharField(max_length = 30, choices = SUBJECT_CHOUCE)
    sem         = models.IntegerField(choices = SEM_CHOUCE)
    

    def __str__(self):
        return self.student_usn + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse("students1")
