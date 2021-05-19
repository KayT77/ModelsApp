from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import datetime


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length= 50)
    faculty = models.ForeignKey(Faculty, on_delete=CASCADE) 

    def __str__(self):
        return self.name


class Grade(models.Model):
    type = models.CharField(max_length= 50)

    def __str__(self):
        return self.type

class Certificate_type(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length= 50)
    year_of_graduation = models.DateField()
    department = models.ForeignKey(Department, on_delete=CASCADE)
    grade = models.ForeignKey(Grade, on_delete=CASCADE)
    school = models.ForeignKey(School,on_delete=CASCADE)
    certificate_type  = models.ForeignKey(Certificate_type, on_delete=CASCADE)

    def __str__(self):
        return self.full_name