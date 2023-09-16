import tkinter as tk
from tkinter import ttk
import executor


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # Settings
        default_font=("Comic", 9)
        
        # init Executor
        self.log = executor.Executor('lab_1_task_1', ['lab_1', 'lab_2', 'lab_3'], [15, 10, 15])

        # Window Settings
        self.geometry("600x325")
        self.resizable(False, False)

        # Choice lab work and task
        self.lab_work_cmb = ttk.Combobox(self, values=self.log.get_lab_works(), font=default_font)
        self.lab_work_cmb.grid(row=0, column=0, sticky="wesn")

        print(self.lab_work_cmb.get())

        self.task_cmb = ttk.Combobox(self, values=self.log.get_tasks(self.lab_work_cmb.get()), font=default_font)
        self.task_cmb.grid(row=0, column=1, sticky="wesn")

        self.lab_work_cmb.bind("<<ComboboxSelected>>", self.reset_task)

        # log consol frame
        self.consol_frame = tk.Frame(self)
        self.consol_frame.grid(row=1, column=0, columnspan=2, rowspan=3)

        # log consol
        self.name_lc = tk.Label(self.consol_frame, text="Log consol.", justify="left", font=default_font).grid(row=0, sticky="w")
        self.log_consol = tk.Entry(self.consol_frame).grid(row=1, rowspan=3, sticky="wesn")

        # button
        self.execute_btn = tk.Button(self, text="Execute", command=self.execute_task, font=default_font)
        self.execute_btn.grid(row=1, column=2, sticky="wesn")
        self.copy_btn = tk.Button(self, text="Copy", command=self.copy_task_code, font=default_font)
        self.copy_btn.grid(row=2, column=2, sticky="wesn")

        # configure settings
        self.grid_columnconfigure(0, minsize=200)
        self.grid_columnconfigure(1, minsize=200)
        self.grid_columnconfigure(2, minsize=200)
        self.consol_frame.grid_columnconfigure(0, minsize=400)
       # self.consol_frame.grid_rowconfigure(1, minsize=275)
        self.grid_rowconfigure(1, minsize=100)
        self.grid_rowconfigure(2, minsize=100)
     
        

    def reset_task(self, event=None):
        self.task_cmb["values"] = self.log.get_tasks(self.lab_work_cmb.get())
        self.task_cmb.set(1)
        print(self.lab_work_cmb.get())

    def execute_task(self):
        pass

    def copy_task_code(self):
        pass
    
    
if __name__ == '__main__':
    root = App()
    root.mainloop()
