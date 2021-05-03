
import sys

from info import Info
from load import Builder
from settings_loader import SettingLoader


def executor_info():
    print("Я виконавець цієї роботи Варіант №5")


def laboratory_condition():
    print("Варіант та умова ЛР")


def print_error():
    print("***** program aborted *****")


def process(path):
    # try:
    settings = SettingLoader()
    settings.load_ini(path)
    if settings.check_settings():
        info = Info()
        builder = Builder()
        builder.load(info, settings.get_path_csv(), settings.get_path_json(), settings.get_encoding())
        info.parse_data()
        info.calculate()


# except Exception:
#     print_error()


if __name__ == '__main__':
    executor_info()
    laboratory_condition()
    print("***********************************")
    if len(sys.argv) == 1:
        print_error()
    if len(sys.argv) > 2:
        print_error()
    if len(sys.argv) == 2:
        process(sys.argv[1])
