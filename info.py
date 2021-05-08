from statistics import mean

from lesson import Lesson
from output import Output
from student import Student
from subject import Subject


class Info:
    def __init__(self):

        self.__student_list = list()
        self.__i = 0
        self.__information = list()
        self.__average_pass = 0;

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

    def check_student(self, s: Student):
        for student in self.__student_list:
            if student.get_surname() == s.get_surname() and student.get_group_code() == s.get_group_code():
                return False
        return True

    def parse_data(self):
        for row in self.__information:
            lesson = Lesson(row[0], row[1], row[5], row[6], row[7])
            subject = Subject(row[4], row[9], lesson)
            student = Student(row[3], row[2], row[8], row[9], subject)
            if self.check_student(student):
                self.__student_list.append(student)
            else:
                for stud in self.__student_list:
                    if stud.get_surname() == student.get_surname() and stud.get_group_code() == student.get_group_code():
                        stud.get_subject_list().append(subject)

    def processing(self):
        self.check_average_pass()
        self.check_visit()

    def check_average_pass(self):
        max_pass: int = 0
        for stud in self.__student_list:
            max_pass += stud.calculate_pass()
        self.__average_pass = max_pass / len(self.__student_list)

    def check_visit(self):
        for stud in self.__student_list:
            if stud.calculate_pass() < self.__average_pass:
                self.print_student_info(stud)
                self.print_lesson_info(stud)

    def print_student_info(self, stud):
        print(stud.get_surname() + " " + stud.get_name() + " " + str(stud.calculate_pass()) + " " + str(
            round(self.__average_pass, 1)))

    def print_lesson_info(self, stud):
        out_list = []
        for subject in stud.get_subject_list():
            for lesson in subject.get_lesson_list():
                output = Output(lesson.get_school_week(), lesson.get_day_of_week(),
                                lesson.get_num_of_class(), lesson.get_audience(),
                                subject.get_subject(), lesson.get_class_type())
                out_list.append(output)
        sorted(out_list, key=lambda out: out.get_class_type())
        sorted(out_list, key=lambda out: out.get_subject())
        sorted(out_list, key=lambda out: out.get_school_week())
        sorted(out_list, key=lambda out: out.get_day_of_week())
        sorted(out_list, key=lambda out: out.get_num_of_class())
        for el in out_list:
            el.print()
