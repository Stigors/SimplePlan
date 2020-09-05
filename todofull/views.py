from django.shortcuts import render
from database.connection import todofull_list
from date.date import date
import sqlite3


def todofull(request):
    tasks_list = todofull_list(sqlite3.connect('tasks_db.sqlite'))
    day = date()

    context = {
        'tasks': tasks_list,
        'day': day,
    }
    return render(request, 'todofull/todofull.html', context)