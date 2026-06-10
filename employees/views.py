from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list.html', {'employees': employees})

@login_required
def add_employee(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        location = request.POST.get('location')

        Employee.objects.create(
            name=name,
            email=email,
            department=department,
            location=location
        )
        return redirect('/list/')

    return render(request, 'employees/add.html')

@login_required
def delete_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    return redirect('/list/')

@login_required
def edit_employee(request, id):
    emp = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        emp.name = request.POST.get('name')
        emp.email = request.POST.get('email')
        emp.department = request.POST.get('department')
        emp.location = request.POST.get('location')
        emp.save()
        return redirect('/list/')

    return render(request, 'employees/edit.html', {'emp': emp})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/list/')
        else:
            return render(request, 'employees/login.html', {'error': 'Invalid credentials'})

    return render(request, 'employees/login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required
def dashboard(request):
    total_employees = Employee.objects.count()
    return render(request, 'employees/dashboard.html', {
        'total_employees': total_employees
    })