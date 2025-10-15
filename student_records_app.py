from sqlalchemy import create_engine, Column, Integer, String, Index, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random

Base = declarative_base()

SAMPLE_NAMES = [
    "Alice Johnson", "Bob Smith", "Carol Davis", "David Wilson", "Emma Brown",
    "Frank Miller", "Grace Lee", "Henry Taylor", "Ivy Chen", "Jack Martin",
    "Kate Anderson", "Leo Garcia", "Mia Martinez", "Noah Robinson", "Olivia Clark"
]

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    grade = Column(String(2), nullable=False)
    
    __table_args__ = (
        Index('idx_students_name', 'name'),#b-tree
        Index('idx_students_email_hash', text('email'), postgresql_using='hash'),
    )
    
    def __repr__(self):
        return f"<Student(name='{self.name}', email='{self.email}', grade='{self.grade}')>"

def setup_database():
    """Initialize database without dropping existing data"""
    engine = create_engine('postgresql://postgres:password123@localhost:5432/student_db')
    
    # Only create tables if they don't exist - NO DROP!
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    return Session(), engine

def insert_sample_data(session):
    """Insert sample student records only if table is empty"""
    # Check if table already has data
    existing_count = session.query(Student).count()
    
    if existing_count > 0:
        print(f"Table already contains {existing_count} records. Skipping insertion.")
        return
    
    # Insert only if table is empty
    grades = ['A', 'B', 'C', 'D', 'F']
    students = []
    
    for i, name in enumerate(SAMPLE_NAMES):
        email = f"{name.lower().replace(' ', '.')}@university.edu"
        grade = random.choice(grades)
        
        students.append(Student(name=name, email=email, grade=grade))
    
    session.add_all(students)
    session.commit()
    print(f"Inserted {len(students)} student records")

def display_all_students(session):
    """Display all students to verify data"""
    print("\n" + "="*60)
    print("ALL STUDENTS IN DATABASE")
    print("="*60)
    
    students = session.query(Student).order_by(Student.name).all()
    
    if not students:
        print("No students found in the database.")
        return
    
    for i, student in enumerate(students, 1):
        print(f"{i:2d}. {student.name:<20} | {student.email:<30} | Grade: {student.grade}")
    
    print(f"\nTotal students: {len(students)}")

def run_queries(session):
    """Run and analyze both query types"""
    # Get a sample student
    sample_student = session.query(Student).first()
    
    if not sample_student:
        print("No students found to run queries.")
        return
    
    print("\n" + "="*60)
    print("B-TREE INDEX QUERY (by name)")
    print("="*60)
    
    # B-tree query
    result = session.execute(text(
        f"EXPLAIN ANALYZE SELECT * FROM students WHERE name = '{sample_student.name}'"
    ))
    for row in result:
        print(row[0])
    
    print("\n" + "="*60)
    print("HASH INDEX QUERY (by email)")
    print("="*60)
    
    # Hash query
    result = session.execute(text(
        f"EXPLAIN ANALYZE SELECT * FROM students WHERE email = '{sample_student.email}'"
    ))
    for row in result:
        print(row[0])

def main():
    session, engine = setup_database()
    
    try:
        insert_sample_data(session)
        display_all_students(session)  # Show all students
        run_queries(session)
        
        print("\n" + "="*60)
        print("REFLECTION")
        print("="*60)
        print("B-tree indexes are versatile for range queries and sorting operations.")
        print("Hash indexes excel at exact equality matches with O(1) complexity.")
        print("Use B-trees for general purposes, hash indexes for specialized exact-match scenarios.")
        print("\nTo view data in pgAdmin:")
        print("1. Expand 'student_db' → 'Schemas' → 'public' → 'Tables'")
        print("2. Right-click 'students' table → 'View/Edit Data' → 'All Rows'")
        
    finally:
        session.close()
        engine.dispose()

if __name__ == "__main__":
    main()