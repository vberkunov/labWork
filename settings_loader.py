import json
import re


class SettingLoader:

    def __init__(self, path_csv="none", path_json="none", encoding="none"):
        self.__path_csv = path_csv
        self.__path_json = path_json
        self.__encoding = encoding

    def set_path_csv(self, value):
        self.__path_csv = value

    def set_path_json(self, value):
        self.__path_json = value

    def set_encoding(self, value):
        self.__encoding = value

    def get_path_csv(self):
        return self.__path_csv

    def get_path_json(self):
        return self.__path_json

    def get_encoding(self):
        return self.__encoding

    def load_ini(self, path):
        print("Читаємо файл з налаштуваннями")
        with open(path, 'r', encoding='utf-8') as f:
            text = json.load(f)
            self.__path_csv = text['input']['csv']
            self.__path_json = text['input']['json']
            self.__encoding = text['input']['encoding']

    def check_settings(self):
        if self.__path_csv != "none" and self.__path_json != "none" and self.__encoding != "none":
            return True
        else:
            return False

    def check_nlecroom(self, nlecroom):
        try:
            int(nlecroom) and nlecroom > 0
            return True
        except ValueError:
            return False

    def check_toccupation(self, toccupation):
        s = ['лекц.', 'п', 'Seminar', 'лаб.']
        if toccupation in s:
            return True
        else:
            return False

    def check_name(self, name):
        if re.compile("/^[a-z ,.'-]+$/i").match(name) and 4 <= len(name) <= 29:
            return True
        else:
            return False

    def check_subject(self, subject):
        if isinstance(subject, str) and 4 <= len(subject) <= 28:
            return True
        else:
            return False

    def check_nweek(self, nweek):
        try:
            int(nweek) and 1 <= len(nweek) <= 19
            return True
        except ValueError:
            return False

    def check_nday(self, nday):
        try:
            int(nday) and 1 <= len(nday) <= 5
            return True
        except ValueError:
            return False

    def check_nclass_cource(self, value):
        try:
            int(value) and 1 <= len(value) <= 4
            return True
        except ValueError:
            return False

    def check_ngroup(self, ncource, ngroup):
        if re.compile("\w{2,3}-\d[%d]\d{1,2}" % ngroup).match(ncource):
            return True
        else:
            return False
