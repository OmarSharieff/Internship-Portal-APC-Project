import sqlite3
import os


PATH = os.path.join('database', 'internship_databse.db')

def db_init():
   
    con = sqlite3.connect(PATH)
    cursor = con.cursor()

    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON;")

    # All Tables 
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS internships (
            internship_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            company_id INTEGER,
            deadline TEXT,
            is_open INTEGER DEFAULT 1,
            FOREIGN KEY (company_id) REFERENCES users(user_id)
        );

        CREATE TABLE IF NOT EXISTS applications (
            app_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            internship_id INTEGER,
            status TEXT DEFAULT 'pending',
            applied_at TEXT,
            notes TEXT,
            FOREIGN KEY (student_id) REFERENCES users(user_id),
            FOREIGN KEY (internship_id) REFERENCES internships(internship_id)
        );
    ''')
    
    con.commit()
    con.close()
    print("successfully created the database.")