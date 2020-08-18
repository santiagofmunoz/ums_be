from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_id', 'course_name', 'quota', 'course')


class PreliminarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Preliminary
        fields = ('preliminary_id', 'course', 'preface_of')


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ('career_id', 'career_name', 'credits')


class StudentCourse(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = ('student_course_id', 'student', 'course', 'course_status')
