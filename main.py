import tkinter as tk
from tkinter import ttk
import executor


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # init Executor
        self.log = executor.Executor('lab_1_task_1', ['lab_1', 'lab_2', 'lab_3'], [15, 10, 15])

        # Window Settings
        self.geometry("600x400")
        self.resizable(False, False)

        # Choice lab work and task
        self.lab_work_cmb = ttk.Combobox(self, values=self.log.get_lab_works())
        self.lab_work_cmb.grid(row=0, column=0, sticky="wesn")

        print(self.lab_work_cmb.get())

        self.task_cmb = ttk.Combobox(self, values=self.log.get_tasks(self.lab_work_cmb.get()))
        self.task_cmb.grid(row=0, column=1, sticky="wesn")

        self.lab_work_cmb.bind("<<ComboboxSelected>>", self.reset_task)

    def reset_task(self, event=None):
        self.task_cmb["values"] = self.log.get_tasks(self.lab_work_cmb.get())
        self.task_cmb.set(1)
        print(self.lab_work_cmb.get())


if __name__ == '__main__':
    root = App()
    root.mainloop()
