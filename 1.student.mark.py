def input_number_of_units(entity):
    """Function to input the number of units (e.g., students, courses)."""
    while True:
        try:
            count = int(input(f"Enter the number of {entity}: "))
            if count > 0:
                return count
            else:
                print("The number must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def input_student_info():
    """Function to input student information."""
    student = {
        'id': input("Enter Student ID: "),
        'name': input("Enter Student Name: "),
        'DoB': input("Enter Student Date of Birth (DoB): "),
        'marks': {}
    }
    return student

def input_course_info():
    """Function to input course information."""
    return {
        'id': input("Enter Course ID: "),
        'name': input("Enter Course Name: ")
    }

def input_mark(student):
    """Function to input marks for a student."""
    try:
        course_id = input("Enter Course ID to enter mark for the student: ")
        mark = float(input("Enter Mark for the student: "))
        student["marks"][course_id] = mark
    except ValueError:
        print("Invalid mark. Please enter a number.")

def list_students(students):
    """Function to list all students."""
    if not students:
        print("There aren't any students yet.")
    else:
        print("Here is the student list:")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student['id']} - {student['name']} - {student['DoB']}")
            if student["marks"]:
                print("  Marks (Course ID - Mark):", student["marks"])

def list_courses(courses):
    """Function to list all courses."""
    if not courses:
        print("There aren't any courses yet.")
    else:
        print("Here is the course list:")
        for i, course in enumerate(courses, 1):
            print(f"{i}. {course['id']} - {course['name']}")

def main():
    """Main function."""
    courses = []
    students = []

    while True:
        print("""
        0. Exit
        1. Add Student
        2. Add Course
        3. Input Mark for Student
        4. List Students
        5. List Courses
        """)
        try:
            option = int(input("Your choice: "))
            if option == 0:
                print("Exiting the program. Goodbye!")
                break
            elif option == 1:
                students.append(input_student_info())
            elif option == 2:
                courses.append(input_course_info())
            elif option == 3:
                if not students:
                    print("No students available. Please add students first.")
                else:
                    student_index = int(input("Enter student index to enter mark: ")) - 1
                    if 0 <= student_index < len(students):
                        input_mark(students[student_index])
                    else:
                        print("Invalid student index.")
            elif option == 4:
                list_students(students)
            elif option == 5:
                list_courses(courses)
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid option.")

if __name__ == "__main__":
    main()
