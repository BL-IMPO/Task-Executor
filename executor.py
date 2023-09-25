import pyperclip
import subprocess
import os

from Lab_Works.settings import *


class Executor:

    def __init__(self):
        self.path = ""
        self.get_path()
        self.lab_works = dict()
        self._init_dict()

    def _init_dict(self):
        """
        Closed method of class. It's needed to initialize dict for "get_lab_works" and "get_tasks" methods.

        :return:
        """
        self.lab_works = dict()
        for i in range(len(LAB_WORKS)):
            self.lab_works[LAB_WORKS[i]] = TASKS[i]

    def execute(self, file_name: str):
        """
        Execute selected file. If os is Linux or Windows file will be launched.

        :param file_name:
        :return:
        """
        if os.name == "nt":
            print("{} S-T-A-R-T {}".format("*" * 8, "*" * 9))
            subprocess.run(["python", self.path + file_name])
            print("{} F-I-N-I-S-H {}".format("*" * 8, "*" * 8))
        elif os.name == "posix":
            print("{} S-T-A-R-T {}".format("*" * 8, "*" * 8))
            subprocess.run(["python3", self.path + file_name])
            print("{} F-I-N-I-S-H {}".format("*" * 8, "*" * 8))

    def copying(self, file_name: str):
        """
        Copy selected file to clipboard.

        :param file_name:
        :return:
        """
        self.get_path()
        with open(file_name, 'r') as text:
            pyperclip.copy(''.join(text.readlines()))

    def get_path(self):
        """
        Return path to the Lab_Works directory.

        :return:
        """
        self.path = os.path.dirname(os.path.abspath(__file__)) + '/Lab_Works/'
        os.chdir(self.path)

    def get_lab_works(self) -> list:
        """
        Return lab works list.

        :return:
        """
        return list(self.lab_works.keys())

    def get_tasks(self, lab_work: str) -> list:
        """
        Return tasks for selected lab work.

        :param lab_work:
        :return:
        """
        try:
            return list(self.lab_works[lab_work])
        except KeyError:
            return ['']
