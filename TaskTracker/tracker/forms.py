from django import forms
from .models import Department, Task

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'department']
