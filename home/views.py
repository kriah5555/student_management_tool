from dataclasses import field
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth import authenticate
from .models import *
from django.contrib import messages
from .serializer import *
from django.urls import reverse, reverse_lazy

user = object()
# class LoginPage(TemplateView):
#     template_name = "login.html"

#     def get_context_data(self, **kwargs):
#         if (self.request.path == '/login_admin/'):
#             path = 'register1.jpg'
#             form = 'Admin'
#         elif (self.request.path == '/login_faculty/'):
#             path = 'home_background.jpg'
#             form = 'Faculty'
#         elif (self.request.path == '/login_student/'):
#             path = 'students.jpg'
#             form = 'Student'
#         context = super().get_context_data(**kwargs)
#         context['image'] = path
#         context['form']  = form
#         return context

class HomPage(TemplateView):
    template_name = "home.html"

class RegisterPage(CreateView):
    template_name = "register.html"
    # success_url = reverse_lazy("faculties")
    model = Faculty
    fields = '__all__'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['image'] = 'regidter.jpg'
    #     return context
        
    def get_queryset(self):
        return super().get_queryset()

class FacultiesPage(TemplateView):
    template_name = "faculties.html"

class StudentList(TemplateView):
    template_name = "students.html"

class StudentLis1t1(TemplateView):
    template_name = "students1.html"

class StudentAttendence(TemplateView):
    template_name = "student_attendence.html"

class StudentDetails(TemplateView):
    template_name = "student_details.html"

def login_page(request):
    if (request.path == '/login_admin/'):
        path = 'register1.jpg'
        form = 'Admin'
    elif (request.path == '/login_faculty/'):
        path = 'home_background.jpg'
        form = 'Faculty'
    elif (request.path == '/login_student/'):
        path = 'students.jpg'
        form = 'Student'
    context = {'image' : path, 'form' : form}
    if request.method == 'GET':
        template_name = "login.html"
    elif (request.method == 'POST'):
        global user
        user = authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None :
            template_name = "faculties.html"
            return redirect('/faculties/')
        else :
            template_name = "login.html"
            context['error'] = 'Please enter username and password'
    return render(request, template_name, context)

def register_faculty(request):
    context = {'image' : 'regidter.jpg'}
    if request.method == 'GET':
        template_name = "register.html"
    elif request.method == 'POST':
        first_name      = request.POST['f_name']
        last_name       = request.POST['l_name']
        date_of_birth   = request.POST['dob']
        date_of_joining = request.POST['doj']
        email           = request.POST['email']
        gender          = request.POST['gender']
        branch          = request.POST['branch']

        f = Faculty()
        f.first_name      = first_name
        f.last_name       = last_name
        f.date_of_birth   = date_of_birth
        f.date_of_joining = date_of_joining
        f.email           = email
        f.gender          = gender
        f.branch          = branch
        if request.FILES != 0:
            print(request.FILES,'--------')
            f.avatars = request.FILES['avatar']
        f.save()
        messages.success(request, f'Faculty {first_name} sdded successfully!')
            
        return redirect('/faculties/')

    return render(request, template_name, context)
    
    # @login_required(login_url='/accounts/login/')
