import sqlite3
from database.db_setup import PATH


def db_connection():

    con = sqlite3.connect(PATH)
    con.execute("PRAGMA foreign_keys = ON;")

    return con


def execute_query(query, params=(), fetch=False, commit=False):

    con = db_connection()
    cursor = con.cursor()

    try:

        cursor.execute(query, params)

        if commit:
            con.commit()

        if fetch:
            return cursor.fetchall()

        return cursor.lastrowid

    finally:

        con.close()


# =========================
# USER FUNCTIONS
# =========================

def insert_user(name, email, password, role):

    query = """
    INSERT INTO users (name, email, password, role)
    VALUES (?, ?, ?, ?)
    """

    return execute_query(
        query,
        (name, email, password, role),
        commit=True
    )


def fetch_user(email, password):

    query = """
    SELECT * FROM users
    WHERE email = ? AND password = ?
    """

    users = execute_query(
        query,
        (email, password),
        fetch=True
    )

    return users[0] if users else None


# =========================
# INTERNSHIP FUNCTIONS
# =========================

def insert_internship(title, description, company_id, deadline):

    query = """
    INSERT INTO internships
    (title, description, company_id, deadline)
    VALUES (?, ?, ?, ?)
    """

    return execute_query(
        query,
        (title, description, company_id, deadline),
        commit=True
    )


def fetch_internships():

    query = """
    SELECT * FROM internships
    """

    return execute_query(query, fetch=True)


# =========================
# APPLICATION FUNCTIONS
# =========================

def insert_application(student_id, internship_id):

    query = """
    INSERT INTO applications
    (student_id, internship_id, applied_at)
    VALUES (?, ?, date('now'))
    """

    return execute_query(
        query,
        (student_id, internship_id),
        commit=True
    )


def fetch_student_applications(student_id):

    query = """
    SELECT applications.app_id,
           internships.title,
           applications.status,
           applications.applied_at
    FROM applications
    JOIN internships
    ON applications.internship_id = internships.internship_id
    WHERE applications.student_id = ?
    """

    return execute_query(
        query,
        (student_id,),
        fetch=True
    )


def fetch_company_applications(company_id):

    query = """
    SELECT applications.app_id,
           users.name,
           internships.title,
           applications.status
    FROM applications
    JOIN internships
    ON applications.internship_id = internships.internship_id
    JOIN users
    ON applications.student_id = users.user_id
    WHERE internships.company_id = ?
    """

    return execute_query(
        query,
        (company_id,),
        fetch=True
    )


def update_application_status(app_id, status):

    query = """
    UPDATE applications
    SET status = ?
    WHERE app_id = ?
    """

    execute_query(
        query,
        (status, app_id),
        commit=True
    )