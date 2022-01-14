from django.shortcuts import redirect, render

from .models import *
from .forms import TaskForms1

# Create your views here.
def index(request):
    task1 = Task1.objects.all()

    forms1 = TaskForms1()

    if request.method == 'POST':
        forms1 = TaskForms1(request.POST)
        if forms1.is_valid():
            forms1.save()
        return redirect('/task1/')
    
    context = {'task1': task1, 'forms1': forms1}
    return render(request, "task1/index1.html", context)

def updateTask(request, pk):
    task = Task1.objects.get(id = pk)
    form = TaskForms1(instance=task)

    if request.method == 'POST':
        form = TaskForms1(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/task1/')

    context = {'form': form, 'task': task}
    return render(request, 'task1/update_task1.html', context)

def deleteTask(request, pk):
    item = Task1.objects.get(id = pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/task1/')

    context = {'item': item}
    return render(request, 'task1/delete.html', context)