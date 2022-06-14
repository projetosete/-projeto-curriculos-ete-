from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ("name","birth_date","modality","status","phone_number","city","image","course")
