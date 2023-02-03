from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)
from setup_db import query
import classes
import crud

@app.route('/register/<student_id>/<course_id>')
def register(student_id, course_id):
    query (F"INSERT INTO students_courses (student_id, course_id) VALUES ('{student_id}', '{course_id}')")
    return redirect(url_for('registrations', student_id=student_id))# שליחת המשתנה על הנתיב

@app.route('/registrations/<student_id>')
def registrations(student_id):
    course_ids=query(f"SELECT course_id FROM students_courses WHERE student_id={student_id}")
    clean_ids=[ c[0] for c in course_ids ]
    course_names=[]
    for i in clean_ids:
        course_names.append(query(f"SELECT name FROM courses WHERE id={i}"))
    student_name=query(f"SELECT name FROM students WHERE id={student_id}")
    return render_template("registrations.html", student_name=student_name, course_names=course_names)


