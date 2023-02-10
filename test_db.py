import setup_db

def test_db_students():
    setup_db.create_tables()
    setup_db.create_fake_data(students_num=10, teachers_num=3)
    num_students=int(setup_db.query('SELECT COUNT(id) FROM students')[0][0])#מחזיר tuple- נכנסים לאיבר הראשון
    assert num_students==10

def test_db_teachers():
    num_teachers=int(setup_db.query('SELECT COUNT(id) FROM teachers')[0][0])
    assert num_teachers==3

def test_courses_teachers():
    num_teachers=int(setup_db.query('SELECT COUNT(teacher_id) FROM courses')[0][0])
    num_courses=int(setup_db.query('SELECT COUNT(id) FROM courses')[0][0])
    assert num_teachers==num_courses

def test