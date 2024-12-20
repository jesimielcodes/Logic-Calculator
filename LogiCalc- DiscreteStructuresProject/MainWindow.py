from tkinter import *
import os

def open_basic_calculator():
    os.system("python basicCalculator.py")

def open_complex_calculator():
    os.system("python complexCalculator.py")

mainwindow = Tk()
mainwindow.title("Logic Calculator")

height = 400
width = 300
x = (mainwindow.winfo_screenwidth() // 2) - (width // 2)
y = (mainwindow.winfo_screenheight() // 2) - (height // 2)
mainwindow.geometry('{}x{}+{}+{}'.format(width, height, x, y))
mainwindow.config(bg="#808080")
mainwindow.overrideredirect(False)

welcome_label = Label(mainwindow, text='WELCOME\n\nplease select a mode', bg='#808080', font=("Trebuchet Ms", 15, "bold"), fg='#FFFFFF')
welcome_label.pack(pady=30)

basic_calculator = Button(mainwindow, text="Basic", font=("Trebuchet Ms", 13), command = open_basic_calculator, width = 20, bg="#108cff", fg="#FFFFFF")
basic_calculator.pack(pady=20)

complex_calculator = Button(mainwindow, text="Complex", font=("Trebuchet Ms", 13), command = open_complex_calculator, width = 20, bg="#108cff", fg="#FFFFFF")
complex_calculator.pack(pady=20)

mainwindow.resizable(False, False)
mainwindow.mainloop()
