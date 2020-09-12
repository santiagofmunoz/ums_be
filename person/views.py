from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


# TODO Add comments

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
# TODO: Optimize this! DRY!
def person_create(request):
    serializer = PersonSerializer(data=request.data)
    person_type = request.data["type"]
    if serializer.is_valid():
        created_person = serializer.save()
        person_pk = created_person.get_pk()
        get_created_person = Person.objects.get(pk=person_pk)
        if person_type == "student":
            Student.objects.create(person=get_created_person)
        elif person_type == "teacher":
            Teacher.objects.create(person=get_created_person)
        elif person_type == "administrative":
            Administrative.objects.create(person=get_created_person)
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
# TODO: Optimize this! DRY!
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
# TODO: Optimize this! DRY!
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
# TODO: Optimize this! DRY!
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
