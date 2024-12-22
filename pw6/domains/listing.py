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
