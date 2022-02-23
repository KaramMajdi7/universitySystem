from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

# ********************************************************

def login_win():
    try:
        root.destroy()
        import logInPage
    except:
        pass


def clear():
    firstNameText.delete(0,END)
    lastNameText.delete(0,END)
    contactNumberText.delete(0,END)
    emailText.delete(0,END)
    answerText.delete(0,END)
    passwordText.delete(0,END)
    confirmPasswordText.delete(0,END)
    securityQuestionBox.current(0)
    check.set(0)


def register():
    if firstNameText.get() == '' or lastNameText.get() == '' or emailText.get() == '' or contactNumberText.get() == ''\
        or passwordText.get() == '' or confirmPasswordText.get() == '' or securityQuestionBox.get() == 'Select'\
            or answerText.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')

    elif passwordText.get() != confirmPasswordText.get():
        messagebox.showerror('Error', 'Password Mismatch')

    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Agree To Our Terms & Conditions')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='kkkmmm777', database='register')
            cur = con.cursor()
            cur.execute('select * from student where email=%s',emailText.get())
            row = cur.fetchone()
            if row != None:
                messagebox.showerror('Error', 'User Already Exists')

            else:
                cur.execute('insert into student(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)',
                            (firstNameText.get(),lastNameText.get(),contactNumberText.get(),emailText.get(),securityQuestionBox.get(),
                             answerText.get(),passwordText.get()))
                con.commit()
                con.close()

                messagebox.showinfo('Success', 'Registration Is Successful')
                clear()
                root.destroy()
                import logInPage

        except Exception as e:
            messagebox.showerror('Error', f'Error Due To {e}')


# ********************************************************

root = Tk()
root.geometry("1280x645+20+15")
root.title("Registration Form")


# ********************************************************

bgImage = PhotoImage(file="Images/imgQ.png")
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=-5, y=-5)

# ********************************************************

registerFrame = Frame(root, width=650, height=650)
registerFrame.place(x=630, y=0)

# ********************************************************

titleLabel = Label(registerFrame, text="Registration Form",
                   font=('arial', 22, 'bold'), fg="#384051")
titleLabel.place(x=20, y=25)

# ********************************************************

firstName = Label(registerFrame, text="First Name",
                  font=('times new roman', 18, 'bold'), fg="#282851")
firstName.place(x=20, y=80)

firstNameText = Entry(registerFrame, font=('times new roman', 18),
                      bg='#D7E9FD')
firstNameText.place(x=20, y=115)

# ********************************************************

lastName = Label(registerFrame, text="Last Name",
                 font=('times new roman', 18, 'bold'), fg="#282851")
lastName.place(x=370, y=80)

lastNameText = Entry(registerFrame, font=('times new roman', 18),
                     bg='#D7E9FD')
lastNameText.place(x=370, y=115)

# ********************************************************

contactNumber = Label(registerFrame, text="Contact Number",
                      font=('times new roman', 18, 'bold'), fg="#282851")
contactNumber.place(x=20, y=200)

contactNumberText = Entry(registerFrame, font=('times new roman', 18),
                          bg='#D7E9FD')
contactNumberText.place(x=20, y=235)

# ********************************************************

email = Label(registerFrame, text="Email",
              font=('times new roman', 18, 'bold'), fg="#282851")
email.place(x=370, y=200)

emailText = Entry(registerFrame, font=('times new roman', 18),
                  bg='#D7E9FD')
emailText.place(x=370, y=235)

# ********************************************************

securityQuestion = Label(registerFrame, text="Security Question",
                         font=('times new roman', 18, 'bold'), fg="#282851")
securityQuestion.place(x=20, y=320)

securityQuestionBox = ttk.Combobox(registerFrame, font=('times new roman', 16), state='readonly')
securityQuestionBox['values'] = ('Select', 'Your Favourite Color', 'Your Favourite language',
                                 'Your Birth Place')
securityQuestionBox.place(x=20, y=355)
securityQuestionBox.current(0)

# ********************************************************

answer = Label(registerFrame, text="Answer",
               font=('times new roman', 18, 'bold'), fg="#282851")
answer.place(x=370, y=320)

answerText = Entry(registerFrame, font=('times new roman', 18),
                   bg='#D7E9FD')
answerText.place(x=370, y=355)

# ********************************************************

password = Label(registerFrame, text="Password",
                 font=('times new roman', 18, 'bold'), fg="#282851")
password.place(x=20, y=440)

passwordText = Entry(registerFrame, font=('times new roman', 18),
                     bg='#D7E9FD', show='*')
passwordText.place(x=20, y=475)

# ********************************************************

confirmPassword = Label(registerFrame, text="Confirm Password",
                        font=('times new roman', 18, 'bold'), fg="#282851")
confirmPassword.place(x=370, y=440)

confirmPasswordText = Entry(registerFrame, font=('times new roman', 18),
                            bg='#D7E9FD', show='*')
confirmPasswordText.place(x=370, y=475)

# ********************************************************

check = IntVar()
checkButton = Checkbutton(registerFrame, text="I Agree To All The Terms & Conditions",
                          onvalue=1, offvalue=0, variable=check, font=('times new roman', 14, 'bold'), fg="#282851")
checkButton.place(x=20, y=530)

# ********************************************************


registerButton = Button(registerFrame, text='Register Now!', font=('arial',14,'bold'), bd=0, cursor='hand2',
                        command = register, bg="#007ae1", fg="white", width=12)
registerButton.place(x=250, y=580)

# ********************************************************


logInButton = Button(root, text='Login', font=('arial',18,'bold'),
                   bg='#00A7CE', fg='white', cursor='hand2', bd=0, activebackground='gray20',
                     activeforeground='white', command=login_win, width=10)
logInButton.place(x=220, y=250)



root.mainloop()
