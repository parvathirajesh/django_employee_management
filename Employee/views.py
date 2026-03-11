from django.shortcuts import render,redirect
from django.views import View

from Employee.models import Employee

from Employee.form import EmployeeForm


# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'home.html')

class CreateEmployee(View):
    def get(self, request):
        form_instance = EmployeeForm()
        context = {'form': form_instance}
        return render(request, 'create.html',context)
    def post(self,request):
        form_instance = EmployeeForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
        return render(request,'create.html')

class ReadEmployee(View):
    def get(self, request):
        e=Employee.objects.all()
        context = {'employee': e}
        return render(request, 'read.html',context)


