from lesson_list import LessonList


class Student:
    def __init__(self, name, surname, course, group_code, lesson):
        # if isinstance(name, str) and isinstance(surname, str) and \
        #         isinstance(course, int) and isinstance(group_code, str):
        self.__group_code = group_code
        self.__course = course
        self.__surname = surname
        self.__name = name
        self.__lesson_list = LessonList()
        self.__lesson_list.add_to_lesson_list(lesson)

    def getCourse(self):
        return self.__course

    def getGroupCode(self):
        return self.__group_code

    def getSurname(self):
        return self.__surname

    def getName(self):
        return self.__name

    def getLessonList(self):
        return self.__lesson_list

    def check_for_passes(self):
        global less_dict
        for lesson in self.__lesson_list.get_lesson_list():
            if lesson.calc_pass > 0:
                less_dict = {'lesson': lesson.getSubject(), 'pass': lesson.calc_pass()}
        return less_dict
