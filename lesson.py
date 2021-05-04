
class Lesson:
    def __init__(self, audience, class_type, school_week, day_of_week, num_of_class, student):
        self.__audience = audience
        self.__class_type = class_type
        self.__school_week = school_week
        self.__day_of_week = day_of_week
        self.__num_of_class = num_of_class
        self.__student_list = list()
        self.__student_list.append(student)


    def get_student_list(self):
        return self.__student_list






