import sqlite3

def connection():
    
    conn = sqlite3.connect('yojaync.db')
    print("Opened database successfully")
    return conn

def create_event_table():
    
    conn = connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS events
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             date TEXT NOT NULL,
             time TEXT NOT NULL,
             location TEXT NOT NULL,
             description TEXT NOT NULL);''')
    conn.commit()
    conn.close()

def insert_event(name, date, time, location, description):
    
    conn = connection()
    conn.execute("INSERT INTO events (name, date, time, location, description) VALUES (?, ?, ?, ?, ?)",
                 (name, date, time, location, description))
    conn.commit()
    conn.close()

def get_all_events():
    
    conn = connection()
    cursor = conn.execute("SELECT * FROM events")
    events = cursor.fetchall()
    conn.close()
    return events
