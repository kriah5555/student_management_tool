from dataclasses import field
from tempfile import tempdir
from webbrowser import get
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib import messages #import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User



class HomPage(TemplateView):
    template_name = "home.html"

class RegisterStudentPage(CreateView):
    template_name = "register.html"
    model         = Student
    fields        = '__all__'
        
    # def get_queryset(self):
    #     return super().get_queryset()
    def get_context_data(self, **kwargs):
        context               = super().get_context_data(**kwargs)
        context["header"]     = 'Register'
        context["button"]     = 'Register'
        context["background"] = '/static/home/images/register_stugent1.jpg'
        return context
    

class UpdateStudent(UpdateView):
    template_name = "register.html"
    model         = Student
    fields        = '__all__'

    def get_context_data(self, **kwargs):
        context               = super().get_context_data(**kwargs)
        context["header"]     = "Update"
        context["button"]     = "Update"
        context["background"] = '/static/home/images/register_stugent1.jpg'
        return context
    

class DeleteStudent(DeleteView):
    template_name = "register.html"
    model         = Student
    success_url   = reverse_lazy('students1')

    def get_context_data(self, **kwargs):
        context               = super().get_context_data(**kwargs)
        context["header"]     = 'Are u shore you want to delete!'
        context["button"]     = 'Delete'
        context["background"] = '/static/home/images/register_stugent1.jpg'
        return context



class FacultiesPage(ListView):
    model         = Faculty
    template_name = "faculties.html"

class StudentList(ListView):
    model         = Student
    template_name = "students.html"

class StudentLis1t1(ListView):
    model         = Student
    template_name = "students1.html"

class StudentAttendenceCredentials(TemplateView):
    template_name = "select_attendence_credentials.html"

class StudentAttendence(ListView):
    model = Student
    template_name = "student_attendence.html"
    

class StudentDetails(DetailView):
    model         = Student
    template_name = "student_details.html"

class FacultytDetails(DetailView):
    model         = Faculty
    template_name = "faculty_details.html"

class RegisterPage(CreateView):
    template_name = "register.html"
    model         = Faculty
    fields        = ['first_name', 'last_name', 'avatars', 'date_of_birth', 'date_of_joining', 'email', 'gender', 'branch']
        
    # def get_queryset(self):
    #     return super().get_queryset()
    def get_context_data(self, **kwargs):
        context               = super().get_context_data(**kwargs)
        context["header"]     = 'Register'
        context["button"]     = 'Register'
        context["background"] = '/static/home/images/regidter.jpg'
        return context
    

class UpdateFaculty(UpdateView):
    template_name = "register.html"
    model         = Faculty
    fields        = ('first_name', 'last_name', 'avatars', 'email', 'gender', 'branch')

    def get_context_data(self, **kwargs):
        context               = super().get_context_data(**kwargs)
        context["header"]     = "Update"
        context["button"]     = "Update"
        context["background"] = '/static/home/images/regidter.jpg'
        return context
    

class DeleteFaculty(DeleteView):
    template_name = "register.html"
    model        = Faculty
    success_url  = reverse_lazy('faculties')

    def get_context_data(self, **kwargs):
        context               = super().get_context_data(**kwargs)
        context["header"]     = 'Are u shore you want to delete!'
        context["button"]     = 'Delete'
        context["background"] = '/static/home/images/regidter.jpg'
        return context

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
        
        user = authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None :
            login(request, user)
            template_name = "faculties.html"
            return redirect('/faculties/')
        else :
            template_name = "login.html"
            context['error'] = 'Please enter valid username and password'
    return render(request, template_name, context)

def create_user(request, pk):
    if request.user.is_authenticated:
        if request.method == 'GET':
            if (request.path == f'/create_faculty_user/{pk}'):
                path = 'create_user.jpg'
                context = {'image' : path, 'obj' : Faculty.objects.all()}
            template_name = 'create_user.html'
            return render(request, template_name, context)
        else:
            faculty = Faculty.objects.get(pk = request.POST['faculty'])
            username = request.POST['username']
            password = request.POST['pwd']
            email    = faculty.email
            if faculty and username and password:
                user = User.objects.create_user(first_name = 'faculty', last_name = faculty.pk, username = username, password = password, email = email)
                user.save()
            elif not username:
                messages.success(request, 'Please enter username')
            elif not password:
                messages.success(request, 'Please enter password')
            elif not faculty:
                messages.success(request, 'Please select faculty')
            messages.success(request, 'Profile details updated.')
            return redirect("/faculties/")
    else:
            return redirect("home")

def lgout(request):
    logout(request)
    return redirect('home')

        




   


            

    
