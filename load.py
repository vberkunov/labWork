import csv
import json

from info import Info


class Builder:
    def __init__(self, row_num=0, lecture_num=0):
        self.__row_num = row_num
        self.__lecture_num = lecture_num

    def load_data(self, info: Info, csv_path: str, encoding: str):
        print("Завантажуємо основний файл")
        arr2 = []
        try:
            with open(csv_path, newline='', encoding=encoding) as f:
                reader = csv.reader(f)
                for row in reader:
                    curr_row = row[0].split(';')
                    arr2.extend([curr_row])
                info.set_information(arr2)
                print("input-csv <" + csv_path + ">: OK")
        except Exception:
            print("***** program aborted *****")
            print("Problem in load data")

    def load_stat(self, json_path: str, encoding: str):
        print("Завантажуємо додатковий файл")
        try:
            with open(json_path, 'r', encoding=encoding) as f:
                text = json.load(f)
                self.__lecture_num = text['кількість лекцій']
                self.__row_num = text['кількість записів']
                print("input-json <" + json_path + ">: OK")
        except Exception:
            print("***** program aborted *****")
            print("Problem in load stat")

    def fit(self, info: Info):
        if info.lecture_count() == self.__lecture_num and info.info_count() == self.__row_num:
            return True
        else:
            return False

    def load(self, info: Info, csv_path: str, json_path: str, encoding: str):
        print("Завантажуємо основні файли")
        self.load_data(info, csv_path, encoding)
        self.load_stat(json_path, encoding)
        if self.fit(info):
            print("json?=csv: OK")
        else:
            print("json?=csv: UPS")
