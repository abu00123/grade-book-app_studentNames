class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def register_for_course(self, course, grade):
        self.courses_registered.append({'course': course, 'grade': grade})

    def calculate_GPA(self):
        if not self.courses_registered:
            self.GPA = 0.0
        else:
            total_credits = sum(course['course'].credits for course in self.courses_registered)
            total_points = sum(course['course'].credits * course['grade'] for course in self.courses_registered)
            self.GPA = total_points / total_credits

    def __repr__(self):
        return f"Student(email={self.email}, names={self.names}, GPA={self.GPA:.2f})"

