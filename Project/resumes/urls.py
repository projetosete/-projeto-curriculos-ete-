from django.urls import path
from . import views

urlpatterns = [
    # Student
    path("", views.home, name="home"),
    path("criar/", views.createResume, name="create-resume"),
    path("editar/<int:id>", views.editResume, name="edit-resume"),

    # Admin
    path("dashboard/", views.dashboard, name="dashboard"),
    # path("admistrador/editar/", views.AdminEditView.as_view(), name="admin-edit"),
]
