from django.db import models

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
    last_name = models.CharField(max_length=200)

    #TODO: Verify if form validation will render this override of save useless
    def save(self, *args, **kwargs):
        """
        It only saves if the names are not blank
        """
        if (len(self.first_name) != 0) and (len(self.last_name) != 0):
            super().save(*args, **kwargs)  # Call the "real" save() method.

#TODO: Update here with the Shift model
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)