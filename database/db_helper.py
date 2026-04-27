import sqlite3
from database.db_setup import PATH

def db_connection():
    con = sqlite3.connect(PATH)
    con.execute("PRAGMA foreign_keys = ON;")
    return con


def execute_query(query, params=(), commit=False, fetchall=False):
    con = db_connection()
    cursor = con.cursor()
    
    try:
        cursor.execute(query, params)
        
        if commit:
            con.commit()
            
        if fetchall:
            return cursor.fetchall()
        # Returns new id if we INSERT 
        return cursor.lastrowid 
        
    finally:
        con.close()


def insert_user(name, email, password, role):
    query = "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)"
    return execute_query(query, (name, email, password, role), commit=True)

def delete_user(user_id):
    query = "DELETE FROM users WHERE user_id = ?"
    execute_query(query, (user_id,), commit=True)

def insert_internship(title, description, company_id, deadline):
    query = "INSERT INTO internships (title, description, company_id, deadline) VALUES (?, ?, ?, ?)"
    return execute_query(query, (title, description, company_id, deadline), commit=True)

def fetch_internships():
    query = "SELECT * FROM internships"
    return execute_query(query, fetchall=True)

def delete_internship(internship_id):
    query = "DELETE FROM internships WHERE internship_id = ?"
    execute_query(query, (internship_id,), commit=True)


def update_status(app_id, new_status):
    query = "UPDATE applications SET status = ? WHERE app_id = ?"
    execute_query(query, (new_status, app_id), commit=True)