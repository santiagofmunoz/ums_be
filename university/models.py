from django.db import models


class Course(models.Model):
    courseId = models.IntegerField("Course Id", primary_key=True, unique=True, auto_created=True)
    courseName = models.CharField("Course Name", max_length=255)
    quota = models.IntegerField("Quota")


class Preliminary(models.Model):
    preliminaryId = models.IntegerField("Preliminary Id", primary_key=True, unique=True, auto_created=True)
    courseId = models.ForeignKey(Course, models.CASCADE, related_name='course')
    prefaceOf = models.ForeignKey(Course, models.CASCADE, related_name='preface')


class Career(models.Model):
    careerId = models.IntegerField("Career Id", primary_key=True, unique=True, auto_created=True)
    careerName = models.CharField("Career Name", max_length=255)
    credits = models.IntegerField("Credits")
