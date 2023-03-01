from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, TemplateView

from employee.models import Employee, Beneficiary


class HomePageView(TemplateView):
    template_name = 'home.html'


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employee/list-employee.html'
    context_object_name = 'employees'


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employee/detail-employee.html'
    context_object_name = 'employee'


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    template_name = 'employee/create-employee.html'
    fields = ('identifier', 'full_name', 'salary', 'job', 'status', 'date_hire', 'image')
    success_url = reverse_lazy('list_employee')


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    template_name = 'employee/update-employee.html'
    fields = ('identifier', 'full_name', 'salary', 'job', 'status', 'date_hire')

    def get_success_url(self):
        return reverse_lazy('list_employee')


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'employee/delete-employee.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('list_employee')


class BeneficiaryCreateView(LoginRequiredMixin, CreateView):
    model = Beneficiary
    template_name = 'beneficiary/create-beneficiary.html'
    fields = ('identifier', 'full_name', 'relationship', 'birthday', 'gender')
    success_url = reverse_lazy('list_employee')

    def form_valid(self, form):
        beneficiary = form.save(commit=False)
        beneficiary.employee_id = self.kwargs['pk']
        return super(BeneficiaryCreateView, self).form_valid(form)


class BeneficiaryDeleteView(LoginRequiredMixin, DeleteView):
    model = Beneficiary
    template_name = 'beneficiary/delete-beneficiary.html'
    context_object_name = 'beneficiary'
    success_url = reverse_lazy('list_employee')


class BeneficiaryDetailView(LoginRequiredMixin, DetailView):
    model = Beneficiary
    template_name = 'beneficiary/detail-beneficiary.html'
    context_object_name = 'beneficiary'


class BeneficiaryUpdateView(LoginRequiredMixin, UpdateView):
    model = Beneficiary
    template_name = 'beneficiary/update-beneficiary.html'
    fields = ('identifier', 'full_name', 'relationship', 'birthday', 'gender')

    def get_success_url(self):
        return reverse_lazy('list_employee')
