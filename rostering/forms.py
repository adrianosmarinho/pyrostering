from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    """
    A class to represent a form for a new Employee
   
    """

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name')