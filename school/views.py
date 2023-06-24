from django.shortcuts import render

from .forms import DepartmentForm, UnitForm

def create_department(request):
    form = DepartmentForm()
    return render(request, 'create_department.html', {'form': form})

def create_unit(request):
    form = UnitForm()
    return render(request, 'create_unit.html', {'form': form})
