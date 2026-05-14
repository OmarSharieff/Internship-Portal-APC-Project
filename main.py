from database.db_setup import init_db
from database.db_helper import (
    insert_user,
    insert_internship,
    fetch_internships
)

from ui.login_screen import Login


def seed_data():

    try:
        student_id = insert_user(
            "Sepideh Mahmoodi",
            "sepideh.mahmoodi.ghaem@vub.be",
            "SepidehVUB",
            "student"
        )

        print(f"Student created: {student_id}")

    except Exception as e:
        print(f"Student exists: {e}")

    try:
        company_id = insert_user(
            "Toyota",
            "toyota.recruit@toyota.be",
            "Toyotarecruit",
            "company"
        )

        print(f"Company created: {company_id}")

    except Exception as e:

        print(f"Company exists: {e}")

        company_id = 2

    try:

        internship_id = insert_internship(
            "ML Engineer Intern",
            "Develop data-driven solutions",
            company_id,
            "2026-05-01"
        )

        print(f"Internship created: {internship_id}")

    except Exception as e:

        print(f"Internship exists: {e}")

    internships = fetch_internships()

    print(f"\nTotal internships: {len(internships)}")

    for internship in internships:

        print(
            f"ID: {internship[0]}, "
            f"Title: {internship[1]}, "
            f"Deadline: {internship[4]}"
        )


def main():

    init_db()

    seed_data()

    app = Login()

    app.root.mainloop()


if __name__ == "__main__":
    main()