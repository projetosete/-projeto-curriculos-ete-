from django.contrib import admin
from .models import Experience, Resume, Knowledge

# Register your models here.

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    # colunas que irá mostrar na tabela
    list_display = ("name","course","city","phone_number","user","created_at","updated_at")

    # barra de pesquisa
    search_fields = ["name","course","city","phone_number"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    # colunas que irá mostrar na tabela
    list_display = ("company","office","start_date","final_date","description","resumes")

    # barra de pesquisa
    search_fields = ["company","office"]

@admin.register(Knowledge)
class KnowledgeAdmin(admin.ModelAdmin):
    # colunas que irá mostrar na tabela
    list_display = ("dominant_skills","english","spanish","basics_skills")

    # barra de pesquisa
    search_fields = ["dominant_skills","english","spanish","basics_skills"]

