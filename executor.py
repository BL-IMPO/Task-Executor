import pyperclip
import os
import Lab_Works.lab_1_task_1 as l1t1


class Executor:

    def __init__(self, file_name):
        self.file_name = file_name

    def execute(self):
        if self.file_name == 'lab_1_task_1':
            l1t1.lab_1_task_1()

    def copying(self):
        path = os.path.dirname(os.path.abspath(__file__)) + '/Lab_Works'
        os.chdir(path)
        with open(self.file_name + '.py', 'r') as text:
            pyperclip.copy(''.join(text.readlines()))


if __name__ == '__main__':
    n = Executor('lab_1_task_1')
    n.copying()
    n.execute()