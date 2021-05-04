class Subject:
    def __init__(self, subject, group_code, lesson, subscriber, max_visit=0, average_pass=0):
        self.__subject = subject
        self.__group_code = group_code
        self.__lesson_list = list()
        self.__lesson_list.append(lesson)
        self.__subscribers = list()
        if subscriber.getSurname() in self.__subscribers:
            self.__subscribers.append(subscriber)
        self._max_visit = max_visit
        self.__average_pass = average_pass

    def get_subject(self):
        return self.__subject

    def get_lesson_list(self):
        return self.__lesson_list

    def get_subscriber_list(self):
        return set(self.__subscribers)

    def get_max_visit(self):
        return len(self.__lesson_list)

    def set_max_visit(self):
        self._max_visit = len(self.__lesson_list)
