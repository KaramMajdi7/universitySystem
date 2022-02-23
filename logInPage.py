from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from PIL import ImageTk, Image
import pywhatkit as pwt

def reset_pass():
    if mailEntry.get() == '':
        messagebox.showerror('Error', 'Please Enter The Email Address To Reset Your Password')

    else:
        con = pymysql.connect(host='localhost', user='root', password='kkkmmm777', database='register')
        cur = con.cursor()
        cur.execute('select * from student where email=%s', mailEntry.get())
        row = cur.fetchone()

        if row == None:
            messagebox.showerror('Error', 'Please Enter The Valid Email Address')
        else:
            con.close()

            def new_pass():
                if securityBox.get() == 'Select' or answerText2.get() == '' or passText.get() == '':
                    messagebox.showerror('Error', 'All Field Are Required')

                else:
                    con = pymysql.connect(host='localhost', user='root', password='kkkmmm777', database='register')
                    cur = con.cursor()
                    cur.execute('select * from student where email=%s and question=%s and answer=%s', (mailEntry.get(), securityBox.get(),
                                answerText2.get()))
                    row = cur.fetchone()

                    if row == None:
                        messagebox.showerror('Error', 'Security Question Or Answer Is Incorrect', parent=root2)

                    else:
                        cur.execute('update student set password=%s where email=%s',(passText.get(),mailEntry.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo('Success', 'Password Was Reseted Successfully', parent=root2)

                        securityBox.current(0)
                        answerText2.delete(0,END)
                        passText.delete(0,END)
                        root2.destroy()
                        mailEntry.delete(0,END)

            root2 = Toplevel()

            root2.geometry('470x560+400+60')
            root2.title('Forget Password')
            root2.config(bg='white')
            root2.focus_force()
            root2.grab_set()


            forgetLabel = Label(root2, text='Forget', font=('times new roman',22,'bold'), bg='white')
            forgetLabel.place(x=128, y=10)


            passwordLabel = Label(root2, text='Password', font=('times new roman', 22, 'bold'), bg='white', fg='#007ae1')
            passwordLabel.place(x=225, y=10)


            lockImage = PhotoImage(file='Images/pass.png')
            lockLabel = Label(root2, image=lockImage, bg='white')
            lockLabel.place(x=170, y=70)


            securityQuLabel = Label(root2, text='Security Questions', font=('times new roman',19,'bold'), bg='white')
            securityQuLabel.place(x=60, y=220)

            securityBox = ttk.Combobox(root2, font=('times new roman', 19), state='readonly', width=28)
            securityBox['values'] = ('Select', 'Your Favourite Color', 'Your Favourite language',
                                             'Your Birth Place')
            securityBox.place(x=60, y=260)
            securityBox.current(0)


            answerLabel = Label(root2, text="Answer",
                           font=('times new roman', 19, 'bold'), bg='white')
            answerLabel.place(x=60, y=310)

            answerText2 = Entry(root2, font=('times new roman', 19),
                               bg='white', width=30)
            answerText2.place(x=60, y=350)


            passNew = Label(root2, text="New Password",
                                font=('times new roman', 19, 'bold'), bg='white')
            passNew.place(x=60, y=400)

            passText = Entry(root2, font=('times new roman', 19),
                                bg='white', width=30)
            passText.place(x=60, y=440)


            changePass = Button(root2, text='Change Password', font=('arial', 17,'bold'),
                                bg='#007ae1', fg='white', cursor='hand2',
                                activebackground='#007ae1', activeforeground='white', bd=0, command=new_pass)
            changePass.place(x=130, y=500)


            root2.mainloop()


def register_win():
    try:
        window.destroy()
        import register
    except:
        pass




def signIn():
    if mailEntry.get() == '' or passwordEntry.get() == "":
        messagebox.showerror('Error', 'All Fields Are Required')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='kkkmmm777', database='register')
            cur = con.cursor()
            cur.execute('select * from student where email=%s and password=%s',(mailEntry.get(),passwordEntry.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror('Error', 'Invalid Email Or Password')
            else:
                root3 = Toplevel()

                root3.geometry('300x250+400+60')
                root3.title('Application Choice')
                root3.config(bg="#4E4E4E")
                root3.focus_force()
                root3.grab_set()



                def gpa():
                    try:
                        window.destroy()
                        import calcGPA
                        root3.destroy()
                    except:
                        pass

                def materialDet():
                    try:
                        window.destroy()
                        import materialInfo
                        root3.destroy()
                    except:
                        pass

                choice1 = Button(root3, text='GPA Calculator', font=('arial', 17, 'bold'),
                                    bg='#007ae1', fg='white', cursor='hand2',
                                    activebackground='#007ae1', activeforeground='white', bd=0, command=gpa)
                choice1.place(x=62, y=75)

                choice2 = Button(root3, text='Material Details', font=('arial', 17, 'bold'),
                                 bg='#007ae1', fg='white', cursor='hand2',
                                 activebackground='#007ae1', activeforeground='white', bd=0, command=materialDet)
                choice2.place(x=62, y=125)

                root3.mainloop()

            con.close()

        except Exception as e:
            messagebox.showerror('Error', f'Error Is Due To {e}')



window = Tk()

window.geometry('900x600+50+50')
window.title('Login Page')

bgloginImage = PhotoImage(file="Images/imgQ.png")
bgloginLabel = Label(window, image=bgloginImage)
bgloginLabel.place(x=-5, y=-5)

frame = Frame(window, width=560, height=320, bg='white')
frame.place(x=180, y=140)

userImage = PhotoImage(file='Images/userW2.png')
userLabel = Label(frame, image=userImage, bg='white')
userLabel.place(x=20, y=50)

mailLabel = Label(frame, text='Email', font=('arial',22,'bold'), bg='white', fg='#282851')
mailLabel.place(x=220, y=32)
mailEntry = Entry(frame, font=('arial',22), bg='#D7E9FD')
mailEntry.place(x=220, y=70)

passwordLabel = Label(frame, text='Password', font=('arial',22,'bold'), bg='white', fg='#282851')
passwordLabel.place(x=220, y=120)
passwordEntry = Entry(frame, font=('arial',22), bg='#D7E9FD', show = '*')
passwordEntry.place(x=220, y=160)

regButton = Button(frame, text='Register New Account?', font=('arial',12),
                   bd=0, bg='white', cursor='hand2', activebackground='white',
                   command=register_win)
regButton.place(x=220, y=200)

forgetButton = Button(frame, text='Forget Password?', font=('arial',12),
                   bd=0, bg='white', cursor='hand2', activebackground='white', fg='red',
                      activeforeground='red', command=reset_pass)
forgetButton.place(x=410, y=200)

logInButton = Button(frame, text='Login', font=('arial',18,'bold'),
                   bg='#0D98C7', fg='white', cursor='hand2', bd=0, activebackground='gray20',
                     activeforeground='white', command=signIn)
logInButton.place(x=450, y=240)



window.mainloop()