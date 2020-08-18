from django.db import models

from university.models import Course, Career


class Person(models.Model):
    personId = models.IntegerField("Person Id", primary_key=True, unique=True, auto_created=True)
    ci = models.IntegerField("CI", unique=True)
    password = models.CharField("Password", max_length=255)
    first_name = models.CharField("First Name", max_length=255)
    last_name = models.CharField("Last Name", max_length=255)
    phone = models.IntegerField("Phone")
    email = models.EmailField("Email")
    address = models.TextField("Address")
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    active = models.BooleanField("Active")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Teacher(models.Model):
    teacherId = models.IntegerField("Teacher Id", primary_key=True, unique=True, auto_created=True)
    personId = models.ForeignKey(Person, models.CASCADE)
    courseId = models.ForeignKey(Course, models.CASCADE)


class Student(models.Model):
    studentId = models.IntegerField("Student Id", primary_key=True, unique=True, auto_created=True)
    personId = models.ForeignKey(Person, models.CASCADE)
    careerId = models.ForeignKey(Career, models.CASCADE)


class Administrative(models.Model):
    administrativeId = models.IntegerField("Administrative Id", primary_key=True, unique=True, auto_created=True)
    personId = models.ForeignKey(Person, models.CASCADE)
