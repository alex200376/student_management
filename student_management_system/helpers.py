from datetime import datetime
from flask import request, flash

def get_date_from_string(date_str):
    """Convert string to date object"""
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return None

def validate_student_form(form):
    """Validate student form data"""
    errors = []
    
    if not form.get('student_id'):
        errors.append('Student ID cannot be empty')
    
    if not form.get('name'):
        errors.append('Name cannot be empty')
    
    # Can add more validation rules
    
    return errors

def validate_course_form(form):
    """Validate course form data"""
    errors = []
    
    if not form.get('course_code'):
        errors.append('Course code cannot be empty')
    
    if not form.get('name'):
        errors.append('Course name cannot be empty')
    
    credit = form.get('credit')
    if credit:
        try:
            float(credit)
        except ValueError:
            errors.append('Credit must be a number')
    
    return errors

def validate_enrollment_form(form):
    """Validate enrollment/grade form data"""
    errors = []
    
    if not form.get('student_id'):
        errors.append('Please select a student')
    
    if not form.get('course_id'):
        errors.append('Please select a course')
    
    if not form.get('semester'):
        errors.append('Semester cannot be empty')
    
    grade = form.get('grade')
    if grade:
        try:
            float(grade)
        except ValueError:
            errors.append('Grade must be a number')
    
    return errors

def flash_errors(errors):
    """Flash error messages"""
    for error in errors:
        flash(error, 'error')

def calculate_gpa(enrollments):
    """Calculate GPA"""
    if not enrollments:
        return 0
    
    total_credits = 0
    weighted_sum = 0
    
    for enrollment in enrollments:
        if enrollment.grade is not None and enrollment.course.credit:
            total_credits += enrollment.course.credit
            weighted_sum += enrollment.grade * enrollment.course.credit
    
    if total_credits == 0:
        return 0
    
    return round(weighted_sum / total_credits, 2)