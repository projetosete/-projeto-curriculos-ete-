from django.contrib import admin
from .models import Experience, Resume

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

