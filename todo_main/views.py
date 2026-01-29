from django.shortcuts import render
from todo.models import Task
def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')

    compleated_tasks = Task.objects.filter(is_completed=True)
    context = {
        'tasks': tasks,
        'compleated_tasks': compleated_tasks,
    } 
    return render(request, 'home.html', context)