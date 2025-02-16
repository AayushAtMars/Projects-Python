from tkinter import *
from tkinter import ttk               #in this there is entery field like google

import cv2
from PIL import Image,ImageTk         #pip install pillow
from tkinter import messagebox
import mysql.connector


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x810+0+0")
        self.root.title("FACE RECOGNISTION SYSTEM")


        img1 = Image.open("Images/helpdesk1.png")
        img1 = img1.resize((1530, 810))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        img_lbl = Label(self.root, image=self.photoimg1)
        img_lbl.place(x=0, y=0, width=1530, height=810)

        # TITLE LABEL
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 30, "bold"), fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # EMAIL
        email_lbl = Label(self.root, text="aayushrajput3105@gmail.com", font=("times new roman", 30, "bold"), fg="purple")
        email_lbl.place(x=550, y=350)



if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()