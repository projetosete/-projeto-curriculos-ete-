from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from resumes.forms import ResumeForm, KnowledgeForm, ExperienceForm
from resumes.models import Resume, Knowledge, Experience
from django.contrib import messages



# função mostrar dashboard do admin
def dashboard(request):

    return render(request, "dashboard.html")