from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

# Create your models here.

class Employee(models.Model):
    """
    A class to represent the Employees of our rostering application
    ...

    Attributes
    ----------
    first_name : CharField(200)
        The first name of the employee. It cannot be blank.
    last_name : CharField(200)
        The last name of the employee. It cannot be blank.
    """
    first_name = models.CharField(max_length=200)
    last_name  = models.CharField(max_length=200)

    #TODO: Verify if form validation will handle this override of save useless
    def save(self, *args, **kwargs):
        """
        It only saves if the names are not blank
        """
        if (len(self.first_name) != 0) and (len(self.last_name) != 0):
            super().save(*args, **kwargs)  # Call the "real" save() method.


class Shift(models.Model):
    employee     = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date         = models.DateField(unique = True)
    start        = models.TimeField()
    end          = models.TimeField()
    break_length = models.IntegerField()

    def clean(self):
        
        # An employee cannot work more than 5 days in a row
        # first, computes how many shifts an employee has
        max_shifts_in_a_row = 5
        all_shifts = self.employee.shift_set.all()
        total_shifts = len(all_shifts)
        offset = total_shifts - max_shifts_in_a_row
        
        # then, if it is more than 5, check for the errors
        if ((offset) >= 0):
            last_five_shifts = all_shifts[offset:]
            
            # a flag for consecutive shifts, it will be false if any of the last_five_shifts are not consecutive
            consecutive = True
            
            for i in range(max_shifts_in_a_row - 1):
                if ((last_five_shifts[i+1].date - last_five_shifts[i].date).days > 1):
                    consecutive = False
                    break

            # An employee cannot work more than 5 days in the same week (7-day window)
            # a flag for working in a week for more than 5 days, it will be false if any of the last_five_shifts is after the threshold
            worked_more_than_five_days_on_a_week = True
            initial_date = datetime(last_five_shifts[0].date.year, last_five_shifts[0].date.month, last_five_shifts[0].date.day)
            threshold_date = initial_date + timedelta(days = 7)
            for i in range(1, max_shifts_in_a_row):
                if (datetime(last_five_shifts[i].date.year, last_five_shifts[i].date.month, last_five_shifts[i].date.day) >= threshold_date):
                    worked_more_than_five_days_on_a_week = False

            #at this point, we already have 5 consecutive shifts in the table, so cannot add another consecutive one
            if (consecutive):
                if ((self.date - last_five_shifts[max_shifts_in_a_row - 1].date).days) == 1:
                    raise ValidationError(_('An employee cannot work more than five shifts in a row'))

            #at this point, we have 5 shifts in a 7-day windows, so cannot add another shift to that window
            if (worked_more_than_five_days_on_a_week):
                if (datetime(self.date.year, self.date.month, self.date.day ) < threshold_date):
                     raise ValidationError(_('An employee cannot work more than five shifts in a 7-day window'))

        
        