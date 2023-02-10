from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)
from setup_db import query
import classes
import crud
from sqlite3 import IntegrityError
from collections import namedtuple

@app.route('/register/<student_id>/<course_id>')
def register(student_id, course_id):
    try:
        query (F"INSERT INTO students_courses (student_id, course_id) VALUES ('{student_id}', '{course_id}')")
    except IntegrityError:
        return f"{student_id} is rong"
    return redirect(url_for('registrations', student_id=student_id))# שליחת המשתנה על הנתיב

@app.route('/registrations/<student_id>')
def registrations(student_id):
    #course_ids=query(f"SELECT course_id FROM students_courses WHERE student_id={student_id}")
    #clean_ids=[ c[0] for c in course_ids ]
    #course_names=[]
    #for i in clean_ids:
    #    course_names.append(query(f"SELECT name FROM courses WHERE id={i}"))
    #student_name=query(f"SELECT name FROM students WHERE id={student_id}")
    course_student=query(f"""
    SELECT students.name FROM students WHERE id={student_id} UNION
    SELECT courses.name FROM courses JOIN students_courses on students_courses.course_id=course_id WHERE students_courses.student_id={student_id}
    """)
    courses=[]
    for course_tuple in course_student:
        course=namedtuple('Course', ['name', 'teacher'])
        course.name=course_tuple[0]
        courses.append(course)

    return render_template("registrations.html", course_student=course_student, courses=courses)

@app.route('/students')
def show_students():
    students_list=crud.read_all('students')
    students_object=[classes.Student(student[0], student[1], student[2]) for student in students_list]
    return render_template('students.html', students_object=students_object)

@app.route('/courses/<student_tid>')
def show_courses(student_tid):
    return render_template('courses.html', student_tid=student_tid)


# TODO