def list_students(students):
    if not students:
        print("No students to display!")
    else:
        print("\nStudent List:")
        for i, student in enumerate(students):
            print(f"{i + 1}. ID: {student.get_id()} - Name: {student.get_name()} - DoB: {student.get_dob()}")
            if student.get_marks():
                print(f"   Marks (Course Id - Mark): {student.get_marks()}")


def list_courses(courses):
    if not courses:
        print("No courses to display!")
    else:
        print("\nCourse List:")
        for i, course in enumerate(courses):
            print(f"{i + 1}. ID: {course.id} - Name: {course.name}")
