from re import template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# função para mostrar currículo


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "students/student-resume.html"


# função para editar currículo de aluno
class StudentEditView(LoginRequiredMixin, TemplateView):
    template_name = "students/student-edit.html"


# função para criar currículo de aluno
class CreateResumeView(LoginRequiredMixin, TemplateView):
    template_name = "students/create-resume.html"


# função mostrar dashboard do admin
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "admin/dashboard.html"


# função para o admin editar currículo
class AdminEditView(LoginRequiredMixin, TemplateView):
    template_name = "admin/manage-edit.html"