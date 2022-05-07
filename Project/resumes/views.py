from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm
from .models import Resume
from django.contrib import messages

# Create your views here.

# função para mostrar currículo
@login_required
def home(request):

    resumes = Resume.objects.all().filter(user=request.user)

    if(not resumes):
        return redirect("criar/")

    return render(request, "students/resume.html", {"resumes" : resumes})


# função para criar currículo de aluno
@login_required
def createResume(request):
    resumes = Resume.objects.all().filter(user=request.user)
    
    if(request.method == "POST"):
        form = ResumeForm(request.POST, request.FILES)

        if(form.is_valid()):
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()

            messages.info(request, "Currículo criado com sucesso!")

            return redirect("/")

    else: 
        form = ResumeForm()

    return render(request, "students/create-resume.html", {"form" : form, "resumes" : resumes})


# função para editar currículo de aluno 
@login_required
def editResume(request, id):

    resume = get_object_or_404(Resume, pk=id)
    form = ResumeForm(instance=resume)

    if(request.method == "POST"):
        form = ResumeForm(request.POST, request.FILES, instance=resume)

        if(form.is_valid()):
            resume.save()

            messages.info(request, "Currículo editado com sucesso!")

            return redirect("/")
        
        else: 
            return render(request, "students/edit-resume.html", {"form" : form, "resume" : resume})
             
    else:
        return render(request, "students/edit-resume.html", {"form" : form, "resume" : resume})


# função mostrar dashboard do admin
def dashboard(request):

    return render(request, "admin/dashboard.html")


# função para o admin editar currículo
