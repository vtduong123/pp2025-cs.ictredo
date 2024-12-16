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
