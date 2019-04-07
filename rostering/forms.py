from django import forms
from .models import Employee, Shift

class EmployeeForm(forms.ModelForm):
    """
    A class to represent a form for a new Employee
   
    """

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name')

class ShiftForm(forms.ModelForm):
    """
    A class to represent a form for a new Employee
   
    """

    class Meta:
        model = Shift
        fields = ('date', 'start', 'end', 'break_length')