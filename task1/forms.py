from django import forms
from django.forms import ModelForm

from .models import *

class TaskForms1 (forms.ModelForm):
    class Meta:
        model = Task1        
        fields = '__all__'
