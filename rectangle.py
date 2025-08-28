from tkinter import *
from tkinter.ttk import *

class Shape:
    def __init__(self, master=None):
        self.master = master

    def create(self):
        self.canvas = Canvas(self.master)
        self.canvas.create_rectangle(230, 10, 290, 30, outline="purple", width=3)
        self.canvas.pack(fill=BOTH, expand=1)

if __name__ == "__main__":
    master = Tk()
    shape = Shape(master)
    shape.create()  
    master.title("Shapes")
    master.geometry("330*220+300+300")
    mainloop()
