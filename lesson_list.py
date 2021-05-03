from lesson import Lesson


class LessonList:
    def __init__(self):
        self.__i = 0
        self.__lesson_list = []

    def __iter__(self):
        return self

    def get_lesson_list(self):
        return self.__lesson_list

    def next(self):
        if self.__i < len(self.__lesson_list):
            self.__i += 1
            return self.__lesson_list[self.__i - 1]
        else:
            raise StopIteration

    def add_to_lesson_list(self, lesson: Lesson):
            self.__lesson_list.append(lesson)

    def get_list_size(self):
        return len(self.__lesson_list) - 1



