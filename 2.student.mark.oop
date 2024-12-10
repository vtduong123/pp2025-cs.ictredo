class Student:
    def __init__(self, student_id, name, dob):
        # Create a student with basic details and an empty marks dictionary
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}

    def add_mark(self, course_id, mark):
        # Add or update a mark for a course
        self.__marks[course_id] = mark

    def get_details(self):
        # Return a dictionary of student info
        return {
            "id": self.__id,
            "name": self.__name,
            "dob": self.__dob,
            "marks": self.__marks
        }


class Course:
    def __init__(self, course_id, name):
        # Create a course with an ID and a name
        self.id = course_id
        self.name = name

    def get_details(self):
        # Return a dictionary of course info
        return {
            "id": self.id,
            "name": self.name
        }


class SchoolManagement:
    def __init__(self):
        # Initialize empty lists for students and courses
        self.students = []
        self.courses = []

    def add_student(self):
        # Get student info from the user and add it to the list
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dob = input("Enter Date of Birth: ")
        self.students.append(Student(student_id, name, dob))
        print("Student added successfully!")

    def add_course(self):
        # Get course info from the user and add it to the list
        course_id = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        self.courses.append(Course(course_id, name))
        print("Course added successfully!")

    def assign_mark(self):
        # Assign a mark to a student for a specific course
        if not self.students:
            print("No students available. Add some students first!")
            return
        if not self.courses:
            print("No courses available. Add some courses first!")
            return

        self.list_students()
        try:
            student_index = int(input("Choose a student by number: ")) - 1
            if student_index < 0 or student_index >= len(self.students):
                print("Invalid student number!")
                return

            self.list_courses()
            course_id = input("Enter Course ID: ")
            mark = float(input("Enter the mark: "))
            self.students[student_index].add_mark(course_id, mark)
            print("Mark assigned successfully!")
        except ValueError:
            print("Invalid input. Please try again!")

    def list_students(self):
        # Show all students
        if not self.students:
            print("No students to show.")
        else:
            print("\nStudent List:")
            for i, student in enumerate(self.students, 1):
                details = student.get_details()
                print(f"{i}. ID: {details['id']} - Name: {details['name']} - DoB: {details['dob']}")
                if details["marks"]:
                    print("   Marks:", details["marks"])

    def list_courses(self):
        # Show all courses
        if not self.courses:
            print("No courses to show.")
        else:
            print("\nCourse List:")
            for i, course in enumerate(self.courses, 1):
                details = course.get_details()
                print(f"{i}. ID: {details['id']} - Name: {details['name']}")


def main():
    # Main program loop
    school = SchoolManagement()

    while True:
        print("""
        0. Exit
        1. Add Student
        2. Add Course
        3. Assign Mark to a Student
        4. Show All Students
        5. Show All Courses
        """)
        try:
            choice = int(input("Pick an option: "))
            if choice == 0:
                print("Goodbye!")
                break
            elif choice == 1:
                school.add_student()
            elif choice == 2:
                school.add_course()
            elif choice == 3:
                school.assign_mark()
            elif choice == 4:
                school.list_students()
            elif choice == 5:
                school.list_courses()
            else:
                print("Invalid option. Try again!")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
