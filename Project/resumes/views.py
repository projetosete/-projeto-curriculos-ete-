from django.shortcuts import render

# Create your views here.

# função para mostrar currículo
def studentResume(request):
    return render(request, "students/student-resume.html")

# função para editar currículo de aluno
def studentEdit(request):
    return render(request, "students/student-edit.html")

# função para criar currículo de aluno
def createResume(request):
    return render(request, "students/create-resume.html")

# função mostrar dashboard do admin
def dashboard(request):
    return render(request, "manager/dashboard.html")

# função para o admin editar currículo
def manageEdit(request):
    return render(request, "manager/manage-edit.html")



