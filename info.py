from lesson import Lesson
from lesson_plan import LessonPlan
from student import Student
from student_list import StudentList


class Info:
    def __init__(self, information: list = None):

        self.__i = 0
        self.__information = information
        self.__student_list = StudentList()

    def __iter__(self):
        return self

    def next(self):
        if self.__i < len(self.__information):
            self.__i += 1
            return self.__information[self.__i - 1]
        else:
            raise StopIteration

    def set_information(self, info):
        self.__information = info

    def print_all_info(self):
        for str1 in self.__information:
            print(str1)

    def clear(self):
        pass

    def info_count(self):

        return len(self.__information) - 1

    def lecture_count(self, i=0):

        for row in self.__information:
            if any('лекц.'.lower() in s.lower() for s in row):
                i += 1
        return i

    def check_student(self, student, lesson):
        list = self.__student_list.get_student_list()
        if len(list) == 0 or self.__student_list.exist(student) == False:
            self.__student_list.add_to_student_list(student)
        else:
            student_from_list = self.__student_list.get_student_by_name(student.getSurname(), student.getGroupCode())
            student_from_list.getLessonList().add_to_lesson_list(lesson)

    def parse_data(self):
        for row in self.__information:
            lesson_plan = LessonPlan(row[5], row[6])
            lesson = Lesson(row[0], row[1], row[4], row[7], lesson_plan)
            student = Student(row[3], row[2], row[8], row[9], lesson)
            self.check_student(student, lesson)

    def calculate(self):
        calculation = self.__student_list.get_pass_info_by_student()
        print(calculation)