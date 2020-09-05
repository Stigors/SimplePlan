from django.shortcuts import render
from database.connection import deleted_list
from date.date import date
import sqlite3


def deleted(request):
    tasks_list = deleted_list(sqlite3.connect('tasks_db.sqlite'))
    day = date()

    context = {
        'tasks': tasks_list,
        'day': day,
    }
    return render(request, 'deleted/deleted.html', context)
