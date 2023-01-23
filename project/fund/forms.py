from django import forms
from .models import fund

class fund_form(forms.ModelForm): 
    class Meta:
        model = fund 
        fields = '__all__'