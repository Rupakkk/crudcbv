from dataclasses import field
from tkinter import Widget
from turtle import textinput
from django import forms
from .models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','age','password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }