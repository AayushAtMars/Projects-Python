from tkinter import *
from tkinter import ttk               #in this there is entery field like google

import cv2
from PIL import Image,ImageTk         #pip install pillow
from tkinter import messagebox
import mysql.connector
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x810+0+0")
        self.root.title("FACE RECOGNISTION SYSTEM")

        # TITLE LABEL
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 23, "bold"),
                          fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)




        img1 = Image.open("Images/train_data_f.jpg")
        img1 = img1.resize((1530, 325))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        img_lbl = Label(self.root, image=self.photoimg1)
        img_lbl.place(x=0, y=45, width=1530, height=325)


        b_text = Button(self.root, text="TRAIN DATA",command=self.train_classifier, font=("times new roman", 25, "bold"), bg="red", fg="yellow",
                         cursor="hand2")
        b_text.place(x=0, y=375, width=1530, height=60)



        img2 = Image.open("Images/train_data_f1.jpg")
        img2 = img2.resize((1530, 325))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img_lbl = Label(self.root, image=self.photoimg2)
        img_lbl.place(x=0, y=440, width=1530, height=325)






    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #Gray scale image
            imageNp = np.array(img,'uint8')     #convert image to grid scale
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #TRAINING THE CLASSIFIER AND SAVE
        clf=cv2.face.LBPHFaceRecognizer_create()  #LOCAL BINARY HISTOGRAM

        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Data Set Training Completed")






if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()