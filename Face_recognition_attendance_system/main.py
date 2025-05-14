import tkinter.messagebox
from tkinter import *
import tkinter
from tkinter import ttk               #in this there is entery field like google
from PIL import Image,ImageTk         #pip install pillow
from student import Student
import cv2
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
#TODO exit function messagebox

class Face_recognistion_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x810+0+0")
        self.root.title("FACE RECOGNISTION SYSTEM")

        #TODO ICON OF GUI


        # BG IMAGE
        img3 = Image.open("Images/bg_img.jpg")
        img3 = img3.resize((1530, 810))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=810)

        #SVIET Logo
        img=Image.open("Images/sviet_logo.png")
        #TODO change image with white background
        img=img.resize((500,130))
        self.photoimg=ImageTk.PhotoImage(img)

        img_lbl=Label(bg_img,image=self.photoimg)
        img_lbl.place(x=0, y=0, width=500, height=130)



        img1=Image.open("Images/phomtu3.jpeg")
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        img_lbl=Label(bg_img,image=self.photoimg1)
        img_lbl.place(x=550, y=0, width=500,height=130)



        img2=Image.open("Images/face_2.png")
        #TODO change image with white background
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        img_lbl=Label(bg_img,image=self.photoimg2)
        img_lbl.place(x=1050, y=0, width=500, height=130)


        #TITLE LABEL
        title_lbl=Label(bg_img,text="FACE RECOGNISTION ATTENDANCE SYSTEM", font=("comicsansms",23,"bold"), bg="white", fg="red")
        title_lbl.place(x=0,y=130,width=1530,height=45)


        #TIME
        def time():
            string=strftime("%H:%M:%S:%p")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",14,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()



        #STUDENT DETAIL
        img4 = Image.open("Images/student_detailss.jpg")
        img4 = img4.resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=180,width=220,height=220)

        b1_text = Button(bg_img, text="Student Details",command=self.student_details  ,font=("times new roman",15,"bold"),bg="blue",fg="white" ,cursor="hand2")
        b1_text.place(x=200, y=400, width=220, height=40)




        # FACE RECOGNISTION
        img5 = Image.open("Images/face_recognistion.png")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5,command=self.face_data, cursor="hand2")
        b2.place(x=500, y=180, width=220, height=220)

        b2_text = Button(bg_img, text="FACE RECOGNISTION",command=self.face_data, font=("times new roman", 15, "bold"), bg="blue", fg="white",
                         cursor="hand2")
        b2_text.place(x=500, y=400, width=220, height=40)



        # ATTENDANCE
        img6 = Image.open("Images/attendance.jpg")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Button(bg_img, image=self.photoimg6,command=self.attendace, cursor="hand2")
        b2.place(x=780, y=180, width=220, height=220)

        b2_text = Button(bg_img, text="ATTENDANCE",command=self.attendace, font=("times new roman", 15, "bold"), bg="blue", fg="white",
                         cursor="hand2")
        b2_text.place(x=780, y=400, width=220, height=40)



        # HELPDESK
        img7 = Image.open("Images/helpdesk.png")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b2 = Button(bg_img, image=self.photoimg7,command=self.help, cursor="hand2")
        b2.place(x=1060, y=180, width=220, height=220)

        b2_text = Button(bg_img, text="HELPDESK",command=self.help, font=("times new roman", 15, "bold"), bg="blue", fg="white",
                         cursor="hand2")
        b2_text.place(x=1060, y=400, width=220, height=40)



        # TRAIN DATA
        img8 = Image.open("Images/train_data.png")
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b2 = Button(bg_img, image=self.photoimg8,command=self.train_data, cursor="hand2")
        b2.place(x=200, y=500, width=220, height=220)

        b2_text = Button(bg_img, text="TRAIN DATA",command=self.train_data, font=("times new roman", 15, "bold"), bg="blue", fg="white",
                         cursor="hand2")
        b2_text.place(x=200, y=720, width=220, height=40)



        # PHOTOS
        img9 = Image.open("Images/photos.png")
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b2 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b2.place(x=500, y=500, width=220, height=220)

        b2_text = Button(bg_img, text="PHOTOS",command=self.open_img, font=("times new roman", 15, "bold"), bg="blue", fg="white",
                         cursor="hand2")
        b2_text.place(x=500, y=720, width=220, height=40)



        # DEVELOPER
        img10 = Image.open("Images/developer.png")
        img10 = img10.resize((220, 220))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b2 = Button(bg_img, image=self.photoimg10,command=self.developer, cursor="hand2")
        b2.place(x=780, y=500, width=220, height=220)

        b2_text = Button(bg_img, text="DEVELOPER",command=self.developer, font=("times new roman", 15, "bold"), bg="blue", fg="white",
                         cursor="hand2")
        b2_text.place(x=780, y=720, width=220, height=40)


        # EXIT
        img11 = Image.open("Images/exit.jpg")
        img11 = img11.resize((220, 220))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b2 = Button(bg_img, image=self.photoimg11,command=exit, cursor="hand2")
        b2.place(x=1080, y=500, width=220, height=220)

        b2_text = Button(bg_img, text="EXIT",command=exit, font=("times new roman", 15, "bold"), bg="blue", fg="white",
                         cursor="hand2")
        b2_text.place(x=1080, y=720, width=220, height=40)




    def open_img(self):
        os.startfile("data")


    # ***************************Functions Buttons*******************************
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)




    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)




    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)


    def attendace(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)


    def help(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Exit?",parent=self.root)
        if self.exit>0:
            self.root.destroy()

        else:
            return










if __name__=="__main__":
    root=Tk()
    obj=Face_recognistion_system(root)
    root.mainloop()