import pyperclip
import os
import Lab_Works.lab_1_task_1 as l1t1


class Executor:

    def __init__(self, file_name: str, lab_works: list[str], tasks: list[int]):

        self._file_name = str(file_name)
        self.lab_works = self._init_dict(lab_works, tasks)

    def _init_dict(self, lab_works: list[str], tasks: list[int]):
        lab = dict()
        for i in range(len(lab_works)):
            lab[lab_works[i]] = [str(i) for i in range(1, tasks[i] + 1)]

        return lab

    def execute(self):
        if self.file_name == 'lab_1_task_1':
            l1t1.lab_1_task_1()

    def copying(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '/Lab_Works'
        os.chdir(path)
        with open(self.file_name + '.py', 'r') as text:
            pyperclip.copy(''.join(text.readlines()))

    def get_lab_works(self):
        return list(self.lab_works.keys())

    def get_tasks(self, lab_work: str):
        try:
            return list(self.lab_works[lab_work])
        except:
            return [' ']
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def set_file(self, name):
        self._file_name = name

if __name__ == '__main__':
    n = Executor('lab_1_task_1', ['lab_1', 'lab_2', 'lab_3'], [15, 10, 15])
    print(n.get_lab_works())
    print(n.get_tasks('lab_1'))
    #n.copying()
    n.execute()
    print(n.file_name)
    n.set_file = 'lab_1_task_2'
    print(n.file_name)
