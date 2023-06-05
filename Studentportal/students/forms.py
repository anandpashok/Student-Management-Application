from django import forms
from students.models import Student

class StudentDetailForm(forms.ModelForm):
   class Meta:
       model= Student
       exclude = ['marks']