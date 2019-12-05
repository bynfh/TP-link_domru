import tkinter as tk

class Window(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_first_field()
        master.title('Прошиватор TP-Link-2600')
        master.geometry('650x450+300+200')
        master.grab_set()

    def create_first_field(self):
        self.button_proshivk = tk.Button(self, text='Прошить', bg='white',fg='red',font='arial 14')
        self.button_proshivk.bind('<Button-1>', self.say_hi())
        self.button_proshivk.grid(row = 1, column = 0)
        self.label_first = tk.Label(self, text='Прошить')
        self.label_first.grid(row = 1, column = 1)

    def say_hi(self):
        print("hi there, everyone!")