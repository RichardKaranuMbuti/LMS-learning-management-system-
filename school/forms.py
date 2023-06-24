from django import forms
from .models import Department, Unit

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['code', 'name', 'description']

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['department', 'code', 'name', 'description']
