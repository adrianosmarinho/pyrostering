from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm, ShiftForm
from .models import Employee
# Create your views here.

class HomePageView(generic.TemplateView):
    """
    A class to handle the home page view
    """

    template_name = "rostering/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['latest_articles'] = Article.objects.all()[:5]
    #     return context

class EmployeeListView(generic.ListView):
    """
    A class to handle the employees index view.
    """

    model = Employee
    template_name = 'rostering/employee_index.html'
    paginate_by = 100  # if pagination is desired


class EmployeeDetailView(generic.DetailView):
    """
    A class to handle the employee show view.
    """
    model = Employee
    template_name = "rostering/employee_show.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context

#TODO: Modify the form handle to use Form classes and Generic Views
def employee_new(request):

    print("employee_new: request.method = ", request.method)

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            #employee.save() #we probably dont need this line
            return redirect('employee_show', pk=employee.pk)
        else:
            # TODO: remove this block
            print("employee_new: form is not valid")
    else:
        form = EmployeeForm()
        context = {'form': form}
        return render(request, 'rostering/employee_edit.html', context)

#TODO: Modify the form handle to use Form classes and Generic Views
def shift_new(request, pk):

    form = ShiftForm(request.POST or None)
       
    if form.is_valid():
        print(form.cleaned_data)
        shift = form.save()
        return redirect('employee_show', pk=pk)
        #this lines work by i have commented to understand validation and get  post
        #shift = form.save(commit = False)
        #employee = Employee.objects.get(pk = pk)
        #shift.employee = employee
        #shift.save()
        #return redirect('employee_show', pk=employee.pk)
        #end of the block that works
    else:
        print("hi the form was not valid, what is wrong? ")
        print(form.errors)
    #old else block
    # else:
    #     form = ShiftForm()
    #     context = {'form': form}
    #     return render(request, 'rostering/shift_edit.html', context)
    #end of old else block. it works
    context = {
        "form": form
    }
    return render(request, 'rostering/shift_edit.html', context)