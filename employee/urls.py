from django.urls import path

from employee.views import (
    EmployeeCreateView, EmployeeListView, EmployeeUpdateView, EmployeeDetailView,
    EmployeeDeleteView, BeneficiaryCreateView, BeneficiaryDeleteView, BeneficiaryDetailView, BeneficiaryUpdateView)

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
    path('employee/list', EmployeeListView.as_view(), name='list_employee'),
    path('employee/create', EmployeeCreateView.as_view(), name='create_employee'),
    path('employee/detail/<int:pk>', EmployeeDetailView.as_view(), name='detail_employee'),
    path('employee/update/<int:pk>', EmployeeUpdateView.as_view(), name='update_employee'),
    path('employee/delete/<int:pk>', EmployeeDeleteView.as_view(), name='delete_employee'),

    path('beneficiary/create/<int:pk>', BeneficiaryCreateView.as_view(), name='create_beneficiary'),
    path('beneficiary/delete/<int:pk>', BeneficiaryDeleteView.as_view(), name='delete_beneficiary'),
    path('beneficiary/detail/<int:pk>', BeneficiaryDetailView.as_view(), name='detail_beneficiary'),
    path('beneficiary/update/<int:pk>', BeneficiaryUpdateView.as_view(), name='update_beneficiary'),

]
