from django.db import models


class Course(models.Model):
    course_id = models.IntegerField("Course Id", primary_key=True, unique=True, auto_created=True)
    course_name = models.CharField("Course Name", max_length=255)
    quota = models.IntegerField("Quota")
    course_credits = models.IntegerField("Course Credits")


class Preliminary(models.Model):
    preliminary_id = models.IntegerField("Preliminary Id", primary_key=True, unique=True, auto_created=True)
    course = models.ForeignKey(Course, models.CASCADE, related_name='course')
    preface_of = models.ForeignKey(Course, models.CASCADE, related_name='preface')


class Career(models.Model):
    career_id = models.IntegerField("Career Id", primary_key=True, unique=True, auto_created=True)
    career_name = models.CharField("Career Name", max_length=255)
    career_credits = models.IntegerField("Career Credits")


class StudentCourse(models.Model):

    class CourseStatuses(models.TextChoices):
        PASS = 'PASS'
        EXAM = 'EXAM'
        FAIL = 'FAIL'
        STUDYING = 'STUDYING'

    student_course_id = models.IntegerField("Student Course Id", primary_key=True, unique=True, auto_created=True)
    student = models.ForeignKey('person.Student', models.CASCADE)
    course = models.ForeignKey(Course, models.CASCADE)
    course_status = models.CharField(max_length=8, choices=CourseStatuses.choices)

