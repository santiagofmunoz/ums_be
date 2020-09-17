from django.contrib import admin
from django.urls import path
from person import views as person_views
from university import views as university_views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),

    # PERSON

    url(r'api/person/create/$', person_views.person_create),
    url(r'api/person/(?P<pk>[0-9]+)$', person_views.person_detail),
    url(r'api/person/teacher/$', person_views.teacher_list),
    url(r'api/person/student/$', person_views.student_list),
    url(r'api/person/administrative/$', person_views.administrative_list),

    # UNIVERSITY

    url(r'api/university/course/$', university_views.course_list),
    url(r'api/university/course/(?P<pk>[0-9]+)$', university_views.course_detail),
    url(r'api/university/career/create', university_views.career_create),
    url(r'api/university/career/$', university_views.career_list),
    url(r'api/university/career/(?P<pk>[0-9]+)$', university_views.career_detail),
    url(r'api/university/preliminary/$', university_views.preliminary_list),
    url(r'api/university/preliminary/(?P<pk>[0-9]+)$', university_views.preliminary_detail),
    url(r'api/university/student_course/$', university_views.student_course_list),
    url(r'api/university/student_course/(?P<pk>[0-9]+)$', university_views.student_course_detail),
    url(r'api/university/student_career/$', university_views.student_career_list),
    url(r'api/university/student_career/(?P<pk>[0-9]+)$', university_views.student_career_detail),
    url(r'api/university/teacher_course/$', university_views.teacher_course_list),
    url(r'api/university/teacher_course/(?P<pk>[0-9]+)$', university_views.teacher_course_detail),
    url(r'api/university/career_course/$', university_views.career_course_list),
    url(r'api/university/career_course/(?P<pk>[0-9]+)$', university_views.career_course_detail),
]
