from doctest import Example
from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH
from tkinter.ttk import Frame, Style

class Example(Frame) :
    def __init__(self, parent):
        Frame.__init__(self, parent)
        
        self.parent = parent
        self.initUI()
        
    def initUI(self) :
            self.parent.title("Absolute positioning")
            self.pack(fill=BOTH, expand=1)
            
            Style() . configure("TFrame", background="#333")
        
            bard = Image.open("C:\\Users\\CICT\\Downloads\\download.jpg")
            bard=bard.resize((100,100), Image.LANCZOS)
            bardejove = ImageTk.PhotoImage (bard)
            labell1 = Label (self, image=bardejove)
            labell1.image = bardejove
            labell1.place(x=20, y=20)
            
            rot = Image.open("C:\\Users\\CICT\\Downloads\\1.jpeg")
            rot=rot.resize((100,100), Image.LANCZOS)
            rotunda = ImageTk.PhotoImage(rot)
            label12 = Label(self, image=rotunda)
            label12.image =rotunda
            label12.place(x=40, y=160)

            minc = Image.open("C:\\Users\\CICT\\Downloads\\h1.jpg")
            minc=minc.resize((100,100), Image.LANCZOS)
            mincol = ImageTk.PhotoImage(minc)
            label13 = Label(self, image=mincol)
            label13.image = mincol
            label13.place (x=170, y=50)

root = Tk()
root.geometry("300x280+300+300")
app = Example(root)
root.mainloop()
