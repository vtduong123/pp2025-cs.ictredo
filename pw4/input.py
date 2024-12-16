def input_student():
    student_id = input("Enter Student ID: ").strip()
    student_name = input("Enter Student Name: ").strip()
    dob = input("Enter Student Date of Birth (DoB): ").strip()
    return student_id, student_name, dob


def input_course():
    course_id = input("Enter Course ID: ").strip()
    course_name = input("Enter Course Name: ").strip()
    return course_id, course_name


def input_mark():
    try:
        student_index = int(input("Enter student index to enter mark: ")) - 1
        course_id = input("Enter Course ID to enter mark for the student: ").strip()
        mark = float(input("Enter Mark for the student: "))
        return student_index, course_id, mark
    except ValueError:
        print("Invalid input. Please try again.")
        return None, None, None
