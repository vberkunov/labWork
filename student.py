from lesson import Lesson



class Student:
    def __init__(self, name, surname, course, group_code):
        # if isinstance(name, str) and isinstance(surname, str) and \
        #         isinstance(course, int) and isinstance(group_code, str):
        self.__group_code = group_code
        self.__course = course
        self.__surname = surname
        self.__name = name


    def getCourse(self):
        return self.__course

    def getGroupCode(self):
        return self.__group_code

    def getSurname(self):
        return self.__surname

    def getName(self):
        return self.__name







