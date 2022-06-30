from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from resumes.forms import ResumeForm, KnowledgeForm, ExperienceForm
from resumes.models import Resume, Knowledge, Experience
from django.contrib import messages

# Create your views here.

# função para mostrar currículo
@login_required
def home(request):

    resumes = Resume.objects.filter(user=request.user)
    knowledges = Knowledge.objects.filter(resume_knowledge=resumes.first())
    experiences = Experience.objects.filter(resume_experience=resumes.first())

    #group_admin = get_object_or_404(Group, name="Admin")


    if(not resumes):
        return redirect("create-resume")

    return render(request, "home.html", {"resumes" : resumes, "knowledges" : knowledges, "experiences" : experiences})






# ____________________________________ CREATE ____________________________________
# função para criar currículo de aluno
@login_required
def createResume(request):
    resumes = Resume.objects.filter(user=request.user)
    
    if(request.method == "POST"):
        form = ResumeForm(request.POST, request.FILES)

        if(form.is_valid()):
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()

            messages.info(request, "Currículo criado com sucesso!")

            return redirect("create-knowledge")

    else: 
        form = ResumeForm()

    return render(request, "create/resume.html", {"form" : form, "resumes" : resumes})


#def encontrar_jobs(request):
#    if request.method == "GET":
#        preco_minimo = request.GET.get('preco_minimo')
#        preco_maximo = request.GET.get('preco_maximo')

@login_required
def createKnowledge(request):
    resumes = Resume.objects.filter(user=request.user)
    
    if(request.method == "POST"):
        form = KnowledgeForm(request.POST, request.FILES)

        if(form.is_valid()):
            knowledge = form.save(commit=False)
            knowledge.resume_knowledge = resumes.first()
            knowledge.save()

            messages.info(request, "Habilidade salva com sucesso!")

            return redirect("create-experience")

    else: 
        form = KnowledgeForm()

    return render(request, "create/knowledge.html", {"form" : form})


@login_required
def createExperience(request):
    resumes = Resume.objects.filter(user=request.user)
    
    if(request.method == "POST"):
        form = ExperienceForm(request.POST, request.FILES)

        if(form.is_valid()):
            experience = form.save(commit=False)
            experience.resume_experience = resumes.first()
            experience.save()

            messages.info(request, "Currículo criado com sucesso!")

            return redirect("/")

    else: 
        form = ExperienceForm()

    return render(request, "create/experience.html", {"form" : form})





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

