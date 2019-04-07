from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_show'),
    path('employee/new/', views.employee_new, name='employee_new'),
    path('employee/index/', views.EmployeeListView.as_view(), name='employee_index'),
    path('employee/<int:pk>/shift/new/', views.shift_new, name='shift_new'), #trial number one, without specifying employee pk
    
]