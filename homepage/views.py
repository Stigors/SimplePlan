from django.shortcuts import render
from database.connection import todo_list
from database.connection import add_task
from database.connection import complete_task
from database.connection import delete_task
from date.date import date
import sqlite3


def index(request):
    tasks_list = todo_list(sqlite3.connect('tasks_db.sqlite'))
    day = date()

    if request.method == 'POST':
        if 'task' in request.POST:
            task_description_value = request.POST['task']
            deadline = request.POST['deadline']
            tasks_list = add_task(task_description_value, deadline)
        if "Complete" in request.POST:
            task_complete = int(request.POST['task_change'])
            tasks_list = complete_task(task_complete)
        if "Delete" in request.POST:
            task_delete = int(request.POST['task_delete'])
            tasks_list = delete_task(task_delete)

    context = {
        'tasks': tasks_list,
        'day': day,
    }
    return render(request, 'homepage/index.html', context)
