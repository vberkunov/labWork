from lesson_plan import LessonPlan
from lesson_plan_list import LessonPlanList


class Lesson:
    def __init__(self, audience, lesson_type, subject, num_of_class, lesson_plan: LessonPlan):
        self.__num_of_class = num_of_class
        self.__lesson_plan = LessonPlanList()
        self.__lesson_plan.add_to_lesson_plan_list(lesson_plan)
        self.__subject = subject
        self.__lesson_type = lesson_type
        self.__audience = audience
        self.__max_day = 5
        self.__max_week = 19

    def getSubject(self):
        return self.__subject

    def getLessonType(self):
        return self.__lesson_type

    def calc_all_lesson(self):
        return self.__max_day * self.__max_week

    def calc_num_of_visit(self):
        return self.__lesson_plan.get_list_size()

    def calc_pass(self):
        num_of_lessons: int = self.calc_all_lesson()
        num_of_visit: int = self.calc_num_of_visit()

        if num_of_visit > (num_of_lessons / 2):
            return num_of_lessons - num_of_visit
        else:
            return 0
