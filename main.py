from database.db_setup import db_init
from database.db_helper import insert_user, fetch_internships, insert_internship

def main():
    db_init()
    
    print("Test the App")
    
    # Add a user 
    try:
        user_id = insert_user("Sepideh mahmoodi", "sepideh.mahmoodi.ghaem@vub.be", "SepidehVUB", "student")
        print(f"User created with ID: {user_id}")
    except Exception as e:
        print(f"This User already exists: {e}")

    try:
      company_id = insert_user("Toyota", "toyota.recruit@toyota.be", "Toyotarecruit", "company")
      print(f"Company created with ID: {company_id}")
    except Exception as e:
      print(f"Company already exists: {e}")

    # Add an internship
    try:
        internship_id = insert_internship("ML Engineer Intern", "Develope data-driven solutions", company_id, "2026-5-01")
        print(f"Internship created with ID: {internship_id}")
    except Exception as e:
        print(f"Failed to create internship: {e}")

    # Fetch data to verify
    internships = fetch_internships()
    print(f"Total internships in Database are: {len(internships)}")
    
    # Get some information anbout internship
    for internship in internships: 
        print(f"ID: {internship[0]}, Title: {internship[1]}, Deadline: {internship[4]}")

if __name__ == "__main__":
    main()
