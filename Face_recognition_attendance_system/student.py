from tkinter import *
from tkinter import ttk               #in this there is entery field like google

import cv2
from PIL import Image,ImageTk         #pip install pillow
from tkinter import messagebox
import mysql.connector


class Student:
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



        img = Image.open("Images/student1.jpg")
        img = img.resize((500, 100))
        self.photoimg = ImageTk.PhotoImage(img)

        img_lbl = Label(bg_img, image=self.photoimg)
        img_lbl.place(x=0, y=0, width=500, height=100)



        img1 = Image.open("Images/student2.jpg")
        img1 = img1.resize((500, 100))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        img_lbl = Label(bg_img, image=self.photoimg1)
        img_lbl.place(x=500, y=0, width=500, height=100)



        img2 = Image.open("Images/student3.jpg")
        img2 = img2.resize((500, 100))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img_lbl = Label(bg_img, image=self.photoimg2)
        img_lbl.place(x=1000, y=0, width=500, height=100)



        #TITLE LABEL
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",23,"bold"), bg="white", fg="blue")
        title_lbl.place(x=0,y=100,width=1530,height=35)


        #MAIN FRAME
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=140,width=1490,height=700)






###################################################################################################################################################
        #LEFT LABEL FRAME
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",fg="red", font=("times new roman",15,"bold"))
        left_frame.place(x=10,y=10,width=790,height=630)


        img4 = Image.open("Images/student_managment.jpg")
        img4 = img4.resize((720, 130))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        img_lbl = Label(left_frame, image=self.photoimg4)
        img_lbl.place(x=15, y=0, width=720, height=130)



        #INSIDE LEFT FRAME-1
        current_course = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",fg="green",
                                    font=("times new roman", 15, "bold"))
        current_course.place(x=15, y=135, width=780, height=120)


        #DEPARTMENT
        self.var_dep=StringVar()
        dept=Label(current_course,text="Department: ",font=("times new roman", 14, "bold"),bg="white")
        dept.grid(row=0,column=0,padx=10)

        # DEPARTMENT COMBOBOX
        dept_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman", 12),width=20,state="readonly")
        dept_combo["values"]=["Select Department","Computing","Engineering","Hotel Management","Management","Pharma Sciences"]
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)




        # COURSE
        self.var_course = StringVar()
        course = Label(current_course, text="Courses: ", font=("times new roman", 14, "bold"), bg="white")
        course.grid(row=0, column=2, padx=10)


        #FUNCTION TO UPDATE COURSES ACCORDING TO THE DEPARTMENT
        def update_values(event):
            course_combo["values"]=[]

            selected_value=dept_combo.get()

            if (selected_value=="Computing"):
                course_combo["values"]= ["B.Sc","M.Sc","BCA","MCA"]

            elif(selected_value == "Engineering"):
                course_combo["values"]=["Computer Science","Computer Science & Design","Civil Engineering","Mechanical Engineering",
                                        "Electrical Engineering","Electronics and Communication Engineering"]

            elif (selected_value == "Hotel Management"):
                course_combo["values"] = ["B.Sc"]

            elif (selected_value == "Management"):
                course_combo["values"] = ["BBA","MBA"]

            elif (selected_value == "Pharma Sciences"):
                course_combo["values"] = ["Bachelor of Pharmacy","Pharma.D"]


            else:
                course_combo["values"]=[]


        #  COURSE COMBOBOX
        course_combo = ttk.Combobox(current_course,textvariable=self.var_course, font=("times new roman", 12), width=20,
                                    state="readonly")
        course_combo["values"] = ("Select Course",)
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        dept_combo.bind('<<ComboboxSelected>>',update_values)





        # YEAR
        self.var_year = StringVar()
        year = Label(current_course, text="Year: ", font=("times new roman", 14, "bold"), bg="white")
        year.grid(row=1, column=0, padx=10)

        # YEAR COMBOBOX
        year_combo = ttk.Combobox(current_course,textvariable=self.var_year, font=("times new roman", 12), width=20, state="readonly")
        year_combo["values"] = ["Select Year","2020-21","2021-22","2022-23","2023-24","2024-25"]
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)



        # SEMESTER
        self.var_semester = StringVar()
        semester = Label(current_course, text="Semester: ", font=("times new roman", 14, "bold"), bg="white")
        semester.grid(row=1, column=2, padx=10)

        # SEMESTER COMBOBOX
        semester_combo = ttk.Combobox(current_course,textvariable=self.var_semester, font=("times new roman", 12), width=20, state="readonly")
        semester_combo["values"] = ["Select Semester", "1st","2nd","3rd","4th","5th","6th","7th","8th"]
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)





        # INSIDE LEFT FRAME-2
        student_info = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Class Information",
                                    fg="green",font=("times new roman", 15, "bold"))
        student_info.place(x=15, y=255, width=780, height=380)




        #Student ID No
        self.var_id = StringVar()
        id = Label(student_info, text="StudentID: ", font=("times new roman", 14, "bold"), bg="white")
        id.grid(row=0, column=0, padx=10)


        #Student ID entry
        id_entry=ttk.Entry(student_info,textvariable=self.var_id,width=20,font=("times new roman", 14, "bold"))
        id_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)



        # Student Name
        self.var_name = StringVar()
        name = Label(student_info, text="Student Name: ", font=("times new roman", 14, "bold"), bg="white")
        name.grid(row=0, column=2, padx=10)

        # Student NAME entry
        name_entry = ttk.Entry(student_info,textvariable=self.var_name, width=20, font=("times new roman", 14, "bold"))
        name_entry.grid(row=0, column=3, padx=2, pady=10, sticky=W)



        # SECTION
        self.var_sec = StringVar()
        section = Label(student_info, text="Section: ", font=("times new roman", 14, "bold"), bg="white")
        section.grid(row=1, column=0, padx=10)

        # SECTION COMBOBOX
        section_combo = ttk.Combobox(student_info,textvariable=self.var_sec, font=("times new roman", 12), width=23, state="readonly")
        section_combo["values"] = ["Select Section", "A","B","C","D","E"]
        section_combo.current(0)
        section_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)



        # ROLL NO.
        self.var_roll = StringVar()
        roll = Label(student_info, text="Roll No.: ", font=("times new roman", 14, "bold"), bg="white")
        roll.grid(row=1, column=2, padx=10)

        # ROLL NO. entry
        roll_value = StringVar()
        roll_entry = ttk.Entry(student_info,textvariable=self.var_roll, width=20, font=("times new roman", 14, "bold"))
        roll_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)



        # GENDER
        self.var_gender = StringVar()
        gender = Label(student_info, text="Gender: ", font=("times new roman", 14, "bold"), bg="white")
        gender.grid(row=2, column=0, padx=10)

        # GENDER COMBOBOX
        gender_combo = ttk.Combobox(student_info,textvariable=self.var_gender, font=("times new roman", 12), width=23, state="readonly")
        gender_combo["values"] = ["Select Gender", "Male","Female","Others"]
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)


        # DOB
        self.var_dob = StringVar()
        dob = Label(student_info, text="DOB: ", font=("times new roman", 14, "bold"), bg="white")
        dob.grid(row=2, column=2, padx=10)

        # DOB entry
        dob_value = StringVar()
        dob_entry = ttk.Entry(student_info,textvariable=self.var_dob, width=20, font=("times new roman", 14, "bold"))
        dob_entry.grid(row=2, column=3, padx=2, pady=10, sticky=W)



        # EMAIL
        self.var_email = StringVar()
        email = Label(student_info, text="Email: ", font=("times new roman", 14, "bold"), bg="white")
        email.grid(row=3, column=0, padx=10)

        # EMAIL entry
        email_entry = ttk.Entry(student_info,textvariable=self.var_email, width=20, font=("times new roman", 14, "bold"))
        email_entry.grid(row=3, column=1, padx=2, pady=10, sticky=W)



        # PHONE NO.
        self.var_phone = StringVar()
        phone = Label(student_info, text="Phone No.: ", font=("times new roman", 14, "bold"), bg="white")
        phone.grid(row=3, column=2, padx=10)

        # PHONE entry
        phone_entry = ttk.Entry(student_info,textvariable=self.var_phone, width=20, font=("times new roman", 14, "bold"))
        phone_entry.grid(row=3, column=3, padx=2, pady=10, sticky=W)



        # ADDRESS
        self.var_address = StringVar()
        address = Label(student_info, text="Address: ", font=("times new roman", 14, "bold"), bg="white")
        address.grid(row=4, column=0, padx=10)

        # ADDRESS ENTRY
        address_entry = ttk.Entry(student_info,textvariable=self.var_address, width=20, font=("times new roman", 14, "bold"))
        address_entry.grid(row=4, column=1, padx=2, pady=10, sticky=W)



        # TEACHER
        self.var_teacher = StringVar()
        teacher = Label(student_info, text="Teacher Name: ", font=("times new roman", 14, "bold"), bg="white")
        teacher.grid(row=4, column=2, padx=10)

        # TEACHER ENTRY
        teacher_entry = ttk.Entry(student_info,textvariable=self.var_teacher, width=20, font=("times new roman", 14, "bold"))
        teacher_entry.grid(row=4, column=3, padx=2, pady=10, sticky=W)



        #RADIO BUTTONS
        self.var_radio1=StringVar()
        rd_button1=ttk.Radiobutton(student_info,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        rd_button1.grid(row=5,column=0)

        #self.var_radio2 = StringVar()
        rd_button2=ttk.Radiobutton(student_info,variable=self.var_radio1,text="No Photo Sample",value="No")
        rd_button2.grid(row=5,column=1)



        #BUTTON FRAME
        but_frame1=Frame(student_info,bd=2,relief=RIDGE,bg="white")
        but_frame1.place(x=0,y=270,width=780,height=40)

        #SAVE BUTTON
        save_btn=Button(but_frame1,text="SAVE",command=self.add_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=19)
        save_btn.grid(row=0,column=0)

        #UPDATE BUTTON
        update_btn=Button(but_frame1,text="Update",command=self.update_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=19)
        update_btn.grid(row=0,column=1)

        #DELETE BUTTON
        delete_btn=Button(but_frame1,text="Delete",command=self.delete_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=19)
        delete_btn.grid(row=0,column=2)

        #RESET BUTTON
        reset_btn=Button(but_frame1,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=19)
        reset_btn.grid(row=0,column=3)


        #BUTTON FRAME - 2
        but_frame2=Frame(student_info,bd=2,relief=RIDGE,bg="white")
        but_frame2.place(x=0,y=310,width=780,height=40)

        #ADD PHOTO SAMPLE BUTTON
        phSamp_btn=Button(but_frame2,text="ADD PHOTO SAMPLE",command=self.genrate_dataset,font=("times new roman",13,"bold"),bg="blue",fg="white",width=40)
        phSamp_btn.grid(row=1,column=0)

        #UPDATE PHOTO SAMPLE BUTTON
        phUSamp_btn=Button(but_frame2,text="UPDATE PHOTO SAMPLE",font=("times new roman",13,"bold"),bg="blue",fg="white",width=40)
        phUSamp_btn.grid(row=1,column=1)



######################################################################################################################################################################


        # RIGHT LABEL FRAME
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",fg="red",font=("times new roman", 15, "bold"))
        right_frame.place(x=810, y=10, width=660, height=630)



        imgr = Image.open("Images/imgr.jpeg")
        imgr = imgr.resize((720, 130))
        self.photoimgr = ImageTk.PhotoImage(imgr)

        img_lbl = Label(right_frame, image=self.photoimgr)
        img_lbl.place(x=5, y=0, width=720, height=130)



        #SEARCH FRAME
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="View Student Details & Search System",fg="green",
                                    font=("times new roman", 15, "bold"))
        search_frame.place(x=5, y=135, width=645, height=70)

        #SEARCH LABEL
        searchlbl = Label(search_frame,text="Search By",font=("times new roman", 15, "bold"),bg="red",fg="white",
                                    )
        searchlbl.grid(row=0,column=0, padx=10,pady=10,sticky=W)

        # SEARCH COMBOBOX
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12), width=12, state="readonly")
        search_combo["values"] = ["Search By", "Roll No","Admission No"]
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # SEARCH ENTRY
        search_value = StringVar()
        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 14, "bold"), text=search_value)
        search_entry.grid(row=0, column=2, padx=8, pady=10, sticky=W)

        #SEARCH BUTTON
        search_button=Button(search_frame,text="Search",width=12, font=("times new roman", 12, "bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=3,padx=2)

        #SHOW ALL BUTTON
        show_button=Button(search_frame,text="Show all",width=12, font=("times new roman", 12, "bold"),bg="blue",fg="white")
        show_button.grid(row=0,column=4,padx=5)




        #TABLE FRAME
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=645, height=390)

        #SCROLLBAR

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","sec","rno","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("rno", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("dep",width=110)
        self.student_table.column("course",width=130)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=80)
        self.student_table.column("id",width=80)
        self.student_table.column("name",width=120)
        self.student_table.column("sec",width=60)
        self.student_table.column("rno", width=120)
        self.student_table.column("gender", width=80)
        self.student_table.column("dob",width=80)
        self.student_table.column("email",width=180)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=130)
        


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    #******************Function Declaration********************************************

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get=="" or self.var_id.get=="" :
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
            try:
                con=mysql.connector.connect(host="localhost",username="root",password="aayu14",database="face_recogniser")
                my_cursor=con.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_id.get(),self.var_name.get(),self.var_sec.get(),self.var_roll.get(),self.var_gender.get()
                    ,self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get()
                ))


                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)






    #**********FETCH DATA**************************

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", username="root", password="aayu14", database="face_recogniser")
        my_cursor = con.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())

            for i in data:
                self.student_table.insert("",END,values=i)

            con.commit()

        con.close()




    #*************GET CURSOR************************

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        list=[self.var_dep,self.var_course,self.var_year,self.var_semester,self.var_id,self.var_name,self.var_sec,self.var_roll,self.var_gender
                    ,self.var_dob,self.var_email,self.var_phone,self.var_address,self.var_teacher,self.var_radio1]
        j=0
        for i in list:
            i.set(data[j])
            j=j+1



    #UPDATE FUNCTION

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get=="" or self.var_id.get=="" :
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    con = mysql.connector.connect(host="localhost", username="root", password="aayu14",
                                                  database="face_recogniser")
                    my_cursor = con.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_name.get(),self.var_sec.get(),self.var_roll.get(),self.var_gender.get()
                                        ,self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_id.get()))


                else:
                    if not Update:
                        return   
                messagebox.showinfo("Success","Student Details Updated Successfully")
                con.commit()
                self.fetch_data()
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



    #DELETE FUNCTION

    def delete_data(self):
        if self.var_id.get=="":
            messagebox.showerror("Error","Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)

                if delete>0:
                        con = mysql.connector.connect(host="localhost", username="root", password="aayu14",
                                                      database="face_recogniser")
                        my_cursor = con.cursor()
                        sql="delete from student where Student_id=%s"
                        val=(self.var_id.get(),)
                        my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return

                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)


            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)





    #RESET DATA

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_sec.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")




    #**************GENRATING DATA SET OT TAKING PHOTO SAMPLE******************************

    def genrate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get=="" or self.var_id.get=="" :
            messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
            try:
                    con = mysql.connector.connect(host="localhost", username="root", password="aayu14",
                                                  database="face_recogniser")
                    my_cursor = con.cursor()
                    my_cursor.execute("select * from student")
                    myresult=my_cursor.fetchall()

                    id1=self.var_id.get()
                    # id=0
                    # for x in myresult:
                    #     id+=1
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),self.var_name.get(), self.var_sec.get(), self.var_roll.get(), self.var_gender.get(),self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),self.var_teacher.get(), self.var_radio1.get(), self.var_id.get()==len(myresult)+1))

                    con.commit()
                    self.fetch_data()
                    self.reset_data()
                    con.close()



                    #******Load predefined data on face frontal from opencv

                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_crop(img):
                        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(grey,1.3,5)
                        #scalling factor=1.3
                        #minimum neighbour=5

                        for(x,y,w,h) in faces:
                            face_crop=img[y:y+h,x:x+w]
                            return face_crop

                    cam=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cam.read()
                        if face_crop(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_crop(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name="data/user."+str(id1)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:        #13 se jo window open hui hai wo close ho jaygei Enter press krne pe
                            break

                    cam.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Data Set Genrated !")




            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()