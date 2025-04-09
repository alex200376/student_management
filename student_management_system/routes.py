from flask import render_template, request, redirect, url_for, flash
from app import app, db, Student, Course, Enrollment
from datetime import datetime

# Index route
@app.route('/')
def index():
    student_count = Student.query.count()
    course_count = Course.query.count()
    enrollment_count = Enrollment.query.count()
    return render_template('index.html', 
                          student_count=student_count,
                          course_count=course_count,
                          enrollment_count=enrollment_count)

# Student routes
@app.route('/students')
def list_students():
    students = Student.query.all()
    return render_template('students/list.html', students=students)

@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        name = request.form.get('name')
        gender = request.form.get('gender')
        birth_date_str = request.form.get('birth_date')
        contact = request.form.get('contact')
        address = request.form.get('address')
        
        # Validation
        if not student_id or not name:
            flash('Student ID and Name are required!', 'danger')
            return render_template('students/add.html')
        
        # Check if student_id already exists
        if Student.query.filter_by(student_id=student_id).first():
            flash('This Student ID already exists!', 'danger')
            return render_template('students/add.html')
        
        # Process birth date
        birth_date = None
        if birth_date_str:
            try:
                birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
            except ValueError:
                flash('Invalid birth date format!', 'danger')
                return render_template('students/add.html')
        
        # Create new student
        student = Student(
            student_id=student_id,
            name=name,
            gender=gender,
            birth_date=birth_date,
            contact=contact,
            address=address
        )
        
        db.session.add(student)
        db.session.commit()
        
        flash('Student added successfully!', 'success')
        return redirect(url_for('list_students'))
    
    return render_template('students/add.html')

@app.route('/students/<int:id>')
def view_student(id):
    student = Student.query.get_or_404(id)
    enrollments = Enrollment.query.filter_by(student_id=id).all()
    return render_template('students/view.html', student=student, enrollments=enrollments)

@app.route('/students/<int:id>/edit', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        name = request.form.get('name')
        gender = request.form.get('gender')
        birth_date_str = request.form.get('birth_date')
        contact = request.form.get('contact')
        address = request.form.get('address')
        
        # Validation
        if not student_id or not name:
            flash('Student ID and Name are required!', 'danger')
            return render_template('students/edit.html', student=student)
        
        # Check if student_id already exists and is not the current student
        existing_student = Student.query.filter_by(student_id=student_id).first()
        if existing_student and existing_student.id != student.id:
            flash('This Student ID already exists!', 'danger')
            return render_template('students/edit.html', student=student)
        
        # Process birth date
        birth_date = None
        if birth_date_str:
            try:
                birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
            except ValueError:
                flash('Invalid birth date format!', 'danger')
                return render_template('students/edit.html', student=student)
        
        # Update student
        student.student_id = student_id
        student.name = name
        student.gender = gender
        student.birth_date = birth_date
        student.contact = contact
        student.address = address
        
        db.session.commit()
        
        flash('Student information updated successfully!', 'success')
        return redirect(url_for('view_student', id=student.id))
    
    return render_template('students/edit.html', student=student)

@app.route('/students/<int:id>/delete', methods=['POST'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    
    db.session.delete(student)
    db.session.commit()
    
    flash('Student deleted!', 'success')
    return redirect(url_for('list_students'))

# Course routes
@app.route('/courses')
def list_courses():
    courses = Course.query.all()
    return render_template('courses/list.html', courses=courses)

@app.route('/courses/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_code = request.form.get('course_code')
        name = request.form.get('name')
        credit_str = request.form.get('credit')
        
        # Validation
        if not course_code or not name:
            flash('Course Code and Course Name are required!', 'danger')
            return render_template('courses/add.html')
        
        # Check if course_code already exists
        if Course.query.filter_by(course_code=course_code).first():
            flash('This Course Code already exists!', 'danger')
            return render_template('courses/add.html')
        
        # Process credit
        credit = 0
        if credit_str:
            try:
                credit = float(credit_str)
            except ValueError:
                flash('Credit must be a number!', 'danger')
                return render_template('courses/add.html')
        
        # Create new course
        course = Course(
            course_code=course_code,
            name=name,
            credit=credit
        )
        
        db.session.add(course)
        db.session.commit()
        
        flash('Course added successfully!', 'success')
        return redirect(url_for('list_courses'))
    
    return render_template('courses/add.html')

@app.route('/courses/<int:id>/edit', methods=['GET', 'POST'])
def edit_course(id):
    course = Course.query.get_or_404(id)
    
    if request.method == 'POST':
        course_code = request.form.get('course_code')
        name = request.form.get('name')
        credit_str = request.form.get('credit')
        
        # Validation
        if not course_code or not name:
            flash('Course Code and Course Name are required!', 'danger')
            return render_template('courses/edit.html', course=course)
        
        # Check if course_code already exists and is not the current course
        existing_course = Course.query.filter_by(course_code=course_code).first()
        if existing_course and existing_course.id != course.id:
            flash('This Course Code already exists!', 'danger')
            return render_template('courses/edit.html', course=course)
        
        # Process credit
        credit = 0
        if credit_str:
            try:
                credit = float(credit_str)
            except ValueError:
                flash('Credit must be a number!', 'danger')
                return render_template('courses/edit.html', course=course)
        
        # Update course
        course.course_code = course_code
        course.name = name
        course.credit = credit
        
        db.session.commit()
        
        flash('Course information updated successfully!', 'success')
        return redirect(url_for('list_courses'))
    
    return render_template('courses/edit.html', course=course)

@app.route('/courses/<int:id>/delete', methods=['POST'])
def delete_course(id):
    course = Course.query.get_or_404(id)
    
    db.session.delete(course)
    db.session.commit()
    
    flash('Course deleted!', 'success')
    return redirect(url_for('list_courses'))

# Grade routes
@app.route('/grades')
def list_grades():
    enrollments = Enrollment.query.all()
    return render_template('grades/list.html', enrollments=enrollments)

@app.route('/grades/add', methods=['GET', 'POST'])
def add_grade():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        course_id = request.form.get('course_id')
        semester = request.form.get('semester')
        grade_str = request.form.get('grade')
        
        # Validation
        if not student_id or not course_id or not semester:
            flash('Student, Course, and Semester are required!', 'danger')
            students = Student.query.all()
            courses = Course.query.all()
            return render_template('grades/add.html', students=students, courses=courses)
        
        # Check if the enrollment already exists
        existing_enrollment = Enrollment.query.filter_by(
            student_id=student_id,
            course_id=course_id,
            semester=semester
        ).first()
        
        if existing_enrollment:
            flash('This student has already enrolled in this course for this semester!', 'danger')
            students = Student.query.all()
            courses = Course.query.all()
            return render_template('grades/add.html', students=students, courses=courses)
        
        # Process grade
        grade = None
        if grade_str:
            try:
                grade = float(grade_str)
                if grade < 0 or grade > 100:
                    flash('Grade must be between 0-100!', 'danger')
                    students = Student.query.all()
                    courses = Course.query.all()
                    return render_template('grades/add.html', students=students, courses=courses)
            except ValueError:
                flash('Grade must be a number!', 'danger')
                students = Student.query.all()
                courses = Course.query.all()
                return render_template('grades/add.html', students=students, courses=courses)
        
        # Create new enrollment
        enrollment = Enrollment(
            student_id=student_id,
            course_id=course_id,
            semester=semester,
            grade=grade
        )
        
        db.session.add(enrollment)
        db.session.commit()
        
        flash('Grade added successfully!', 'success')
        return redirect(url_for('list_grades'))
    
    students = Student.query.all()
    courses = Course.query.all()
    return render_template('grades/add.html', students=students, courses=courses)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500