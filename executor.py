import pyperclip
import subprocess
import os


class Executor:

    def __init__(self, lab_works: list[str], tasks: list[int]):

        self.lab_works = self._init_dict(lab_works, tasks)

    def _init_dict(self, lab_works: list[str], tasks: list[int]):
        lab = dict()
        for i in range(len(lab_works)):
            lab[lab_works[i]] = [str(i) for i in range(1, tasks[i] + 1)]

        return lab

    def execute(self, file_name: str):
        if os.name == "nt":
            print("{} S-T-A-R-T {}".format("*" * 8, "*" * 9))
            subprocess.run(["python", self.get_path() + file_name])
            print("{} F-I-N-I-S-H {}".format("*" * 8, "*" * 8))
        elif os.name == "posix":
            print("{} S-T-A-R-T {}".format("*" * 8, "*" * 8))
            subprocess.run(["python3", self.get_path() + file_name])
            print("{} F-I-N-I-S-H {}".format("*" * 8, "*" * 8))

    def copying(self, file_name: str):
        self.get_path()
        with open(file_name, 'r') as text:
            pyperclip.copy(''.join(text.readlines()))

    def get_path(self) -> str:
        path = os.path.dirname(os.path.abspath(__file__)) + '/Lab_Works/'
        os.chdir(path)

        return path

    def get_lab_works(self) -> list:
        return list(self.lab_works.keys())

    def get_tasks(self, lab_work: str) -> list:
        try:
            return list(self.lab_works[lab_work])
        except KeyError:
            return ['']

#
# if __name__ == '__main__':
#    n = Executor(['lab_1', 'lab_2', 'lab_3'], [15, 10, 15])
#    print(n.get_lab_works())
#    print(n.get_tasks('lab_1'))
#    n.copying('lab_1_task_1.py')
#    n.execute('lab_1_task_1.py')
#    n.set_file = 'lab_1_task_2'

