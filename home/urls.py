
from django.views.generic import TemplateView
from django.urls import path
from home.views import *
from home import views as v

urlpatterns = [
    path('login_admin/', v.login_page, name = 'login_admin'),
    # path('login_admin/', LoginPage.as_view(), name = 'login_admin'),
    path('login_faculty/', v.login_page, name = 'login_faculty'),
    # path('login_faculty/', LoginPage.as_view(), name = 'login_faculty'),
    path('login_student/', v.login_page, name = 'login_student'),
    # path('login_student/', LoginPage.as_view(), name = 'login_student'),
    path('', HomPage.as_view(), name = 'home'),
    # path('register/', register_faculty, name = 'register'),
    path('register/', RegisterPage.as_view(), name = 'register'),
    path('register_student/', RegisterStudentPage.as_view(), name = 'register_student'),
    path('update_faculty/<int:pk>', UpdateFaculty.as_view(), name = 'update_faculty'),
    path('update_student/<int:pk>', UpdateStudent.as_view(), name = 'update_student'),
    path('delete_faculty/<int:pk>', DeleteFaculty.as_view(), name = 'delete_faculty'),
    path('delete_student/<int:pk>', DeleteStudent.as_view(), name = 'delete_faculty'),
    path('faculties/', FacultiesPage.as_view(), name = 'faculties'),
    path('students/', StudentList.as_view(), name = 'students'),
    path('students1/', StudentLis1t1.as_view(), name = 'students1'),
    path('student_attendenct/', StudentAttendence.as_view(), name = 'student_attendenct'),
    path('student_details/', StudentDetails.as_view(), name = 'student_details'),
]

