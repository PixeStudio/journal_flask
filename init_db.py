import sqlite3

DB = 'projects.db'

def init_db():
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXIST projects_snapshot (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project TEXT UNIQUE,
            last_update TEXT,
            tasks_done TEXT,
            tasks_todo TEXT,
            meta_notes TEXT,
            plan TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXIST projects_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project TEXT UNIQUE,
            update_date TEXT,
            tasks_done TEXT,
            tasks_todo TEXT,
            meta_notes TEXT,
            plan TEXT,
            note TEXT
        )
    ''')

    print("Databse initialized.")

if __name__ == '__main__':
    init_db()





    



