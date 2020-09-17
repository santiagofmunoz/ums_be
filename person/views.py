from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


# TODO Add comments

def associate_person_student_teacher_administrative(person_type, person_obj):
    if person_type == "student":
        Student.objects.create(person=person_obj)
    elif person_type == "teacher":
        Teacher.objects.create(person=person_obj)
    elif person_type == "administrative":
        Administrative.objects.create(person=person_obj)

@api_view(['GET', 'PUT'])
def person_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def person_create(request):
    serializer = PersonSerializer(data=request.data)
    person_type = request.data["type"]
    if serializer.is_valid():
        created_person = serializer.save()
        person_pk = created_person.get_pk()
        get_created_person = Person.objects.get(pk=person_pk)
        associate_person_student_teacher_administrative(person_type, get_created_person)
        return Response(status=status.HTTP_201_CREATED)
    if serializer.errors["ci"] == ["person with this CI already exists."]:
        person_ci = request.data["ci"]
        get_person = Person.objects.get(ci=person_ci)
        associate_person_student_teacher_administrative(person_type, get_person)
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def teacher_list(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def administrative_list(request):
    if request.method == 'GET':
        administratives = Administrative.objects.all()
        serializer = AdministrativeSerializer(administratives, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdministrativeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
