from rest_framework import serializers
from .models import *


# TODO Add comments

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('pk', 'course_name', 'quota', 'course_credits')


class PreliminarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Preliminary
        fields = ('pk', 'course', 'preface_of')


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ('pk', 'career_name', 'career_credits')


class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = ('pk', 'student', 'course', 'score', 'course_status')


class StudentCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCareer
        fields = ('pk', 'student', 'career', 'student_career_credits')


class TeacherCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherCourse
        fields = ('pk', 'teacher', 'course')


class CareerCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerCourse
        fields = ('pk', 'career', 'course')
