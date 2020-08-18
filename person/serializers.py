from rest_framework import serializers
from person.models import *


# Serializers allow complex data such as query sets and model instances to be converted to native Python datatypes
# that can then be easily rendered into JSON, XML or other content types.

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'person_id',
            'ci',
            'password',
            'first_name',
            'last_name',
            'phone',
            'email',
            'address',
            'created_at',
            'active',
        )


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('teacher_id', 'person', 'course')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('student_id', 'person', 'career')


class AdministrativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrative
        fields = ('administrative_id', 'person')
