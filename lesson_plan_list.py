from lesson_plan import LessonPlan


class LessonPlanList:
    def __init__(self):
        self.__i = 0
        self.__lesson_plan_list = []

    def __iter__(self):
        return self

    def get_lesson_plan_list(self):
        return self.__lesson_plan_list

    def next(self):
        if self.__i < len(self.__lesson_plan_list):
            self.__i += 1
            return self.__lesson_plan_list[self.__i - 1]
        else:
            raise StopIteration

    def add_to_lesson_plan_list(self, lesson_plan: LessonPlan):
        self.__lesson_plan_list.append(lesson_plan)

    def get_list_size(self):
        return len(self.__lesson_plan_list) - 1
