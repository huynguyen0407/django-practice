from django import forms
from django.forms import ModelForm, TextInput, widgets

from .models import City

class weatherForms (ModelForm):
    class Meta:
        model = City        
        fields =  ['name_city']
        widgets = {'name_city' :TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}
