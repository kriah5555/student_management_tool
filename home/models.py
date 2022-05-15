from __future__ import division
from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User
from django.urls import reverse

"""
pip install pillow
pip install django-rest_framework
"""
GENDER_CHOUCE = (('MALE','MALE'), ('FEMALE','FEMALE'), ('GAY','GAY'))
BRANCH_CHOUCE = (('E & C','E & C'), ('MECHANICAL','MECHANICAL'), ('COMPUTER SCIENCE','COMPUTER SCIENCE'))
SEM_CHOUCE    = ((1,'1 SEM'), (2,'2 SEM'), (3,'3 SEM'), (4,'4 SEM'), (5,'5 SEM'), (6,'1 SEM'), (7,'1 SEM'), (8,'1 SEM'),)

class Faculty(models.Model):
    fid             = models.AutoField(primary_key=True)
    # username        = models.CharField(max_length=30)
    # password        = models.CharField(max_length=30)
    first_name      = models.CharField(max_length = 30, default='')
    last_name       = models.CharField(max_length = 30, default='')
    avatars         = models.ImageField(upload_to='faculties/', default = 'default_faculty.jpg')
    date_of_birth   = models.DateField(default=datetime.now(), blank=True)
    date_of_joining = models.DateField(default=datetime.now(), blank=True)
    email           = models.EmailField(max_length = 30, default='email',)
    gender          = models.CharField(max_length = 30, default = 'MALE', choices = GENDER_CHOUCE)
    branch          = models.CharField(max_length = 30,  choices = BRANCH_CHOUCE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse("faculties")
    


class Student(models.Model):
    usn             = models.AutoField(primary_key=True)
    first_name      = models.CharField(max_length = 30, default='')
    # username        = models.CharField(max_length=30)
    # password        = models.CharField(max_length=30)
    last_name       = models.CharField(max_length = 30, default='')
    avatars         = models.ImageField(upload_to='students/', default = 'default_student.jpg')
    date_of_birth   = models.DateField(default=datetime.now(), blank=True)
    date_of_joining = models.DateField(default=datetime.now(), blank=True)
    email           = models.EmailField(max_length = 30, default='email',)
    gender          = models.CharField(max_length = 10, default = 'MALE', choices = GENDER_CHOUCE)
    branch          = models.CharField(max_length = 30, choices = BRANCH_CHOUCE)
    division        = models.CharField(max_length = 30, choices = GENDER_CHOUCE)
    sem             = models.IntegerField( choices = SEM_CHOUCE)



class Subject(models.Model):
    id       = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length = 30, default='add first name')
    sem      = models.IntegerField( choices = SEM_CHOUCE)
