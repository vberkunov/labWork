class Subject:
    def __init__(self, subject, group_code, lesson):
        self.__subject = subject
        self.__group_code = group_code
        self.__lesson_list = list()
        self.__lesson_list.append(lesson)

    def get_subject(self):
        return self.__subject

    def get_lesson_list(self):
        return self.__lesson_list

    def count_of_pass_lesson(self):
        return len(self.__lesson_list)

