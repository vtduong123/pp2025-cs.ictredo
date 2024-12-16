import math

class Student:
    def __init__(self, student_id, student_name, dob):
        self.__id = student_id
        self.__name = student_name
        self.__DOB = dob
        self.__marks = {}

    def input_mark(self, course_id, mark):
        # Round mark to 1 decimal place
        self.__marks[course_id] = round(mark, 1)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__DOB

    def get_marks(self):
        return self.__marks


class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name


class Listing:
    def __init__(self):
        self.students = []
        self.courses = []

    def list_students(self):
        if not self.students:
            print("No students to display!")
        else:
            print("\nStudent List:")
            for i, student in enumerate(self.students):
                print(f"{i + 1}. ID: {student.get_id()} - Name: {student.get_name()} - DoB: {student.get_dob()}")
                if student.get_marks():
                    print(f"   Marks (Course Id - Mark): {student.get_marks()}")

    def list_courses(self):
        if not self.courses:
            print("No courses to display!")
        else:
            print("\nCourse List:")
            for i, course in enumerate(self.courses):
                print(f"{i + 1}. ID: {course.id} - Name: {course.name}")


def main():
    school_listing = Listing()

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Input Mark for Student")
        print("4. List Students")
        print("5. List Courses")
        print("0. Exit")

        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 0:
            print("Exiting the program. Goodbye!")
            break
        elif option == 1:
            student_id = input("Enter Student ID: ").strip()
            student_name = input("Enter Student Name: ").strip()
            dob = input("Enter Student Date of Birth (DoB): ").strip()
            student = Student(student_id, student_name, dob)
            school_listing.students.append(student)
            print("Student added successfully!")
        elif option == 2:
            course_id = input("Enter Course ID: ").strip()
            course_name = input("Enter Course Name: ").strip()
            course = Course(course_id, course_name)
            school_listing.courses.append(course)
            print("Course added successfully!")
        elif option == 3:
            try:
                student_index = int(input("Enter student index to enter mark: ")) - 1
                if student_index < 0 or student_index >= len(school_listing.students):
                    print("Invalid student index!")
                    continue
                course_id = input("Enter Course ID to enter mark for the student: ").strip()
                mark = float(input("Enter Mark for the student: "))
                school_listing.students[student_index].input_mark(course_id, mark)
                print("Mark added successfully!")
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")
        elif option == 4:
            school_listing.list_students()
        elif option == 5:
            school_listing.list_courses()
        else:
            print("Invalid option. Please try again!")


if __name__ == "__main__":
    main()