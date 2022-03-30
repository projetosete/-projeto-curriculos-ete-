from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    # Student
    path("student/resume/", views.studentResume, name="student-resume"),
    path("student/edit/", views.studentEdit, name="student-edit"),
    path("create/resume/", views.createResume, name="create-resume"),

    # Admin
    path("dashboard/", views.dashboard, name="dashboard"),
    path("manage/edit/", views.manageEdit, name="manage-edit"),
]
