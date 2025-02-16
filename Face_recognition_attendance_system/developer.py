from tkinter import *
from tkinter import ttk               #in this there is entery field like google

import cv2
from PIL import Image,ImageTk         #pip install pillow
from tkinter import messagebox
import mysql.connector


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x810+0+0")
        self.root.title("FACE RECOGNISTION SYSTEM")


        img1 = Image.open("Images/developer1.png")
        img1 = img1.resize((1530, 810))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        img_lbl = Label(self.root, image=self.photoimg1)
        img_lbl.place(x=0, y=0, width=1530, height=810)

        # TITLE LABEL
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 30, "bold"), fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img2 = Image.open("Images/developer_info.jpg")
        img2 = img2.resize((1080, 810))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img_lbl = Label(self.root, image=self.photoimg2)
        img_lbl.place(x=225, y=50, width=1080, height=740)

        # # MAIN FRAME
        # main_frame = Frame(img_lbl, bd=2, bg="white")
        # main_frame.place(x=1000, y=100, width=500, height=600)

        # img2 = Image.open("photo1.jpg")
        # img2 = img2.resize((200,200))
        # self.photoimg2 = ImageTk.PhotoImage(img2)
        #
        # img_lbl = Label(main_frame, image=self.photoimg2)
        # img_lbl.place(x=300, y=0, width=200, height=200)







if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()