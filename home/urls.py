
from django.views.generic import TemplateView
from django.urls import path
from home.views import *

urlpatterns = [
    path('login_admin/', LoginPage.as_view(), name = 'login_admin'),
    path('login_faculty/', LoginPage.as_view(), name = 'login_faculty'),
    path('login_student/', LoginPage.as_view(), name = 'login_student'),
    path('', HomPage.as_view(), name = 'home'),
    path('register/', RegisterPage.as_view(), name = 'register'),
    path('faculties/', FacultiesPage.as_view(), name = 'faculties'),
    path('students/', StudentList.as_view(), name = 'students'),
    path('students1/', StudentLis1t1.as_view(), name = 'students1'),
    path('student_attendenct/', StudentAttendence.as_view(), name = 'student_attendenct'),
    path('student_details/', StudentDetails.as_view(), name = 'student_details'),
]

