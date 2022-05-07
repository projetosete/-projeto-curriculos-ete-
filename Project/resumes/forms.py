from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ("name","birth_date","phone_number","city","image","course")
