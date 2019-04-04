from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_show'),
    path('employee/new/', views.employee_new, name='employee_new'),
    path('employee/index/', views.EmployeeListView.as_view(), name='employee_index')
]