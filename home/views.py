from django.shortcuts import render
from django.views.generic import TemplateView

class LoginPage(TemplateView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        if (self.request.path == '/login_admin/'):
            path = 'register1.jpg'
            form = 'Admin'
        elif (self.request.path == '/login_faculty/'):
            path = 'home_background.jpg'
            form = 'Faculty'
        elif (self.request.path == '/login_student/'):
            path = 'students.jpg'
            form = 'Student'
        context = super().get_context_data(**kwargs)
        context['image'] = path
        context['form']  = form
        return context

class HomPage(TemplateView):
    template_name = "home.html"

class RegisterPage(TemplateView):
    template_name = "register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = 'regidter.jpg'
        return context

        FacultiesPage
class FacultiesPage(TemplateView):
    template_name = "faculties.html"