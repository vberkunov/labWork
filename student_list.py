from student import Student


class StudentList:
    def __init__(self):
        self.__i = 0
        self.__student_list = []

    def __iter__(self):
        return self

    def get_student_list(self):
        return self.__student_list

    def next(self):
        if self.__i < len(self.__student_list):
            self.__i += 1
            return self.__student_list[self.__i - 1]
        else:
            raise StopIteration

    def add_to_student_list(self, student: Student):
        self.__student_list.append(student)

    def get_list_size(self):
        return len(self.__student_list) - 1

    def get_student_by_name(self, sname, group):


        for x in self.__student_list:
            if x.getSurname() == sname and x.getGroupCode() == group:
                return x

    def exist(self, student):
        for x in self.__student_list:

            if x.getSurname() == student.getSurname() and x.getGroupCode() == student.getGroupCode():
                return True
            else:
                return False



    def get_pass_info_by_student(self):
        global student_dict
        for student in self.__student_list:
            student_dict = student.check_for_passes()
        return student_dict