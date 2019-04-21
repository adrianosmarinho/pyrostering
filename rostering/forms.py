import datetime
from datetime import date, datetime, timedelta
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

    # we need to override break_length
    break_length = forms.IntegerField(label="Break Length")
    # we may also need to override start and end
    # start = forms.TimeField()
    # end = forms.TimeField()

    class Meta:
        model = Shift
        #TODO: there must be a better way of handling the employee than inserting it into a form
        fields = ('employee', 'date', 'start', 'end', 'break_length')

    def clean_break_length(self, *args, **kwargs):
        break_length = self.cleaned_data.get("break_length")
        if break_length > 40:
            return break_length
        else:
            raise forms.ValidationError("This is not a valid break")
            # raise forms.ValidationError(
            #     _('This is not a valid break value: %(value)s'),
            #     code='invalid',
            #     params={'value': break_length},)

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start")
        end = cleaned_data.get("end")

        time_difference = datetime.combine(date.today(), end) - datetime.combine(date.today(), start)
        time_difference_in_hours = time_difference / timedelta(hours=1)

        if (time_difference_in_hours > 10):
            raise forms.ValidationError("You cannot create a shift bigger than 10 hours")