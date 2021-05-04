from statistics import mean

from lesson import Lesson
from student import Student
from subject import Subject


class Info:
    def __init__(self):

        self.__subject_list = list()
        self.__i = 0
        self.__information = list()

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

    def check_subject(self, subject):
        for sub in self.__subject_list:
            if sub.get_subject() == subject.get_subject():
                print("+")
                return False
        return True

    def parse_data(self):
        for row in self.__information:
            student = Student(row[3], row[2], row[8], row[9])
            lesson = Lesson(row[0], row[1], row[5], row[6], row[7], student)
            subject = Subject(row[4], row[9], lesson, student)
            if self.check_subject(subject):
                self.__subject_list.append(subject)
            else:
                for sub in self.__subject_list:
                    if sub.get_subject() == subject:
                        sub.get_lesson_list().append(lesson)

    def processing(self):
        self.set_max_visit()
        for subject in self.__subject_list:
            self.get_pass_count(subject)

    def set_max_visit(self):
        for subject in self.__subject_list:
            subject.set_max_visit()

    def get_pass_count(self, subject):
        pass_subject = dict()
        for student in subject.get_subscriber_list():

            print(student.getSurname())
            pass_count = 0
            pass_dict = dict()
            for lesson in subject.get_lesson_list():

                if student not in lesson.get_student_list():
                    pass_count += 1
                pass_dict = dict({student.getSurname(): pass_count})
            pass_subject = dict({subject.get_subject(): pass_dict})
            print(pass_subject)
