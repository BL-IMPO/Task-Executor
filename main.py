import tkinter as tk
from tkinter import ttk
import os
# LOCAL
import executor
from Lab_Works.settings import *


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # Settings
        img = tk.PhotoImage(file=os.path.dirname(os.path.abspath(__file__)) + "\gear.png")
        default_font = ("Comic", 9)

        # init Executor
        self.log = executor.Executor(LAB_WORKS, TASKS)

        # Window Settings
        self.geometry("600x260")
        self.resizable(False, False)
        self.title("Task-Executor")
        self.iconphoto(False, img)

        # Choice lab work and task
        self.lab_work_cmb = ttk.Combobox(self, values=self.log.get_lab_works(), font=default_font)
        self.lab_work_cmb.grid(row=0, column=0, sticky="wesn")
        self.lab_work_cmb.set("lab_1")

        self.task_cmb = ttk.Combobox(self, values=self.log.get_tasks(self.lab_work_cmb.get()), font=default_font)
        self.task_cmb.grid(row=0, column=1, sticky="wesn")
        self.task_cmb.set(1)

        self.lab_work_cmb.bind("<<ComboboxSelected>>", self.reset_task)

        # log console frame
       #self.console_frame = tk.Frame(self)
       #self.console_frame.grid(row=1, column=0, columnspan=2, rowspan=3)

        # log console
        #self.name_lc = (tk.Label(self, text="Log consol.", justify="left", font=default_font))
        #self.name_lc.grid(row=1, sticky="w")
        #self.log_console = tk.Entry(self)
        #self.log_console.grid(row=2, sticky="wesn", column=0, columnspan=2)
        ##self.log_console.configure(state="disabled")

        # button
        self.execute_btn = tk.Button(self, text="Execute", command=self.execute_task, font=default_font)
        self.execute_btn.grid(row=3, column=2, sticky="wesn")
        self.copy_btn = tk.Button(self, text="Copy", command=self.copy_task_code, font=default_font)
        self.copy_btn.grid(row=4, column=2, sticky="wesn")

        # configure settings
        self.grid_columnconfigure(0, minsize=200)
        self.grid_columnconfigure(1, minsize=200)
        self.grid_columnconfigure(2, minsize=200)
        #self.console_frame.grid_columnconfigure(0, minsize=400)
        #self.console_frame.grid_rowconfigure(1, minsize=275)
        #self.grid_rowconfigure(1, minsize=100)
        self.grid_rowconfigure(3, minsize=100)
        self.grid_rowconfigure(4, minsize=100)

    def reset_task(self, event=None):
        self.task_cmb["values"] = self.log.get_tasks(self.lab_work_cmb.get())
        self.task_cmb.set(1)

    def file_name(self) -> str:
        return self.lab_work_cmb.get() + '_task_' + self.task_cmb.get() + '.py'

    def execute_task(self):
        self.log.execute(self.file_name())

    def copy_task_code(self):
        try:
            self.log.copying(self.file_name())
        except FileNotFoundError:
            print("Chose wrong file!")


if __name__ == '__main__':
    root = App()
    root.mainloop()