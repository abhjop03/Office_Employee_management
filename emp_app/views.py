from django.shortcuts import render
from . models import Employee
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')
def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        dept = int(request.POST['dept'])
        sal = int(request.POST['sal'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name = first_name, last_name = last_name, sal=sal, role_id = role, dept_id = dept, bonus=bonus,email=email, hire_date= datetime.now())
        new_emp.save()
        return render(request, 'add_emp.html')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An error occurred")
    

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        dept = request.POST['dept']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains = name))
        elif role:
            emps = emps.filter(role__role_name__icontains = role)
        elif dept:
            emps = emps.filter(dept__Dep_name__icontains = dept)
        context ={
            'emps': emps
            }
        return render(request, 'view_all_emp.html', context )
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("An error occurred")

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_remove = Employee.objects.get(id=emp_id)
            emp_remove.delete()
            return HttpResponse("Employee deleted")
        except:
            return HttpResponse("An error occurred")


    
    emps = Employee.objects.all()
    context ={
        'emps': emps
        }
    return render(request, 'remove_emp.html', context)
    

def view_all_emp(request):
    emps = Employee.objects.all()
    context ={
        'emps': emps
        }
    print(context)
    return render(request, 'view_all_emp.html', context)
    