from django import forms
from .models import project

class project_form(forms.ModelForm): 
    class Meta:
        model = project 
        fields = '__all__' 