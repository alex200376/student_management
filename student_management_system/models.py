from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Student(db.Model):
    """Student Model"""
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), unique=True, nullable=False)  # Student ID
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10))
    birth_date = db.Column(db.Date)
    contact = db.Column(db.String(50))
    address = db.Column(db.String(100))
    enrollments = db.relationship('Enrollment', backref='student', lazy=True, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Student {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'name': self.name,
            'gender': self.gender,
            'birth_date': self.birth_date.strftime('%Y-%m-%d') if self.birth_date else None,
            'contact': self.contact,
            'address': self.address
        }

class Course(db.Model):
    """Course Model"""
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    credit = db.Column(db.Float, default=0)
    enrollments = db.relationship('Enrollment', backref='course', lazy=True, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Course {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'course_code': self.course_code,
            'name': self.name,
            'credit': self.credit
        }

class Enrollment(db.Model):
    """Enrollment/Grade Model"""
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    semester = db.Column(db.String(20), nullable=False)
    grade = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Enrollment {self.student_id}-{self.course_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'semester': self.semester,
            'grade': self.grade,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }