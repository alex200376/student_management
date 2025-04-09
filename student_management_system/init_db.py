from app import app, db, Student, Course, Enrollment
from datetime import datetime

def reset_db():
    """Delete and recreate all database tables"""
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Database has been reset.")

def add_sample_data():
    """Add sample data (in English) to the database"""
    with app.app_context():
        # Check if the database is empty
        if Student.query.count() > 0 or Course.query.count() > 0:
            print("Database already contains data. Please reset the database first to add sample data.")
            return False
        
        print("Adding sample data...")
        
        # Add sample students
        students = [
            Student(student_id="S001", name="John Smith", gender="Male", 
                   birth_date=datetime.strptime("2000-05-15", "%Y-%m-%d").date(),
                   contact="john.smith@email.com", address="123 Main St"),
            Student(student_id="S002", name="Emma Johnson", gender="Female", 
                   birth_date=datetime.strptime("2001-08-22", "%Y-%m-%d").date(),
                   contact="emma.j@email.com", address="456 Oak Avenue"),
            Student(student_id="S003", name="Michael Brown", gender="Male", 
                   birth_date=datetime.strptime("2000-11-10", "%Y-%m-%d").date(),
                   contact="m.brown@email.com", address="789 Pine Road"),
            Student(student_id="S004", name="Sophia Davis", gender="Female", 
                   birth_date=datetime.strptime("2001-03-17", "%Y-%m-%d").date(),
                   contact="sophia.d@email.com", address="321 Maple Drive"),
            Student(student_id="S005", name="William Wilson", gender="Male", 
                   birth_date=datetime.strptime("2000-07-30", "%Y-%m-%d").date(),
                   contact="will.wilson@email.com", address="654 Cedar Lane"),
        ]
        
        # Add sample courses
        courses = [
            Course(course_code="CS101", name="Introduction to Programming", credit=3.0),
            Course(course_code="CS202", name="Data Structures", credit=4.0),
            Course(course_code="MATH101", name="Calculus I", credit=4.0),
            Course(course_code="ENG101", name="English Composition", credit=3.0),
            Course(course_code="PHYS201", name="Physics for Scientists", credit=4.0),
        ]
        
        # Add all students and courses to the database
        db.session.add_all(students)
        db.session.add_all(courses)
        db.session.commit()
        
        # Add sample enrollments with grades
        enrollments = [
            Enrollment(student_id=1, course_id=1, semester="Fall 2023", grade=85.5),
            Enrollment(student_id=1, course_id=3, semester="Fall 2023", grade=78.0),
            Enrollment(student_id=2, course_id=1, semester="Fall 2023", grade=92.0),
            Enrollment(student_id=2, course_id=4, semester="Fall 2023", grade=88.5),
            Enrollment(student_id=3, course_id=2, semester="Fall 2023", grade=76.0),
            Enrollment(student_id=3, course_id=5, semester="Fall 2023", grade=81.5),
            Enrollment(student_id=4, course_id=3, semester="Fall 2023", grade=95.0),
            Enrollment(student_id=4, course_id=4, semester="Fall 2023", grade=90.0),
            Enrollment(student_id=5, course_id=1, semester="Fall 2023", grade=82.5),
            Enrollment(student_id=5, course_id=5, semester="Fall 2023", grade=87.0),
            # Spring 2024 enrollments
            Enrollment(student_id=1, course_id=2, semester="Spring 2024", grade=88.0),
            Enrollment(student_id=2, course_id=2, semester="Spring 2024", grade=91.0),
            Enrollment(student_id=3, course_id=3, semester="Spring 2024", grade=79.5),
            Enrollment(student_id=4, course_id=5, semester="Spring 2024", grade=93.0),
            Enrollment(student_id=5, course_id=4, semester="Spring 2024", grade=85.0),
        ]
        
        db.session.add_all(enrollments)
        db.session.commit()
        
        print("Sample data has been successfully added to the database.")
        return True

def init_db_with_sample_data():
    """Initialize database and add sample data"""
    reset_db()
    add_sample_data()

if __name__ == "__main__":
    # When this script is run directly, initialize the database and add sample data
    init_db_with_sample_data()
    print("Database initialization complete, sample data has been added.") 