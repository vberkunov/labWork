class Output:
    def __init__(self, school_week, day_of_week, num_of_class, audience, subject, class_type):
        self.__class_type = class_type
        self.__subject = subject
        self.__audience = audience
        self.__num_of_class = num_of_class
        self.__day_of_week = day_of_week
        self.__school_week = school_week

    def get_class_type(self):
        return self.__class_type

    def get_subject(self):
        return self.__subject

    def get_audience(self):
        return self.__audience

    def get_num_of_class(self):
        return self.__num_of_class

    def get_day_of_week(self):
        return self.__day_of_week

    def get_school_week(self):
        return self.__school_week

    def print(self):
        print(
              self.__school_week + self.__day_of_week
              + self.__num_of_class + self.__audience
              + self.__subject + self.__class_type)
