DELIMITER //
DROP PROCEDURE IF EXISTS VNS.sp_getAllProfessors;
CREATE PROCEDURE VNS.`sp_getAllProfessors` ()
  BEGIN
    select first_name, mid_name, last_name, email, department from Professor;
  end//

DROP PROCEDURE IF EXISTS VNS.sp_getCourse;
CREATE PROCEDURE VNS.`sp_getCourse` (IN c_id INT)
  BEGIN
    select name, description, number_of_lectures, Professor_professor_id from Courses where course_id = c_id;
  end;

DROP PROCEDURE IF EXISTS VNS.sp_getAllCoursesByProfessor;
CREATE PROCEDURE VNS.`sp_getAllCoursesByProfessor` (IN pr_id INT)
  BEGIN
    select name, description, number_of_lectures, Professor_professor_id from Courses where Professor_professor_id = pr_id;
  end;

DROP PROCEDURE IF EXISTS VNS.sp_getAllStudentCourses;
CREATE PROCEDURE VNS.`sp_getAllStudentCourses` (IN st_id INT)
  BEGIN
    select name, description, number_of_lectures, Professor_professor_id from Courses
        where course_id = (select Courses_course_id from Students_has_Courses where Students_student_id = st_id);
  end;

DROP PROCEDURE IF EXISTS VNS.sp_addStudent;
CREATE PROCEDURE VNS.`sp_addStudent` (IN first_name VARCHAR(20), mid_name VARCHAR(20), last_name VARCHAR(20), email VARCHAR(50), year_of_study INT)
  BEGIN
    insert into Students (first_name, mid_name, last_name, email, year_of_study)
    value (first_name, mid_name, last_name, email, year_of_study);
  end;

DROP PROCEDURE IF EXISTS VNS.sp_getStudent;
CREATE PROCEDURE VNS.`sp_getStudent` (IN st_id INT)
  BEGIN
    select first_name, mid_name, last_name, email, year_of_study from Students where student_id = st_id;
  end;

DROP PROCEDURE IF EXISTS VNS.sp_loginStudent;
CREATE PROCEDURE VNS.`sp_loginStudent` (IN st_email VARCHAR(50))
  BEGIN
    select student_id from Students where email = st_email;
  end;

DROP PROCEDURE IF EXISTS VNS.sp_loginProfessor;
CREATE PROCEDURE VNS.`sp_loginProfessor` (IN pr_email VARCHAR(50))
  BEGIN
    select professor_id from Professor where email = pr_email;
  end;

DROP PROCEDURE IF EXISTS VNS.sp_getApplications;
CREATE PROCEDURE VNS.`sp_getApplications` (IN c_id INT)
  BEGIN
    select Students_student_id, Courses_course_id, status from Application where Courses_course_id = c_id;
  end;

DROP PROCEDURE IF EXISTS VNS.sp_addNewCourse;
CREATE PROCEDURE VNS.`sp_addNewCourse` (IN c_name VARCHAR(20), c_description VARCHAR(200), c_number_of_lectures INT, c_pr_id INT)
  BEGIN
    insert into Courses (name, description, number_of_lectures, Professor_professor_id)
    value (c_name, c_description, c_number_of_lectures, c_pr_id);
  end;

DROP PROCEDURE IF EXISTS VNS.sp_patchCourse;
CREATE PROCEDURE VNS.`sp_patchCourse` (IN c_name VARCHAR(20), c_description VARCHAR(200), c_number_of_lectures INT, c_id INT)
  BEGIN
    update Courses SET name = c_name, description = c_description, number_of_lectures = c_number_of_lectures where course_id = c_id;
  end;

DROP PROCEDURE IF EXISTS VNS.sp_deleteCourse;
CREATE PROCEDURE VNS.`sp_deleteCourse` (IN c_id INT)
  BEGIN
    delete from Courses where course_id = c_id;
  end;

DROP PROCEDURE IF EXISTS VNS.sp_addStudentToCourse;
CREATE PROCEDURE VNS.`sp_addStudentToCourse` (IN c_id INT, st_id INT)
  BEGIN
    insert into Students_has_Courses (Students_student_id, Courses_course_id)
    value (st_id, c_id);
  end;

DROP PROCEDURE IF EXISTS VNS.sp_createApplication;
CREATE PROCEDURE VNS.`sp_createApplication` (IN c_id INT, st_id INT)
  BEGIN
    insert into Application (Students_student_id, Courses_course_id, status)
    value (st_id, c_id, 1);
  end;

DROP PROCEDURE IF EXISTS VNS.sp_changeApplicationStatus;
CREATE PROCEDURE VNS.`sp_changeApplicationStatus` (IN a_id INT, new_status TINYINT)
  BEGIN
    update Application set status = new_status where application_id = a_id;
  end;
