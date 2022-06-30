from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # create
    path("create/", views.createResume, name="create-resume"),
    path("knowledge/", views.createKnowledge, name="create-knowledge"),
    path("experience/", views.createExperience, name="create-experience"),

    # edit
    path("editar/<int:id>", views.editResume, name="edit-resume"),
    
]