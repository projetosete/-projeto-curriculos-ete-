from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    # Student
    path("", views.IndexView.as_view(), name="index"),
    path("aluno/aditar/", views.StudentEditView.as_view(), name="student-edit"),
    path("criar/cirriculo/", views.CreateResumeView.as_view(), name="create-resume"),

    # Admin
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("admistrador/editar/", views.AdminEditView.as_view(), name="admin-edit"),
]
