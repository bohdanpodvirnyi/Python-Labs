import unittest as test
import lab3.controller as controller
import lab3.model as model


class ApplicationTest(test.TestCase):

    # controller tests

    def test_get_all_professors(self):
        actual_result = controller.get_all_professors_from_db()

        self.assertIsInstance(actual_result, list)
        for result in actual_result:
            self.assertIsInstance(result, model.Professor)

    def test_get_course(self):
        course_id = 1
        actual_result = controller.get_course(course_id)

        self.assertIsInstance(actual_result, model.Course)

        course_id = -1
        actual_result = controller.get_course(course_id)

        self.assertIsInstance(actual_result, dict)
        self.assertTrue(actual_result["Error"])

    def test_get_all_courses_by_professor(self):
        professor_id = 1
        actual_result = controller.get_all_courses_by_professor(professor_id)

        self.assertIsInstance(actual_result, list)
        for result in actual_result:
            self.assertIsInstance(result, model.Course)

        professor_id = -1
        actual_result = controller.get_all_courses_by_professor(professor_id)

        self.assertIsInstance(actual_result, dict)
        self.assertTrue(actual_result["Error"])

    def test_get_all_students_courses(self):
        student_id = 8
        actual_result = controller.get_all_students_courses(student_id)

        self.assertIsInstance(actual_result, list)
        for result in actual_result:
            self.assertIsInstance(result, model.Course)

        student_id = -1
        actual_result = controller.get_all_students_courses(student_id)

        self.assertIsInstance(actual_result, dict)
        self.assertTrue(actual_result["Error"])

    def test_add_student(self):
        student = model.Student("Test", "-", "Student", "test@email.com", 1)
        actual_result = controller.add_student(student)

        self.assertIsInstance(actual_result, model.Student)
        self.assertEqual(student.to_json(), actual_result.to_json())

    def test_add_professor(self):
        professor = model.Professor("Test", "-", "Professor", "test@email.com", "AI")
        actual_result = controller.add_professor(professor)

        self.assertIsInstance(actual_result, model.Professor)
        self.assertEqual(professor.to_json(), actual_result.to_json())

    def test_get_student(self):
        student_id = 8
        expected_result = model.Student("Test", "-", "3", "test3@gmail.com", 1)
        actual_result = controller.get_student(student_id)

        self.assertIsInstance(actual_result, model.Student)
        self.assertEqual(expected_result.to_json(), actual_result.to_json())

    def test_get_professor(self):
        professor_id = 1
        expected_result = model.Professor("Jack", "-", "Russel", "test2@gmail.com", "AI")
        actual_result = controller.get_professor(professor_id)

        self.assertIsInstance(actual_result, model.Professor)
        self.assertEqual(expected_result.to_json(), actual_result.to_json())

        professor_id = -1
        actual_result = controller.get_professor(professor_id)

        self.assertIsInstance(actual_result, dict)
        self.assertTrue(actual_result["Error"])

    def test_db_student_login(self):
        email = "test@gmail.com"
        user_type = "student"
        actual_result = controller.db_login(email, user_type)

        self.assertIsInstance(actual_result, int)
        self.assertNotEqual(actual_result, 0)

        email = "test2@gmail.com"
        user_type = "professor"
        actual_result = controller.db_login(email, user_type)

        self.assertIsInstance(actual_result, int)
        self.assertNotEqual(actual_result, 0)

        email = ""
        user_type = "student"
        actual_result = controller.db_login(email, user_type)

        self.assertIsInstance(actual_result, int)
        self.assertEqual(actual_result, 0)

        user_type = "professor"
        actual_result = controller.db_login(email, user_type)

        self.assertIsInstance(actual_result, int)
        self.assertEqual(actual_result, 0)

    def test_get_applications_by_id(self):
        course_id = 1
        actual_result = controller.get_applications_by_id(course_id)

        self.assertIsInstance(actual_result, list)
        for result in actual_result:
            self.assertIsInstance(result, model.Application)

        course_id = -1
        actual_result = controller.get_applications_by_id(course_id)

        self.assertIsInstance(actual_result, dict)
        self.assertTrue(actual_result["Error"])

    def test_save_course(self):
        course = model.Course("Test", "-", 10, 1)
        actual_result = controller.save_course(course)

        self.assertIsInstance(actual_result, model.Course)
        self.assertEqual(course.to_json(), actual_result.to_json())

    def test_patch_course(self):
        course = model.Course("Test", "-", 10, 1)
        actual_result = controller.patch_course(course)

        self.assertIsInstance(actual_result, model.Course)
        self.assertEqual(course.to_json(), actual_result.to_json())

    def test_delete_course_from_db(self):
        course_id = 1
        actual_result = controller.delete_course_from_db(course_id)

        self.assertIsInstance(actual_result, model.Course)
        test_result = controller.get_course(course_id)
        self.assertEqual(test_result, 0)

        course_id = -1
        actual_result = controller.delete_course_from_db(course_id)

        self.assertIsInstance(actual_result, dict)
        self.assertTrue(actual_result["Error"])

    def test_add_students_to_course(self):
        course_id = 1
        students = ["test3@gmail.com"]
        actual_result = controller.add_students_to_course(course_id, students)

        self.assertIsNone(actual_result)

        course_id = -1
        actual_result = controller.add_students_to_course(course_id, students)

        self.assertIsInstance(actual_result, dict)
        self.assertTrue(actual_result["Error"])

        students = []
        actual_result = controller.add_students_to_course(course_id, students)

        self.assertIsInstance(actual_result, dict)
        self.assertTrue(actual_result["Error"])

    def test_create_application(self):
        course_id = 1
        student_id = 1
        actual_result = controller.create_application(course_id, student_id)

        self.assertIsInstance(actual_result, model.Application)

        course_id = -1
        actual_result = controller.create_application(course_id, student_id)

        self.assertIsInstance(actual_result, dict)
        self.assertTrue(actual_result["Error"])

        course_id = 1
        student_id = -1
        actual_result = controller.create_application(course_id, student_id)

        self.assertIsInstance(actual_result, dict)
        self.assertTrue(actual_result["Error"])

    def test_change_application_status(self):
        application_id = 1
        status = 0
        actual_result = controller.change_application_status(application_id, status)

        self.assertIsNone(actual_result)

    def test_to_json(self):
        course = model.Course("AI", "-", 10, 1)
        json = course.to_json()

        self.assertIsInstance(json, dict)
        self.assertEqual(json["name"], course.name)
        self.assertEqual(json["description"], course.description)
        self.assertEqual(json["number_of_lectures"], course.number_of_lectures)
        self.assertEqual(json["professor_id"], course.professor_id)
        self.assertEqual(json["students"], course.students)
