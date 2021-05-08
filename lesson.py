
class Lesson:
    def __init__(self, audience, class_type, school_week, day_of_week, num_of_class):
        self.__audience = audience
        self.__class_type = class_type
        self.__school_week = school_week
        self.__day_of_week = day_of_week
        self.__num_of_class = num_of_class

    def get_audience(self):
        return self.__audience

    def get_class_type(self):
        return self.__class_type

    def get_school_week(self):
        return self.__school_week

    def get_day_of_week(self):
        return self.__day_of_week

    def get_num_of_class(self):
        return self.__num_of_class





