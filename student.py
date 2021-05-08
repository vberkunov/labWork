from lesson import Lesson


class Student:
    def __init__(self, name, surname, course, group_code, subject):
        # if isinstance(name, str) and isinstance(surname, str) and \
        #         isinstance(course, int) and isinstance(group_code, str):
        self.__group_code = group_code
        self.__course = course
        self.__surname = surname
        self.__name = name
        self.__subject_list = list()
        self.__subject_list.append(subject)

    def get_course(self):
        return self.__course

    def get_group_code(self):
        return self.__group_code

    def get_surname(self):
        return self.__surname

    def get_name(self):
        return self.__name

    def get_subject_list(self):
        return self.__subject_list

    def calculate_pass(self) -> int:
        count_of_pass: int = 0
        for subject in self.__subject_list:
            count_of_pass += subject.count_of_pass_lesson()
        return count_of_pass



