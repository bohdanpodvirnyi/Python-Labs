from lab3.app import *
from flaskext.mysql import MySQL

app = Flask(__name__)
app.secret_key = 'python/labs/lab3'

mysql = MySQL()


def connect():
    # MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'upperlined27'
    app.config['MYSQL_DATABASE_DB'] = 'VNS'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)


def get_all_professors_from_db():
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_getAllProfessors')
    data = cursor.fetchall()

    professors = []
    for record in data:
        professors.append(Professor(*record))
    return professors


def get_course(course_id):
    if course_id <= 0:
        return {"Error": True, "Message": "Incorrect argument"}
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_getCourse', [course_id])
    data = cursor.fetchall()
    if len(data) == 0:
        return 0
    course = Course(*data[0])
    return course


def get_all_courses_by_professor(professor_id):
    if professor_id <= 0:
        return {"Error": True, "Message": "Incorrect argument"}
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_getAllCoursesByProfessor', [professor_id])
    data = cursor.fetchall()

    courses = []
    for record in data:
        courses.append(Course(*record))

    return courses


def get_all_students_courses(student_id):
    if student_id <= 0:
        return {"Error": True, "Message": "Incorrect argument"}
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_getAllStudentCourses', [student_id])
    data = cursor.fetchall()

    courses = []
    for record in data:
        courses.append(Course(*record))

    return courses


def add_student(student: Student):
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_addStudent', [student.first_name,
                                      student.mid_name,
                                      student.last_name,
                                      student.email,
                                      student.year_of_study])
    data = cursor.fetchall()

    if len(data) == 0:
        return 0

    student_id = int(data[0][0])
    return student_id


def add_professor(professor: Professor):
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_addProfessor', [professor.first_name,
                                        professor.mid_name,
                                        professor.last_name,
                                        professor.email,
                                        professor.department])
    data = cursor.fetchall()
    print(data)
    if len(data) == 0:
        return 0

    professor_id = int(data[0][0])
    return professor_id


def get_student(student_id):
    if student_id <= 0:
        return {"Error": True, "Message": "Incorrect argument"}
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getStudent', [student_id])
    data = cursor.fetchall()

    student = Student(*data[0])
    return student


def get_professor(professor_id):
    if professor_id <= 0:
        return {"Error": True, "Message": "Incorrect argument"}
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_getProfessor', [professor_id])
    data = cursor.fetchall()

    professor = Professor(*data[0])
    return professor


def db_login(email, user_type):
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()
    if user_type == "student":
        cursor.callproc('sp_loginStudent', [email])
        data = cursor.fetchall()
        if len(data) == 0:
            return 0
        student_id = int(data[0][0])
        return student_id
    elif user_type == "professor":
        cursor.callproc('sp_loginProfessor', [email])
        data = cursor.fetchall()
        if len(data) == 0:
            return 0
        professor_id = int(data[0][0])
        return professor_id
    else:
        return 0


def get_applications_by_id(course_id):

    if course_id <= 0:
        return {"Error": True, "Message": "Incorrect argument"}

    connect()
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_getApplications', [course_id])
    data = cursor.fetchall()

    applications = []
    for record in data:
        applications.append(Application(*record))

    return applications


def save_course(course):
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_addNewCourse', [course.name,
                                        course.description,
                                        course.professor_id,
                                        course.professor_id])
    conn.commit()
    data = cursor.fetchall()
    if len(data) == 0:
        return 0
    course = Course(*data[0])
    return course


def patch_course(course):
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_patchCourse', [course.name,
                                       course.description,
                                       course.professor_id,
                                       course.professor_id])
    conn.commit()
    data = cursor.fetchall()

    if len(data) == 0:
        return 0
    course = Course(*data[0])
    return course


def delete_course_from_db(course_id):
    if course_id <= 0:
        return {"Error": True, "Message": "Incorrect argument"}
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_deleteCourse', [course_id])
    conn.commit()
    data = cursor.fetchall()

    if len(data) == 0:
        return 0
    course = Course(*data[0])
    return course


def add_students_to_course(course_id, students):
    if course_id <= 0 or len(students) == 0:
        return {"Error": True, "Message": "Incorrect argument"}
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()
    for student in students:
        cursor.callproc('sp_addStudentToCourse', [course_id, db_login(student, "student")])
    conn.commit()
    return


def create_application(course_id, student_id):
    if course_id <= 0 or student_id <= 0:
        return {"Error": True, "Message": "Incorrect argument"}
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('sp_createApplication', [course_id, student_id])
    conn.commit()

    application = Application(student_id, course_id, "pending")
    return application


def change_application_status(application_id, status):
    if application_id <= 0:
        return {"Error": True, "Message": "Incorrect argument"}
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_changeApplicationStatus', [application_id, status])
    if status == 2:
        cursor.callproc('sp_acceptApplication', [application_id])
    conn.commit()
    return
