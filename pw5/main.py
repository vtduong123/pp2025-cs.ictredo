from domains import Student
from domains import Course
from domains.listing import Listing
import input as inp
import output as out


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
            student_id, student_name, dob = inp.input_student()
            student = Student(student_id, student_name, dob)
            school_listing.students.append(student)
            print("Student added successfully!")
        elif option == 2:
            course_id, course_name = inp.input_course()
            course = Course(course_id, course_name)
            school_listing.courses.append(course)
            print("Course added successfully!")
        elif option == 3:
            student_index, course_id, mark = inp.input_mark()
            if student_index is not None and course_id is not None:
                try:
                    school_listing.students[student_index].input_mark(course_id, mark)
                    print("Mark added successfully!")
                except IndexError:
                    print("Invalid student index!")
        elif option == 4:
            out.list_students(school_listing.students)
        elif option == 5:
            out.list_courses(school_listing.courses)
        else:
            print("Invalid option. Please try again!")


if __name__ == "__main__":
    main()
