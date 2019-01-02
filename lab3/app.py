from flask import Flask, jsonify, request, session, redirect, url_for, escape
from lab3.model import *
from lab3.controller import *

app = Flask(__name__)
app.secret_key = 'python/labs/lab3'


@app.route('/', methods=['GET'])
def initial():
    if 'user_type' in escape(session):
        user_id = escape(session['user_id'])
        return jsonify({"success": True, "id": user_id})
    return get_login_error()


@app.route('/signup/<type>', methods=['POST'])
def signup(type):
    first_name = request.form.get('first_name', default="", type=str)
    mid_name = request.form.get('mid_name', default="", type=str)
    last_name = request.form.get('last_name', default="", type=str)
    email = request.form.get('email', default="", type=str)
    if type == "student":
        year_of_study = request.form.get('year_of_study', default=1, type=int)
        student = Student(first_name, mid_name, last_name, email, year_of_study)
        session['user_type'] = "student"
        session['user_id'] = add_student(student)
    else:
        department = request.form.get('department', default="", type=str)
        professor = Professor(first_name, mid_name, last_name, email, department)
        session['user_type'] = "professor"
        session['user_id'] = add_professor(professor)
    return redirect(url_for('initial'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if check_session():
        user_type = escape(session['user_type'])
        user_id = int(escape(session['user_id']))
        print(user_id)
        if user_type == "student":
            student = get_student(user_id)
            return jsonify({"student": student.to_json()})
        else:
            professor = get_professor(user_id)
            return jsonify({"professor": professor.to_json()})
    else:
        email = request.form.get('email', default="", type=str)
        user_type = request.form.get('type', default="", type=str)
        user_id = db_login(email, user_type)
        if user_id > 0:
            session['user_id'] = user_id
            session['user_type'] = user_type
            return jsonify({"success": True, "id": user_id})
        else:
            return get_login_error()


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user_type', None)
    session.pop('user_id', None)
    return jsonify({"success": True, "message": "Logout successful."})


@app.route('/my_courses', methods=['GET'])
def get_my_courses():
    auth = check_authorization()
    if auth:
        if auth[0] == "student":
            course_id = request.args.get('id')
            if course_id:
                course = get_course(course_id)
                if course == 0:
                    return jsonify({"error": True, "message": "There\' is no course with this id."})
                return jsonify({"course": course.to_json()})
            else:
                courses = get_all_students_courses(auth[1])
        else:
            course_id = request.args.get('id')
            if course_id:
                course = get_course(course_id)
                if course == 0:
                    return jsonify({"error": True, "message": "There\' is no course with this id."})
                return jsonify({"course": course.to_json()})
            else:
                courses = get_all_courses_by_professor(auth[1])
        result = []
        for course in courses:
            result.append(course.to_json())
        return jsonify({'courses': result})
    else:
        return get_login_error()


@app.route('/create_course', methods=['POST'])
def create_course():
    auth = check_authorization()
    if auth:
        if auth[0] == "professor":
            name = request.form.get('name', default="", type=str)
            description = request.form.get('description', default="", type=str)
            number_of_lectures = request.form.get('number_of_lectures', default="", type=str)
            new_course = save_course(Course(name, description, number_of_lectures, auth[1]))
            return jsonify({"course": new_course.to_json()})
        return get_access_error()
    else:
        return get_login_error()


@app.route('/my_courses/<course_id>', methods=['DELETE', 'PATCH', 'GET'])
def delete_course(course_id):
    auth = check_authorization()
    if auth:
        if auth[0] == "professor":
            course = get_course(course_id)
            if course is not Course:
                return something_went_wrong()
            if request.method == 'GET':
                return jsonify({"course": course.to_json()})
            elif request.method == 'PATCH':
                name = request.form.get('name', default="", type=str)
                description = request.form.get('description', default="", type=str)
                number_of_lectures = request.form.get('number_of_lectures', default="", type=str)
                new_course = patch_course(Course(name, description, number_of_lectures, auth[1]))
                return jsonify({"course": new_course.to_json()})
            else:
                delete_course_from_db(course_id)
                return jsonify({"success": True, "message": "Course was deleted successfully."})
        return get_access_error()
    else:
        return get_login_error()


@app.route('/my_courses/<course_id>/add', methods=['POST'])
def add_students(course_id):
    auth = check_authorization()
    if auth:
        if auth[0] == "professor":
            students = request.json["students"]
            add_students_to_course(course_id, students)
            return jsonify({"success": True, "message": "Students added successfully."})
        return get_access_error()
    else:
        return get_login_error()


@app.route('/apply/<course_id>', methods=['GET'])
def apply_to_course(course_id):
    auth = check_authorization()
    if auth:
        if auth[0] == "student":
            create_application(course_id, auth[1])
            return jsonify({"success": True, "message": "Application sent."})
        return get_access_error()
    else:
        return get_login_error()


@app.route('/my_courses/<course_id>/applications', methods=['GET'])
def show_applications(course_id):
    auth = check_authorization()
    if auth:
        if auth[0] == "professor":
            applications = get_applications_by_id(course_id)
            result = []
            for application in applications:
                result.append(application.to_json())
            return jsonify({'courses': result})
        return get_access_error()
    else:
        return get_login_error()


@app.route('/my_courses/<course_id>/applications/<application_id>', methods=['GET'])
def edit_application(course_id, application_id):
    auth = check_authorization()
    if auth:
        if auth[0] == "professor":
            new_status = request.args.get('status')
            change_application_status(application_id, new_status)
            return jsonify({"success": True, "message": "Application status changed."})
        return get_access_error()
    else:
        return get_login_error()


def check_session():
    if 'user_id' in escape(session):
        if escape(session['user_type']) == "student" or escape(session['user_type']) == "professor":
            if int(escape(session['user_id'])) > 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def check_authorization():
    user_type = escape(session['user_type'])
    user_id = int(escape(session['user_id']))
    if user_type == "student" or user_type == "professor":
        if user_id > 0:
            return user_type, user_id


def get_login_error():
    result = {"error": True, "message": "Login error. Please, log in and try again."}
    return jsonify(result)


def get_access_error():
    result = {"error": True, "message": "Access error. You have no access to this data."}
    return jsonify(result)


def something_went_wrong():
    result = {"error": True, "message": "Something went wrong. Please, try again."}
    return jsonify(result)
