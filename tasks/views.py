from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

# INDEX → /tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})


# DETALLE → /tasks/<slug>
def task_detail(request, slug):
    task = get_object_or_404(Task, slug=slug)
    return render(request, 'tasks/details.html', {'task': task})


# CREAR → /tasks/create
def task_create(request):
    if request.method == 'POST':
        # Le pasamos los datos del usuario al formulario
        form = TaskForm(request.POST)
        if form.is_valid(): # Django comprueba que todo esté correcto
            form.save()     # ¡Y lo guarda directamente en la base de datos!
            return redirect('task_list')
    else:
        # Si entra por primera vez, le damos un formulario vacío
        form = TaskForm()

    return render(request, 'tasks/form.html', {'form': form})

# EDITAR /tasks/edit
def task_edit(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        # Le pasamos los datos nuevos, pero le decimos que actualice una instancia existente (task)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        # Si entra por primera vez, llenamos el formulario con los datos de esa tarea
        form = TaskForm(instance=task)

    # Pasamos 'form' (para dibujar los inputs) y 'task' (para saber si el título es Editar o Nuevo)
    return render(request, 'tasks/form.html', {'form': form, 'task': task})

# BORRAR → /tasks/<id>/delete
def task_delete(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/confirm_delete.html', {'task': task})


# CAMBIAR ESTADO → /tasks/<id>/toggle
def task_toggle(request, id):
    task = get_object_or_404(Task, id=id)
    task.completada = not task.completada
    task.save()

    return redirect('task_list')

# TAREAS COMPLETADAS
def tareas_completadas(request):
    # Filtramos donde completada sea True
    tareas = Task.objects.filter(completada=True)
    return render(request, 'tasks/tasksCompleted.html', {'tareas': tareas})

# TAREAAS PDENDIENTES
def tareas_pendientes(request):
    # Filtramos donde completada sea False
    tareas = Task.objects.filter(completada=False)
    return render(request, 'tasks/noCompleted.html', {'tareas': tareas})
