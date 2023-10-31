from tkinter import *
from tkinter import ttk

gui = Tk()
gui.title("Poço infinito")
gui.geometry('280x150')
gui.configure(bg='blue')

gui.configure(background = "gray92")
L_label = Label(gui ,text = "Largura [m]:").grid(row = 0,column = 0)
n_i_label = Label(gui ,text = "n inicial").grid(row = 1,column = 0)
n_f_label = Label(gui ,text = "n final").grid(row = 2,column = 0)
a_label = Label(gui ,text = "Posição inicial de procura").grid(row = 3,column = 0)
b_label = Label(gui ,text = "Posição final de procura").grid(row = 4,column = 0)
L = Entry(gui).grid(row = 0,column = 1)
n_i = Entry(gui).grid(row = 1,column = 1)
n_f = Entry(gui).grid(row = 2,column = 1)
a = Entry(gui).grid(row = 3,column = 1)
a = Entry(gui).grid(row = 4,column = 1)

def simulacao():
   print("funcionando")

btn = ttk.Button(gui, text = "Simular", command = simulacao).grid(row = 5, column = 1)
gui.mainloop()