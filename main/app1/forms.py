from django import forms
from .models import Employee

class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class Form(forms.Form):
    dep_choices = [('1', 'IT'), ('2', 'Admin'), ('3', 'HR')]
    file= forms.FileField()   
    agree = forms.BooleanField() #  creates checkbox
    date_of_birth = forms.DateField(widget = forms.NumberInput(attrs={'type':'date'})) # add calendar
    department = forms.ChoiceField(choices=dep_choices) # creates dropdown
    department_new = forms.ChoiceField(widget = forms.RadioSelect, choices=dep_choices) #creates radio button
     