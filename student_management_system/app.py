from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Configure the app
app.config['SECRET_KEY'] = 'a-very-secret-key'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10))
    birth_date = db.Column(db.Date)
    contact = db.Column(db.String(100))
    address = db.Column(db.Text)
    enrollments = db.relationship('Enrollment', backref='student', lazy='dynamic', cascade="all, delete-orphan")

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    credit = db.Column(db.Float, default=0)
    enrollments = db.relationship('Enrollment', backref='course', lazy='dynamic', cascade="all, delete-orphan")

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    semester = db.Column(db.String(20), nullable=False)
    grade = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Import routes after models to avoid circular imports
from routes import *

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    # Ensure instance folder exists
    os.makedirs(os.path.join(basedir, 'instance'), exist_ok=True)
    app.run(debug=True)