# Internship-Portal-APC-Project

A desktop application built with **Python + Tkinter + SQLite** that connects students, companies, and instructors through a structured internship management system.

> **Academic Project** · Object-Oriented Programming · Python 3 · Tkinter · SQLite

---

## ✨ Features

### 👨‍🎓 Student
- Browse all available internship listings
- Apply to internships (duplicate application prevention)
- Track application status in real time (`Pending → Under Review → Approved / Rejected`)
- View personal application history

### 🏢 Company
- Post new internship listings
- Review incoming applications
- Approve or reject applicants with optional notes
- Manage all active postings

### 👨‍🏫 Instructor
- Monitor all student applications across the portal
- View status breakdowns per student
- Generate overview reports
- Track internship outcomes

---

## 🗂️ Project Structure

```
internship-portal/
│
├── main.py                  # Entry point — launches the Tkinter app
│
├── models/                  # OOP class definitions
│   ├── user.py              # Abstract base class: User
│   ├── student.py           # Student (inherits User)
│   ├── company.py           # Company (inherits User)
│   ├── instructor.py        # Instructor (inherits User)
│   ├── internship.py        # Internship entity class
│   └── application.py       # Application entity class
│
├── database/                # Database layer
│   ├── db_setup.py          # Table creation & schema init
│   └── db_helper.py         # CRUD operations (insert, fetch, update)
│
├── ui/                      # Tkinter screens
│   ├── login_screen.py      # Role selection + login
│   ├── student_dashboard.py # Student UI
│   ├── company_dashboard.py # Company UI
│   └── instructor_dashboard.py # Instructor UI
│
└── internship_portal.db     # SQLite database (auto-created on first run)
```

---

## 🧱 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Language | Python 3 | Core logic and scripting |
| UI | Tkinter | Desktop GUI (built-in, no install needed) |
| Database | SQLite3 | Lightweight local database |
| OOP Design | Classes + Inheritance | Student, Company, Instructor all extend User |
| Data Access | `sqlite3` module | Raw SQL queries via Python |

---

## 🗃️ Database Schema

```sql
-- Users table (all roles)
CREATE TABLE users (
    user_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    email       TEXT UNIQUE NOT NULL,
    password    TEXT NOT NULL,
    role        TEXT NOT NULL  -- 'student' | 'company' | 'instructor'
);

-- Internships posted by companies
CREATE TABLE internships (
    internship_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    title           TEXT NOT NULL,
    description     TEXT,
    company_id      INTEGER,
    deadline        TEXT,
    is_open         INTEGER DEFAULT 1,  -- 1 = open, 0 = closed
    FOREIGN KEY (company_id) REFERENCES users(user_id)
);

-- Applications submitted by students
CREATE TABLE applications (
    app_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id      INTEGER,
    internship_id   INTEGER,
    status          TEXT DEFAULT 'pending',  -- pending | under_review | approved | rejected
    applied_at      TEXT,
    notes           TEXT,
    FOREIGN KEY (student_id)    REFERENCES users(user_id),
    FOREIGN KEY (internship_id) REFERENCES internships(internship_id)
);
```

---

## 🔷 UML Class Diagram

### Class Hierarchy

```
User  (abstract base class)
 ├── Student
 ├── Company
 └── Instructor
```

### Full Class Diagram

```
┌─────────────────────────────────────┐
│           «abstract» User           │
├─────────────────────────────────────┤
│ # _user_id  : int                   │
│ # _name     : str                   │
│ # _email    : str                   │
│ # _password : str                   │
├─────────────────────────────────────┤
│ + login(email, password) : bool     │
└──────────────┬──────────────────────┘
               │ inherits
       ┌───────┼──────────────┐
       ▼       ▼              ▼
┌──────────────────┐  ┌──────────────────────┐  ┌──────────────────────┐
│     Student      │  │       Company        │  │      Instructor      │
├──────────────────┤  ├──────────────────────┤  ├──────────────────────┤
│ – _university    │  │ – _industry          │  │ – _department        │
│ – _gpa           │  │ – _location          │  │ – _courses : list    │
│ – _resume        │  ├──────────────────────┤  ├──────────────────────┤
├──────────────────┤  │ + post_intern()      │  │ + view_all_apps()    │
│ + view_intern()  │  │ + view_apps()        │  │ + monitor_students() │
│ + apply()        │  │ + approve()          │  │ + generate_report()  │
│ + view_apps()    │  │ + reject()           │  └──────────────────────┘
└────────┬─────────┘  └──────────┬───────────┘
         │ applies               │ posts
         ▼                       ▼
┌──────────────────────┐   ┌─────────────────────────┐
│     Application      │◆──│       Internship         │
├──────────────────────┤   ├─────────────────────────┤
│ – _app_id            │   │ – _internship_id         │
│ – _student_id (FK)   │   │ – _title                 │
│ – _internship_id (FK)│   │ – _description           │
│ – _status            │   │ – _company_id (FK)       │
│ – _applied_at        │   │ – _deadline              │
│ – _notes             │   │ – _is_open : bool        │
├──────────────────────┤   ├─────────────────────────┤
│ + update_status()    │   │ + get_details()          │
│ + get_approved()     │   │ + close()                │
└──────────────────────┘   └─────────────────────────┘
```

> **Note on the diagram:** `Student`, `Company`, and `Instructor` do **not** have
> their own `_id` fields. They all inherit `_user_id` from `User`. The `_name`
> attribute also comes from `User` — `Company` does not have a separate
> `_company_name` field.

### Application Status Flow

```
Student applies
      │
      ▼
  [Pending]
      │
      ▼
[Under Review]  ← Company opens application
      │
   ┌──┴──┐
   ▼     ▼
[Approved] [Rejected]
```

---

## 🧠 OOP Concepts Applied

| Concept | Where It's Used |
|---|---|
| **Inheritance** | `Student`, `Company`, `Instructor` all extend the `User` base class |
| **Encapsulation** | All attributes are protected (`self._name`), accessed via methods |
| **Abstraction** | `User` is never instantiated directly — only subclasses are used (`ABC`) |
| **Composition** | An `Application` cannot exist without a linked `Internship` |
| **List Comprehensions** | Filtering open internships, student apps, company apps |
| **`filter()` + `map()`** | Used in `Instructor` to build per-student status reports |
| **`reduce()`** | Used in `Instructor.generate_report()` to total application count |
| **`any()`** | Used in `Student.apply()` and `Company.post_intern()` for duplicate checks |

---

## 🚀 How to Run

**Requirements:** Python 3.8+ (no external packages needed)

```bash
# Clone the repo
git clone https://github.com/OmarSharieff/Internship-Portal-APC-Project.git
cd Internship-Portal-APC-Project

# Run the app
python main.py
```

The SQLite database will be created automatically on first launch.

---

## 🧪 Edge Cases Handled

- Student cannot apply to the same internship twice (checked at both model and database layers)
- Empty internship listings handled gracefully
- Invalid login credentials show error messages
- Applications cannot be submitted after a deadline
- Instructor view is read-only (cannot modify data)
- Company can action multiple applications per session without the window closing
- Approve/Reject buttons are hidden for applications already actioned

---

## 📸 UI Screens

| Screen | Description |
|---|---|
| Login / Role Select | Choose role and authenticate |
| Student Dashboard | Browse internships, apply, track status |
| Company Dashboard | Post listings, review and action applications |
| Instructor Dashboard | Monitor all students and application outcomes |

---

## 📄 License

This project was developed as part of an academic assignment. All rights reserved.