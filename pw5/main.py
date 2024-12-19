import os
import gzip
import json
from domains import Student
from domains import Course
from domains.listing import Listing
import input as inp
import output as out


def compress_files():
    """Compress students.txt, courses.txt, and marks.txt into students.dat."""
    with gzip.open("students.dat", "wb") as archive:
        data = {
            "students": open("students.txt", "r").read() if os.path.exists("students.txt") else "",
            "courses": open("courses.txt", "r").read() if os.path.exists("courses.txt") else "",
            "marks": open("marks.txt", "r").read() if os.path.exists("marks.txt") else "",
        }
        archive.write(json.dumps(data).encode("utf-8"))
    print("Files compressed into students.dat.")


def decompress_files():
    """Decompress students.dat and load data into memory."""
    if os.path.exists("students.dat"):
        with gzip.open("students.dat", "rb") as archive:
            data = json.loads(archive.read().decode("utf-8"))
        # Write the decompressed data back to the original files
        with open("students.txt", "w") as f:
            f.write(data.get("students", ""))
        with open("courses.txt", "w") as f:
            f.write(data.get("courses", ""))
        with open("marks.txt", "w") as f:
            f.write(data.get("marks", ""))
        print("Data decompressed and loaded from students.dat.")


def load_data(school_listing):
    """Load data from students.txt, courses.txt, and marks.txt into memory."""
    # Load students
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                student_id, student_name, dob = line.strip().split(",")
                student = Student(student_id, student_name, dob)
                school_listing.students.append(student)

    # Load courses
    if os.path.exists("courses.txt"):
        with open("courses.txt", "r") as f:
            for line in f:
                course_id, course_name = line.strip().split(",")
                course = Course(course_id, course_name)
                school_listing.courses.append(course)

    # Load marks
    if os.path.exists("marks.txt"):
        with open("marks.txt", "r") as f:
            for line in f:
                student_index, course_id, mark = line.strip().split(",")
                student_index = int(student_index)
                mark = float(mark)
                school_listing.students[student_index].input_mark(course_id, mark)


def main():
    # Decompress data if students.dat exists
    decompress_files()

    # Initialize school listing and load data from text files
    school_listing = Listing()
    load_data(school_listing)

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
            # Compress files before exiting
            compress_files()
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
