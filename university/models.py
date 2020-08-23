from django.core.validators import MaxValueValidator
from django.db import models


# TODO Add Comments

class Course(models.Model):
    course_name = models.CharField("Course Name", max_length=255)
    quota = models.IntegerField("Quota")
    course_credits = models.IntegerField("Course Credits")
    active = models.BooleanField("Active", default=True)


class Preliminary(models.Model):
    course = models.ForeignKey(Course, models.CASCADE, related_name='course')
    preface_of = models.ForeignKey(Course, models.CASCADE, related_name='preface')


class Career(models.Model):
    career_name = models.CharField("Career Name", max_length=255)
    career_credits = models.IntegerField("Career Credits")
    active = models.BooleanField("Active", default=True)


class StudentCourse(models.Model):
    class CourseStatuses(models.TextChoices):
        PASS = 'PASS'
        EXAM = 'EXAM'
        FAIL = 'FAIL'
        STUDYING = 'STUDYING'

    student = models.ForeignKey('person.Student', models.CASCADE)
    course = models.ForeignKey(Course, models.CASCADE)
    score = models.IntegerField("Score", blank=True, null=True, validators=[MaxValueValidator(12)])
    course_status = models.CharField(max_length=8, choices=CourseStatuses.choices, blank=True, null=True)


class StudentCareer(models.Model):
    student = models.ForeignKey('person.Student', models.CASCADE)
    career = models.ForeignKey(Career, models.CASCADE)
    student_career_credits = models.IntegerField("Student Career Credits", default=0)
    active = models.BooleanField("Active", default=True)


class TeacherCourse(models.Model):
    teacher = models.ForeignKey('person.Teacher', models.CASCADE)
    course = models.ForeignKey(Course, models.CASCADE)


class CareerCourse(models.Model):
    career = models.ForeignKey(Career, models.CASCADE)
    course = models.ForeignKey(Course, models.CASCADE)
