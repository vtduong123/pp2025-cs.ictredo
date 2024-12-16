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