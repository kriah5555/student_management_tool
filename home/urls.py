
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
]

