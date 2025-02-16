from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import security_login


class register:

    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # BG IMAGE
        img1 = Image.open("Images/bg_img.jpg")
        img1 = img1.resize((1530, 800))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1530, height=800)

        # MAIN FRAME
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=365, y=100, width=800, height=550)

        # TITLE LABEL
        title_lbl = Label(main_frame, text="REGISTER HERE", font=("times new roman", 25, "bold"),
                          bg="white", fg="green")
        title_lbl.place(x=20, y=20)

        #LABELS AND ENTERIES

        #FIRST NAME
        self.f_name = StringVar()
        fname = Label(main_frame, text="First Name", font=("times new roman", 15, "bold"),
                          bg="white", fg="black")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(main_frame, textvariable=self.f_name, font=("times new roman", 15))
        fname_entry.place(x=50, y=130, width=250)

        #LAST NAME
        self.l_name = StringVar()
        lname = Label(main_frame, text="last Name", font=("times new roman", 15, "bold"),
                      bg="white", fg="black")
        lname.place(x=370, y=100)

        lname_entry = ttk.Entry(main_frame, textvariable=self.l_name, font=("times new roman", 15))
        lname_entry.place(x=370, y=130, width=250)


        # Contact No.
        self.contact = StringVar()
        cont = Label(main_frame, text="Contact No.", font=("times new roman", 15, "bold"),
                      bg="white", fg="black")
        cont.place(x=50, y=170)

        cont_entry = ttk.Entry(main_frame, textvariable=self.contact, font=("times new roman", 15))
        cont_entry.place(x=50, y=200, width=250)

        # Email
        self.var_email = StringVar()
        email = Label(main_frame, text="Email", font=("times new roman", 15, "bold"),
                     bg="white", fg="black")
        email.place(x=370, y=170)

        email_entry = ttk.Entry(main_frame, textvariable=self.var_email, font=("times new roman", 15))
        email_entry.place(x=370, y=200, width=250)

        # Security Question
        self.var_ques = StringVar()
        ques = Label(main_frame, text="Select Security Question", font=("times new roman", 15, "bold"),
                      bg="white", fg="black")
        ques.place(x=50, y=240)

        # SECURITY COMBOBOX
        section_combo = ttk.Combobox(main_frame, textvariable=self.var_ques, font=("times new roman", 12), width=23,
                                     state="readonly")
        section_combo["values"] = ["Select Security Question", "In what city were you born?", "What is the name of your favourite pet?", "Which high school did you attend?"]
        section_combo.current(0)
        section_combo.place(x=50,y=270,width=250)

        # SECURITY ANSWER
        self.var_answer = StringVar()
        answer = Label(main_frame, text="Security Answer", font=("times new roman", 15, "bold"),
                      bg="white", fg="black")
        answer.place(x=370, y=240)

        answer_entry = ttk.Entry(main_frame, textvariable=self.var_answer, font=("times new roman", 15))
        answer_entry.place(x=370, y=270, width=250)

        # PASSWORD
        self.var_password = StringVar()
        password = Label(main_frame, text="Password", font=("times new roman", 15, "bold"),
                       bg="white", fg="black")
        password.place(x=50, y=310)

        password_entry = ttk.Entry(main_frame, textvariable=self.var_password, font=("times new roman", 15))
        password_entry.place(x=50, y=340, width=250)

        # CONFIRM PASSWORD
        self.var_cpassword = StringVar()
        cpassword = Label(main_frame, text="Confirm Password", font=("times new roman", 15, "bold"),
                         bg="white", fg="black")
        cpassword.place(x=370, y=310)

        cpassword_entry = ttk.Entry(main_frame, textvariable=self.var_cpassword, font=("times new roman", 15))
        cpassword_entry.place(x=370, y=340, width=250)


        #BUTTON
        # CHECK BUTTON
        # self.var_check=StringVar()
        # check_btn = Checkbutton(main_frame, variable=self.var_check, text="I Agree The Terms & Conditions",  font=("times new roman", 12, "bold"),onvalue=1,offvalue=0)
        # check_btn.place(x=50,y=380)

        # REGISTER BUTTON
        register_btn = Button(main_frame, text="Register Now",command=self.register_data, font=("times new roman", 13, "bold"),
                            bg="red", fg="white", width=20)
        register_btn.place(x=60,y=440)

        # LOGIN BUTTON
        login_btn = Button(main_frame, text="Login Now",command=self.login, font=("times new roman", 13, "bold"),
                              bg="darkblue", fg="white", width=20)
        login_btn.place(x=400, y=440)







    #Function
    def register_data(self):
        if self.f_name.get()=="" or self.var_email.get()=="" or self.var_ques.get()=="Select Security Question":
            messagebox.showerror("Error","All Fields are Required")

        elif self.var_password.get()!=self.var_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password must be same")

        # elif self.var_check.get()==0:
        #     messagebox.showerror("Error","Check Terms & Conditions")

        else:
            con = mysql.connector.connect(host="localhost", username="root", password="aayu14",
                                          database="security")
            my_cursor = con.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists....Please Login!")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.f_name.get(),self.l_name.get(),self.contact.get(),self.var_email.get(),self.var_ques.get(),self.var_answer.get(),self.var_password.get()
                ))

            con.commit()
            con.close()
            messagebox.showinfo("Success", "Registered successfully", parent=self.root)




    def login(self):
        self.new_window = Toplevel(self.root)
        self.app = security_login.Login_Window(self.new_window)








if __name__=="__main__":
    root=Tk()
    obj=register(root)
    root.mainloop()