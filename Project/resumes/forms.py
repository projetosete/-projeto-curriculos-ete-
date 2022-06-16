from django import forms
from .models import Resume, Knowledge, Experience


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ("name","birth_date","modality","status","phone_number","city","image","course")


class KnowledgeForm(forms.ModelForm):

    class Meta:
        model = Knowledge
        fields = ("dominant_skills","english","spanish","basics_skills")


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ("company","office","start_date","final_date","description")