from django.db import models


# TODO Add comments

class Person(models.Model):
    ci = models.IntegerField("CI", unique=True)
    password = models.CharField("Password", max_length=255)
    first_name = models.CharField("First Name", max_length=255)
    last_name = models.CharField("Last Name", max_length=255)
    phone = models.IntegerField("Phone")
    email = models.EmailField("Email")
    address = models.TextField("Address")
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    active = models.BooleanField("Active", default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_pk(self):
        return self.pk


class Teacher(models.Model):
    person = models.OneToOneField(Person, models.CASCADE)


class Student(models.Model):
    person = models.OneToOneField(Person, models.CASCADE)


class Administrative(models.Model):
    person = models.OneToOneField(Person, models.CASCADE)
