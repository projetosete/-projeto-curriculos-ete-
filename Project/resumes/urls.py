from django.urls import path
from . import views

urlpatterns = [
    # Student
    path("", views.home, name="home"),
    path("editar/<int:id>", views.editResume, name="edit-resume"),

    # create
    path("create/", views.createResume, name="create-resume"),
    path("knowledge/", views.createKnowledge, name="create-knowledge"),
    path("experience/", views.createExperience, name="create-experience"),

    # Admin
    path("dashboard/", views.dashboard, name="dashboard"),
    # path("admistrador/editar/", views.AdminEditView.as_view(), name="admin-edit"),
]
