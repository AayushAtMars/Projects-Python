from tkinter import *
from tkinter import ttk               #in this there is entery field like google

import cv2
from PIL import Image,ImageTk         #pip install pillow
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x810+0+0")
        self.root.title("FACE RECOGNISTION SYSTEM")

        # TITLE LABEL
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 23, "bold"),
                          fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)



        img1 = Image.open("Images/face_detection.png")
        img1 = img1.resize((650, 700))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        img_lbl = Label(self.root, image=self.photoimg1)
        img_lbl.place(x=0, y=45, width=650, height=700)



        img2 = Image.open("Images/face_detection2.png")
        img2 = img2.resize((950, 700))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img_lbl = Label(self.root, image=self.photoimg2)
        img_lbl.place(x=650, y=45, width=950, height=700)



        b_text = Button(self.root, text="Recognize Face",command=self.face_recog,cursor="hand2",font=("times new roman", 25, "bold"), bg="skyblue", fg="white")
        b_text.place(x=1000, y=650, width=250, height=45)




    #********************ATTENDANCE**************************

    def mark_attendance(self,i,r,n,d):
        with open("aayush.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split(",")
                name_list.append(entry[0])


            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")



    #**********FACE RECOGNITION***************************

    def face_recog(self):
            def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

                coord=[]

                for(x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))



                    con = mysql.connector.connect(host="localhost", username="root", password="aayu14",
                                                  database="face_recogniser")
                    my_cursor = con.cursor()

                    my_cursor.execute("select Name from student where Student_id="+str(id))
                    n=my_cursor.fetchone()
                    n="+".join(n)

                    my_cursor.execute("select Roll from student where Student_id=" + str(id))
                    r = my_cursor.fetchone()
                    r = "+".join(r)

                    my_cursor.execute("select Dep from student where Student_id=" + str(id))
                    d = my_cursor.fetchone()
                    d = "+".join(d)

                    my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                    i = my_cursor.fetchone()
                    i = "+".join(i)



                    if confidence>77:
                        cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
                        cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),1)
                        cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
                        cv2.putText(img, f"department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
                        self.mark_attendance(i,r,n,d)


                    else:
                        cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown face",(x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)

                    coord=[x,y,w,h]


                return coord

            def recognize(img,clf,faceCascade):
                coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
                return img

            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap=cv2.VideoCapture(0)

            while True:
                ret,img=video_cap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Welcome To Face Recognition",img)

                if cv2.waitKey(1)==13:
                    break

            video_cap.release()
            cv2.destroyAllWindows()




if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()