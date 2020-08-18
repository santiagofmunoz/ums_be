from django.db import models


class Person(models.Model):
    person_id = models.IntegerField("Person Id", primary_key=True, unique=True, auto_created=True)
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
    teacher_id = models.IntegerField("Teacher Id", primary_key=True, unique=True, auto_created=True)
    person = models.ForeignKey(Person, models.CASCADE)
    course = models.ForeignKey('university.Course', models.CASCADE)


class Student(models.Model):
    student_id = models.IntegerField("Student Id", primary_key=True, unique=True, auto_created=True)
    person = models.ForeignKey(Person, models.CASCADE)
    career = models.ForeignKey('university.Career', models.CASCADE)


class Administrative(models.Model):
    administrative_id = models.IntegerField("Administrative Id", primary_key=True, unique=True, auto_created=True)
    person = models.ForeignKey(Person, models.CASCADE)
