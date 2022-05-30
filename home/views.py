from dataclasses import field
from pickle import TRUE
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
from django.core.mail import send_mail



class HomPage(TemplateView):
    template_name = "home1.html"
    # template_name = "home.html"

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

    def post(self, request, *args, **kwargs):
        request.session['subject']  = request.POST['subject']
        request.session['sem']      = request.POST['sem']
        request.session['branch']   = request.POST['branch']
        request.session['division'] = request.POST['division']
        request.session['sdate']    = request.POST['sdate']
        request.session['stime']    = request.POST['stime']
        request.session['etime']    = request.POST['etime']
        return redirect('student_attendenct')

class StudentAttendence(ListView):
    model         = Student
    template_name = "student_attendence.html"
    success_url = reverse_lazy('faculties')

def student_attendence(request):
    if request.method == 'GET':
        context = {
            'students' : Student.objects.filter(branch = request.session['branch'], division = request.session['division'], sem = request.session['sem']),
            'subject'  : request.session['subject'],
            'sem'      : request.session['sem'],
            'branch'   : request.session['branch'],
            'division' : request.session['division'],
            'sdate'    : request.session['sdate'],
            'stime'    : request.session['stime'],
            'etime'    : request.session['etime'],
        }
        return render(request, 'student_attendence.html', context)
    else:
        students   = Student.objects.filter(branch = request.session['branch'], division = request.session['division'], sem = request.session['sem'])
        # attendence = StudentAttendences.objects.create()
        for stu in students:
            print(stu.student_usn,'------------///////////')

        print(request.POST,'======---------------   ')
        return redirect('faculties')




    

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
    # send_mail(
    # 'Subject here',
    # 'Here is the message.',
    # 'ka36l1107@gmail.com',
    # ['sunilgangadhar.infanion@gmail.com'],
    # # fail_silently=False,
    # )
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

        if (request.path == '/login_admin/'):
           first_name = ''
           next       = '/faculties/'
        elif (request.path == '/login_faculty/'):
            first_name = 'faculty'
            next       = '/students1/'
        elif (request.path == '/login_student/'):
            first_name = 'student'
        user = authenticate(username = request.POST['username'], password = request.POST['password'], first_name = first_name)
        if user is not None :
            login(request, user)
            print(request.user.last_name,'==============')
            if  (request.path == '/login_student/'):
                next = '/student_details/'+request.user.last_name
            return redirect(next)
        else :
            template_name = "login.html"
            context['error'] = 'Please enter valid username and password'
    return render(request, template_name, context)

def create_user(request, pk):
    if request.user.is_authenticated:
        if request.method == 'GET':
            if (request.path == f'/create_faculty_user/{pk}'):
                path = 'create_user.jpg'
                context = {'image' : path, 'obj' : Faculty.objects.get(pk = pk, status = 0)}
            elif (request.path == f'/create_student_user/{pk}'):
                path = 'create_user.jpg'
                context = {'image' : path, 'obj' : Student.objects.get(pk = pk, status = 0)}
            template_name = 'create_user.html'
            return render(request, template_name, context)
        else:
            if (request.path == f'/create_faculty_user/{pk}'):
                faculty = Faculty.objects.get(pk = pk)
                email     = faculty.email
                first_name = 'faculty'
            elif (request.path == f'/create_student_user/{pk}'):
                faculty    = Student.objects.get(pk = pk)
                email      = faculty.email
                first_anme = 'student'
            username = request.POST['username']
            password = request.POST['pwd']
            if faculty and username and password:
                user = User.objects.create_user(first_name = first_anme, last_name = faculty.pk, username = username, password = password, email = email, is_staff = True)
                user.save()
                faculty.status = TRUE
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

        




   


            

    
