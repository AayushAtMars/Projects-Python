from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import security_newUser
import mysql.connector
from main import Face_recognistion_system



class Login_Window:

    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # BG IMAGE
        img1 = Image.open("Images/bg_img.jpg")
        img1 = img1.resize((1530, 800))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1530, height=800)

        # MAIN FRAME
        main_frame = Frame(bg_img, bd=2, bg="black")
        main_frame.place(x=610, y=170, width=340, height=450)

        img2 = Image.open("Images/loginpd.jpg")
        img2 = img2.resize((100, 100))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img_lbl = Label(bg_img, image=self.photoimg2)
        img_lbl.place(x=730, y=175, width=100, height=100)

        # TITLE LABEL
        title_lbl = Label(main_frame, text="GET STARTED", font=("times new roman", 20, "bold"),
                          bg="black", fg="white")
        title_lbl.place(x=70, y=100)

        # USERNAME
        self.user_id = StringVar()
        id = Label(main_frame, text="Username ", font=("times new roman", 15, "bold"), bg="black",fg="white")
        id.place(x=60,y=152)

        # USERNAME ENTRY
        id_entry = ttk.Entry(main_frame, textvariable=self.user_id, width=20, font=("times new roman", 15, "bold"))
        id_entry.place(x=30,y=180,width=270)

        # PASSWORD
        self.pass_id = StringVar()
        id = Label(main_frame, text="Password ", font=("times new roman", 15, "bold"), bg="black", fg="white")
        id.place(x=60, y=225)

        # PASSWORD ENTRY
        id_entry = ttk.Entry(main_frame, textvariable=self.pass_id, width=20, font=("times new roman", 15, "bold"))
        id_entry.place(x=30, y=250, width=270)


        #ICON IMAGES


        #USERNAME ICON
        img3 = Image.open("Images/user_icon1.jpg")
        img3 = img3.resize((25, 25))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        img_lbl = Label(main_frame, image=self.photoimg3)
        img_lbl.place(x=30, y=155, width=25, height=25)


        #PASSWORD ICON
        img4 = Image.open("Images/password_icon.jpg")
        img4 = img4.resize((25, 25))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        img_lbl = Label(main_frame, image=self.photoimg4)
        img_lbl.place(x=30, y=225, width=25, height=25)


        #BUTTONS


        #LOGIN BUTTTON
        b1_text = Button(main_frame, text="Login",command=self.login,font=("times new roman", 15, "bold"),bd=3,relief=RIDGE, bg="darkblue", fg="white", cursor="hand2")
        b1_text.place(x=110, y=300, width=120, height=35)

        #REGISTER BUTTON
        b2_text = Button(main_frame, text="New User",command=self.new_user, font=("times new roman", 10, "bold"), borderwidth=0,bg="black", fg="white", cursor="hand2",activeforeground="white",activebackground="black")
        b2_text.place(x=15, y=350, width=60)


        #FORGET BUTTON
        b3_text = Button(main_frame, text="Forget Password", font=("times new roman", 10, "bold"), borderwidth=0, bg="black", fg="white", cursor="hand2",activeforeground="white",activebackground="black")
        b3_text.place(x=15, y=375, width=100)




    def login(self):
        con = mysql.connector.connect(host="localhost", username="root", password="aayu14",
                                      database="security")
        my_cursor = con.cursor()
        # my_cursor.execute("select * from register where email=%s and password=%s",(self.user_id.get(),self.pass_id.get()))
        query = "select * from register"
        my_cursor.execute(query)
        a = my_cursor.fetchall()
        count = 0
        for i in range(0, len(a)):
            if a[i][0] == self.user_id.get() and a[i][6] == self.pass_id.get():
                count = count + 1

        if self.user_id.get()=="" or self.pass_id=="":
            messagebox.showerror("Error","All fields are required")

        # elif self.user_id.get()=="aayush" and self.pass_id.get()=="aayu14":
        #     messagebox.showinfo("Success","Welcome to the Attendance System")
        elif(count>0):
        # else:
            self.new_window = Toplevel(self.root)
            self.app = Face_recognistion_system(self.new_window)

        else:
            messagebox.showerror("Error", "Invalid Username & Password")

            # row=my_cursor.fetchone()
            # if row!=None:
            #     messagebox.showerror("Error","Invalid Username & Password")

            # else:
            #     open_main=messagebox.askyesno("YesNO","Access only Admin")
            #     if open_main>0:
            #         self.new_window=Toplevel(self.root)
            #         self.app=Face_recognistion_system(self.new_window)





    def new_user(self):
        self.new_window = Toplevel(self.root)
        self.app = security_newUser.register(self.new_window)


if __name__=="__main__":
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()