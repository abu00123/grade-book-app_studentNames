from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name, grade):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)

    def calculate_GPA(self):
        for student in self.student_list:
            student.calculate_GPA()

    def calculate_ranking(self):
        self.student_list.sort(key=lambda s: s.GPA, reverse=True)
        for rank, student in enumerate(self.student_list, 1):
            print(f"Rank {rank}: {student.names} - GPA: {student.GPA:.2f}")

    def search_by_grade(self, min_grade, max_grade):
        result = [s for s in self.student_list if min_grade <= s.GPA <= max_grade]
        for student in result:
            print(f"Student: {student.names}, GPA: {student.GPA:.2f}")

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            print(f"Transcript for {student.names}:")
            for course in student.courses_registered:
                print(f"Course: {course['course'].name}, Grade: {course['grade']}, Credits: {course['course'].credits}")
            print(f"GPA: {student.GPA:.2f}")

    def print_all_students(self):
        if not self.student_list:
            print("No students registered yet.")
        else:
            print("All registered students:")
            for student in self.student_list:
                print(f"Email: {student.email}, Names: {student.names}, GPA: {student.GPA:.2f}")

