from django.shortcuts import render , redirect

from django.http import HttpResponse

from .forms import TaskForm

from .models import Tasks

# Create your views here.


def hello(request):
    form = TaskForm()
    task = Tasks.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'task':task, 'TaskForm':form}

    return render(request, 'createtask.html', context)



def update_task(request,pk):
    task = Tasks.objects.get(id=pk)

    form  = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'task':task, 'TaskForm':form}
    return render(request, 'update.html', context)


def delete_task(request,pk):
    task = Tasks.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()

        return redirect('/')

    context = {'task':task}
    return render(request, 'delete.html', context)


