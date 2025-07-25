from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

def get_db_connection():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')

def index():
    conn = get_db_connection()
    projects = conn.execute('SELECT * FROM projects_snapshot').fetchall()
    conn.close()
    return render_template('index.html', projects=projects)

@app.route('/add', methods=('GET', 'POST'))

def add():
    if request.method == 'POST':
        project = request.form['project']
        tasks_done = request.form['tasks_done']
        tasks_todo = request.form['tasks_todo']
        meta_notes = request.form['meta_notes']
        plan = request.form['plan']
        note = request.form('note')
        now = datetime.now().strftime('%Y-%m-%d')
        conn = get_db_connection()

        # update snapshot

        conn.execute('''
        INSERT INTO projects_snapshot (project, update_date, tasks_done, tasks_todo, meta_notes, plan)
        VALUES (?,?,?,?,?,?)
        ON CONFLICT(project) DO UPDATE SET 
        last_update=excluded.last_update,
        tasks_done=excluded.tasks_done,
        tasks_todo=excluded.tasks_todo,
        meta_notes=excluded.meta_notes,
        plan=excluded.plan
        ''', (project, now, tasks_done, tasks_todo, meta_notes,plan))

