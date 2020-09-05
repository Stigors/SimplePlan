from django.shortcuts import render
from database.connection import completed_list
from date.date import date
import sqlite3


def completed(request):
    tasks_list = completed_list(sqlite3.connect('tasks_db.sqlite'))
    day = date()

    context = {
        'tasks': tasks_list,
        'day': day,
    }
    return render(request, 'completed/completed.html', context)
