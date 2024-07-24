from gradebook import GradeBook

def main():
    grade_book = GradeBook()

    while True:
        print("\nMenu:")
        print("1. Add student")
        print("2. Add course")
        print("3. Register student for course")
        print("4. Calculate GPA")
        print("5. Calculate ranking")
        print("6. Search by grade")
        print("7. Generate transcript")
        print("8. Print all students")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            grade_book.add_student(email, names)
            print("\nStudent added successfully.")
            grade_book.print_all_students()
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            grade_book.add_course(name, trimester, credits)
            print("\nCourse added successfully.")
        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            grade_book.register_student_for_course(student_email, course_name, grade)
            print("\nStudent registered for course successfully.")
            grade_book.print_all_students()
        elif choice == '4':
            grade_book.calculate_GPA()
            print("\nGPA calculated successfully.")
            grade_book.print_all_students()
        elif choice == '5':
            grade_book.calculate_ranking()
            print("\nRanking calculated successfully.")
        elif choice == '6':
            min_grade = float(input("Enter minimum grade: "))
            max_grade = float(input("Enter maximum grade: "))
            grade_book.search_by_grade(min_grade, max_grade)
        elif choice == '7':
            student_email = input("Enter student email: ")
            grade_book.generate_transcript(student_email)
        elif choice == '8':
            grade_book.print_all_students()
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

