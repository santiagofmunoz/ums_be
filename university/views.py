from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


# TODO Add comments


@api_view(['GET', 'PUT'])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def career_create(request):
    serializer = CareerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def career_detail(request, pk):
    try:
        career = Career.objects.get(pk=pk)
    except Career.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CareerSerializer(career)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CareerSerializer(career, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def student_career_detail(request, pk):
    try:
        student_career = StudentCareer.objects.get(pk=pk)
    except StudentCareer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentCareerSerializer(student_career)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentCareerSerializer(student_career, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def preliminary_detail(request, pk):
    try:
        preliminary = Preliminary.objects.get(pk=pk)
    except Preliminary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PreliminarySerializer(preliminary)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PreliminarySerializer(preliminary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        preliminary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def teacher_course_detail(request, pk):
    try:
        teacher_course = TeacherCourse.objects.get(pk=pk)
    except TeacherCourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeacherCourseSerializer(teacher_course)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeacherCourseSerializer(teacher_course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        teacher_course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def career_course_detail(request, pk):
    try:
        career_course = CareerCourse.objects.get(pk=pk)
    except CareerCourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CareerCourseSerializer(career_course)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CareerCourseSerializer(career_course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        career_course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# TODO: Optimize this! DRY!
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO: Optimize this! DRY!
@api_view(['GET', 'POST'])
def preliminary_list(request):
    if request.method == 'GET':
        preliminaries = Preliminary.objects.all()
        serializer = PreliminarySerializer(preliminaries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PreliminarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO: Optimize this! DRY!
@api_view(['GET', 'POST'])
def career_list(request):
    if request.method == 'GET':
        careers = Career.objects.all()
        serializer = CareerSerializer(careers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CareerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO: Optimize this! DRY!
@api_view(['GET', 'POST'])
def student_course_list(request):
    if request.method == 'GET':
        student_course = StudentCourse.objects.all()
        serializer = StudentCourseSerializer(student_course, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_course_detail(request, pk):
    try:
        student_course = StudentCourse.objects.get(pk=pk)
    except StudentCourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentCourseSerializer(student_course)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentCourseSerializer(student_course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student_course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# TODO: Optimize this! DRY!
@api_view(['GET', 'POST'])
def student_career_list(request):
    if request.method == 'GET':
        student_career = StudentCareer.objects.all()
        serializer = StudentCareerSerializer(student_career, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentCareerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO: Optimize this! DRY!
@api_view(['GET', 'POST'])
def teacher_course_list(request):
    if request.method == 'GET':
        teacher_course = TeacherCourse.objects.all()
        serializer = TeacherCourseSerializer(teacher_course, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeacherCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO: Optimize this! DRY!
@api_view(['GET', 'POST'])
def career_course_list(request):
    if request.method == 'GET':
        career_course = CareerCourse.objects.all()
        serializer = CareerCourseSerializer(career_course, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CareerCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_unenrols_course(request):
    try:
        student_course = StudentCourse.objects.get(request.data['student_course_pk'])
    except StudentCourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    student_course.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
