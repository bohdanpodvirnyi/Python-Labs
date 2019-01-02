class BaseObject(object):
    def to_json(self):
        result = {}
        for s in self.__dict__:
            result[s] = self.__dict__[s]
        return result


class UserBasic(BaseObject):
    def __init__(self, first_name, mid_name, last_name):
        self.first_name = first_name
        self.mid_name = mid_name
        self.last_name = last_name


class Course(BaseObject):
    def __init__(self, name, description, number_of_lectures, professor_id):
        self.name = name
        self.description = description
        self.number_of_lectures = number_of_lectures
        self.professor_id = professor_id
        self.students = []


class Student(UserBasic):
    def __init__(self, first_name, mid_name, last_name, email, year_of_study):
        UserBasic.__init__(self, first_name, mid_name, last_name)
        self.email = email
        self.year_of_study = year_of_study
        self.courses = []


class Application(BaseObject):
    def __init__(self, student, course, status):
        self.student = student
        self.course = course
        self.status = status


class Professor(UserBasic):
    def __init__(self, first_name, mid_name, last_name, email, department):
        UserBasic.__init__(self, first_name, mid_name, last_name)
        self.email = email
        self.department = department
        self.courses = []
