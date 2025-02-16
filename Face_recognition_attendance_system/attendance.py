from tkinter import *
from tkinter import ttk               #in this there is entery field like google

import cv2
from PIL import Image,ImageTk         #pip install pillow
from tkinter import messagebox
import mysql.connector
import os
import csv
from tkinter import filedialog


#TODO update button


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x810+0+0")
        self.root.title("FACE RECOGNISTION SYSTEM")

        # BG IMAGE
        img3 = Image.open("Images/bg_img.jpg")
        img3 = img3.resize((1530, 810))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=810)

        img1 = Image.open("Images/attendance1.png")
        img1 = img1.resize((800, 200))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        img_lbl = Label(self.root, image=self.photoimg1)
        img_lbl.place(x=0, y=0, width=800, height=200)


        img2 = Image.open("Images/attendance2.jpg")
        img2 = img2.resize((800,200))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img_lbl = Label(self.root, image=self.photoimg2)
        img_lbl.place(x=800, y=0, width=800, height=200)

        # TITLE LABEL
        title_lbl = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 23, "bold"), bg="white",
                          fg="green")
        title_lbl.place(x=0, y=150, width=1530, height=35)

        # MAIN FRAME
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=200, width=1490, height=575)

        # LEFT LABEL FRAME
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", fg="red",
                                font=("times new roman", 15, "bold"))
        left_frame.place(x=10, y=5, width=740, height=550)

        img4 = Image.open("Images/student_managment.jpg")
        img4 = img4.resize((710, 130))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        img_lbl = Label(left_frame, image=self.photoimg4)
        img_lbl.place(x=5, y=0, width=710, height=130)

        insideLeft_frame = Frame(left_frame, bd=2,relief=RIDGE, bg="white")
        insideLeft_frame.place(x=0, y=135, width=730, height=385)

        #LABELS AND ENTRIES

        # Student ID No
        self.var_attendanceid = StringVar()
        attendance_id = Label(insideLeft_frame, text="StudentID: ", font=("times new roman", 14, "bold"), bg="white")
        attendance_id.grid(row=0, column=0)

        # Student ID entry
        attendance_id_entry = ttk.Entry(insideLeft_frame, textvariable=self.var_attendanceid, width=20, font=("times new roman", 14, "bold"))
        attendance_id_entry.grid(row=0, column=1, sticky=W)

        # Roll No
        self.var_roll_no = StringVar()
        roll = Label(insideLeft_frame, text="Roll: ", font=("times new roman", 14, "bold"), bg="white")
        roll.grid(row=0, column=2, padx=1)

        # Student ROLL entry
        roll_entry = ttk.Entry(insideLeft_frame, textvariable=self.var_roll_no, width=17, font=("times new roman", 14, "bold"))
        roll_entry.grid(row=0, column=3, padx=0, pady=10, sticky=W)

        # NAME
        self.var_name = StringVar()
        name = Label(insideLeft_frame, text="Name: ", font=("times new roman", 14, "bold"), bg="white")
        name.grid(row=1, column=0, padx=10)

        # Student NAME entry
        name_entry = ttk.Entry(insideLeft_frame, textvariable=self.var_name, width=20,
                               font=("times new roman", 14, "bold"))
        name_entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # DEPARTMENT
        self.var_dep = StringVar()
        dep = Label(insideLeft_frame, text="Department: ", font=("times new roman", 14, "bold"), bg="white")
        dep.grid(row=1, column=2, padx=10)

        # Student DEPARTMENT entry
        dep_entry = ttk.Entry(insideLeft_frame, textvariable=self.var_dep, width=17,
                               font=("times new roman", 14, "bold"))
        dep_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # TIME
        self.var_time = StringVar()
        time = Label(insideLeft_frame, text="Time: ", font=("times new roman", 14, "bold"), bg="white")
        time.grid(row=2, column=0, padx=10)

        # Student TIME entry
        time_entry = ttk.Entry(insideLeft_frame, textvariable=self.var_time, width=20,
                              font=("times new roman", 14, "bold"))
        time_entry.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        # Date
        self.var_date = StringVar()
        date = Label(insideLeft_frame, text="Date: ", font=("times new roman", 14, "bold"), bg="white")
        date.grid(row=2, column=2, padx=10)

        # Student date entry
        date_entry = ttk.Entry(insideLeft_frame, textvariable=self.var_date, width=17,
                               font=("times new roman", 14, "bold"))
        date_entry.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        # ATTENDANCE
        self.var_atten = StringVar()
        atten = Label(insideLeft_frame, text="Attendance Status: ", font=("times new roman", 14, "bold"), bg="white")
        atten.grid(row=3, column=0, padx=10)

        # GENDER COMBOBOX
        self.atten_combo = ttk.Combobox(insideLeft_frame, textvariable=self.var_atten, font=("times new roman", 12), width=23,
                                    state="readonly")
        self.atten_combo["values"] = ["Status", "Present", "Absent"]
        self.atten_combo.current(0)
        self.atten_combo.grid(row=3, column=1, padx=2, pady=10, sticky=W)



        # BUTTON FRAME
        but_frame1 = Frame(insideLeft_frame, bd=2, relief=RIDGE, bg="white")
        but_frame1.place(x=0, y=250, width=725, height=40)

        # SAVE BUTTON
        save_btn = Button(but_frame1, text="Import csv",command=self.importCsv,  font=("times new roman", 13, "bold"),
                          bg="blue", fg="white", width=17)
        save_btn.grid(row=0, column=0)

        # UPDATE BUTTON
        update_btn = Button(but_frame1, text="Export csv",command=self.exportCsv,  font=("times new roman", 13, "bold"),
                            bg="blue", fg="white", width=17)
        update_btn.grid(row=0, column=1)

        # DELETE BUTTON
        delete_btn = Button(but_frame1, text="Update",  font=("times new roman", 13, "bold"),
                            bg="blue", fg="white", width=17)
        delete_btn.grid(row=0, column=2)

        # RESET BUTTON
        reset_btn = Button(but_frame1, text="Reset",command=self.reset_data,  font=("times new roman", 13, "bold"),
                           bg="blue", fg="white", width=17)
        reset_btn.grid(row=0, column=3)

        # RIGHT LABEL FRAME
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", fg="red",
                                 font=("times new roman", 15, "bold"))
        right_frame.place(x=755, y=5, width=708, height=550)


        insideRight_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        insideRight_frame.place(x=3, y=5, width=700, height=515)

        # SCROLLBAR

        scroll_x = ttk.Scrollbar(insideRight_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(insideRight_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(insideRight_frame,column=("id","roll","name","dep","time","date","attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("time", text="Time")
        self.student_table.heading("date", text="Date")
        self.student_table.heading("attendance", text="Attendance")

        self.student_table["show"] = "headings"

        self.student_table.column("id", width=80)
        self.student_table.column("roll", width=120)
        self.student_table.column("name", width=120)
        self.student_table.column("dep", width=120)
        self.student_table.column("time", width=100)
        self.student_table.column("date", width=100)
        self.student_table.column("attendance", width=80)

        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)




    #FETCH DATA

    def fetchData(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)

    #IMPORT CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    #EXPORT CSV

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*csv"), ("All File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data Exported to"+os.path.basename(fln)+" Successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)


    # GET CURSOR

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        list=[self.var_attendanceid,self.var_roll_no,self.var_name,self.var_dep,self.var_time,self.var_date,self.var_atten]
        j=0
        for i in list:
            i.set(data[j])
            j=j+1


    def reset_data(self):
        list = [self.var_attendanceid, self.var_roll_no, self.var_name, self.var_dep, self.var_time, self.var_date,self.var_atten]
        for i in list:
            i.set("")









if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()