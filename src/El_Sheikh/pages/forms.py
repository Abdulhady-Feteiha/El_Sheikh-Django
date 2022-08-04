from django import forms
from .models import report_request
from django.forms import ModelForm

class report_request_Form(forms.ModelForm):
    
    class Meta:
        model = report_request
        fields = ('Owner','Month','Year')

