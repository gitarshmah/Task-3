from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Task
from .forms import DepartmentForm, TaskForm

# Create your views here.

def index(request):
    departments = Department.objects.all()
    department_form = DepartmentForm(request.POST or None)
    task_form = TaskForm(request.POST or None)

    if request.method == "POST":
        if "add_department" in request.POST and department_form.is_valid():
            department_form.save()
            return redirect('index')

        elif "add_task" in request.POST and task_form.is_valid():
            task_form.save()
            return redirect('index')

        elif "toggle_task" in request.POST:
            task_id = request.POST.get("task_id")
            task = get_object_or_404(Task, id=task_id)
            task.completed = not task.completed
            task.save()
            return redirect('index')

    return render(request, 'index.html', {
        'departments': departments,
        'department_form': department_form,
        'task_form': task_form,
    })
