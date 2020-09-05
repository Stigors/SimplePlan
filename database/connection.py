import sqlite3
import pandas as pd
from date.date import date

day = date()


def connect_db():
    conn = sqlite3.connect('tasks_db.sqlite')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks_db(
    task_id INTEGER PRIMARY KEY,
    task_description VARCHAR(20) NOT NULL,
    task_deadline VARCHAR(20) NOT NULL,
    task_type VARCHAR(20) NOT NULL,
    task_status VARCHAR(20) NOT NULL);
    ''')


def todo_list(connection):
    tasks_frame = pd.read_sql_query("""
    SELECT * FROM tasks_db 
    WHERE task_status = "To do" AND task_deadline <= date("now", "+3 hours")
    """, connection)
    tasks_frame.rename(columns={'task_id': 'ID', 'task_description': 'Task description', 'task_deadline': 'Deadline',
                                'task_status': 'Status'}, inplace=True)
    tasks_html = tasks_frame.to_html(columns=('ID', 'Task description', 'Deadline', 'Status'), index=False)
    return tasks_html

def completed_list(connection):
    tasks_frame = pd.read_sql_query("""
    SELECT * FROM tasks_db 
    WHERE task_status = "Done"
    """, connection)
    tasks_frame.rename(columns={'task_id': 'ID', 'task_description': 'Task description', 'task_deadline': 'Deadline',
                                'task_status': 'Status'}, inplace=True)
    tasks_html = tasks_frame.to_html(columns=('ID', 'Task description', 'Deadline', 'Status'), index=False)
    return tasks_html

def deleted_list(connection):
    tasks_frame = pd.read_sql_query("""
    SELECT * FROM tasks_db 
    WHERE task_status = "Deleted"
    """, connection)
    tasks_frame.rename(columns={'task_id': 'ID', 'task_description': 'Task description', 'task_deadline': 'Deadline',
                                'task_status': 'Status'}, inplace=True)
    tasks_html = tasks_frame.to_html(columns=('ID', 'Task description', 'Deadline', 'Status'), index=False)
    return tasks_html

def add_task(task_description_value, deadline):
    connection = sqlite3.connect('tasks_db.sqlite')
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO tasks_db(task_description, task_deadline, task_type, task_status)
    VALUES (?, ?, "Home", "To do")
    """, (task_description_value, deadline))
    connection.commit()
    return db_to_html(connection)


def complete_task(task_id_i):
    conn = sqlite3.connect('tasks_db.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE tasks_db
    SET task_status = "Done"
    WHERE task_id = ?
    """, (task_id_i,))
    conn.commit()
    return db_to_html(conn)


def delete_task(task_id_i):
    conn = sqlite3.connect('tasks_db.sqlite')
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE tasks_db
    SET task_status = "Deleted"
    WHERE task_id = ?
    """, (task_id_i,))
    conn.commit()
    return db_to_html(conn)


connect_db()
