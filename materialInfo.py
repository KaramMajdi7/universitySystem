from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import webbrowser
import tkinter as tk
from tkinter import messagebox


#*********************** Functions ***********************

def exit():
    try:
        root.destroy()
        import register
    except:
        pass



def callback(url):
   webbrowser.open_new_tab(url)

def search():

    # **************************************
    if materialText.get() == "AR111":
        root4 = Toplevel()
        root4.title("AR111")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Arabic Communication Skills (I)", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="3 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="None", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year, in first semester or second semester", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Mandatory", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=500, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="Arabic level one language, you can pass it if you get a grade of 60 or more in the test exam before you enter the university.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="it's an easy level language which contains basic arabic grammar and basic reading for beginners, and you can study for the slides of the course from the material on the LMS.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=480)

        root4.mainloop()

    # **************************************
    if materialText.get() == "AR112":
        root4 = Toplevel()
        root4.title("AR112")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Arabic Communication Skills (II)", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="3 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="AR111", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year, in second semester or in fourth year.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Mandatory", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=500, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="Arabic level two language, you can pass it if you get a grade of 80 or more in the test exam before you enter the university.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="it's an easy level language which contains basic arabic grammar and basic reading and poems for beginners, and you can study for the slides of the course from the material on the LMS.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=480)

        root4.mainloop()

    #**************************************
    if materialText.get() == "EL111":
        root4 = Toplevel()
        root4.title("EL111")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="English Communication Skills (I)", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="3 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="None", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year, in first semester or in second semester.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Mandatory", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=500, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="English level one language, you can pass it if you get a grade of between 80 and 95 or more in the test exam before you enter the university.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="it's an easy level language which contains basic english grammar and basic reading for beginners, and you can study for the slides of the course from the material on the LMS.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=480)

        root4.mainloop()

#**************************************
    if materialText.get() == "EL112":
        root4 = Toplevel()
        root4.title("EL112")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="English Communication Skills (II)", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="3 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="EL111", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year, in second semester or in fourth year.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Mandatory", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=500, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="English level two language, you can pass it if you get a grade of 95 or more in the test exam before you enter the university.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="it's an easy level language which contains basic english grammar and basic reading and the most important thing which is writing for beginners, and you can study for the slides of the course from the material on the LMS.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        root4.mainloop()

#**************************************
    if materialText.get() == "GR101":
        root4 = Toplevel()
        root4.title("GR101")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Self-Learning Skills", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="3 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="None", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year, in first semester or in second semester.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Mandatory", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=500, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="It's one of the most important elective material for the university.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="it's an easy course with so much knowledge you can get from it and how to be a self learner, and you can study for the slides of the course from the material on the LMS.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        root4.mainloop()

#**************************************
    if materialText.get() == "TU170":
        root4 = Toplevel()
        root4.title("TU170")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Computing Essentials", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="3 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="None", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year, in first semester or in second semester.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Mandatory", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=500, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="It's one of the most important elective material for the university.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="it's an easy course for CS students because of the basic computer skills it contain, and you can study for the slides of the course from the material on the LMS.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        root4.mainloop()

#**************************************
    if materialText.get() == "GR131":
        root4 = Toplevel()
        root4.title("GR131")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="History and Civilization of EGYPT", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="3 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="None", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year, or fourth year.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Elective", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=500, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="It's one of the elective material you can pick for the university, and you must choose at least one.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You could read articles from the internet, and you can study for the slides of the course from the material on the LMS.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        root4.mainloop()

#**************************************
    if materialText.get() == "GR111":
        root4 = Toplevel()
        root4.title("GR111")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Arab Islamic Civilization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="3 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="None", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year, or fourth year.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Elective", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=500, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="It's one of the elective material you can pick for the university, and you must choose at least one.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You could read articles from the internet, and you can study for the slides of the course from the material on the LMS.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        root4.mainloop()

#**************************************
    if materialText.get() == "EL118":
        root4 = Toplevel()
        root4.title("EL118")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Reading", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="4 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="EL111", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year, or fourth year.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Elective", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=500, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="It's one of the elective material you can pick for the university, and you must choose at least one.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You could read articles from the internet, and you can study for the slides of the course from the material on the LMS.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        root4.mainloop()

#**************************************
    if materialText.get() == "GR121":
        root4 = Toplevel()
        root4.title("GR121")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Environment and Health", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="3 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="None", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year, or fourth year.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Elective", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=500, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="It's one of the elective material you can pick for the university, and you must choose at least one.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You could read articles from the internet, and you can study for the slides of the course from the material on the LMS.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        root4.mainloop()

#**************************************
    if materialText.get() == "MT131":
        root4 = Toplevel()
        root4.title("MT131")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Discrete Mathematics", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="4 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="EL111", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year, or Second year.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="It's one of the Specialization material you must take , and it's a helpful math material to take, especially in Machine Learning.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You should solve alot of examples from the course material and the internet, and you can study for the slides of the course, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.MT131_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1AIHfPnLyfFIujACHcnHb4pzF624aB49l"))
        link.place(x=405, y=540)

        root4.mainloop()

#**************************************
    if materialText.get() == "MT132":
        root4 = Toplevel()
        root4.title("MT132")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Linear Algebra", font=('Helvetica', 16, 'bold'), fg='white', bg="#6EBFC3")
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="4 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="EL111", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="Second year, in first semester or second semester.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=550)
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="It's one of the Specialization material you must take , and it's a helpful math material to take, especially in Data Science.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You should solve alot of examples from the course material and the internet, and you can study for the slides of the course, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.MT132_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1unXx15wkRtpCZmOPJkNYRfjyAli9OuCV"))
        link.place(x=405, y=540)

        root4.mainloop()


#**************************************
    if materialText.get() == "TM103":
        root4 = Toplevel()
        root4.title("TM103")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Computer Organization and Architecture", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="4 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="EL111", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="Second year, in first semester or second semester.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="It's one of the Specialization material you must take , and it's a helpful material to understand more about the inside processes of the computer.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You should solve alot of examples and watch videos from the internet , and you can study for the slides of the course, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.TM103_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1sXR1ZwmLvlYB751ceGKlHWs_OoTYwWxo"))
        link.place(x=325, y=540)

        root4.mainloop()

#**************************************
    if materialText.get() == "TM105":
        root4 = Toplevel()
        root4.title("TM105")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Introduction to Programming", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="4 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="EL111", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year in second semester or in second year first semester.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='coral1')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="The most important one to begin with, it will enter you in the programming world, and a good Java basics to understand.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You should solve alot of examples and try to think of an idea to program and to solve using the syntax you will learn, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.TM105_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1-_-4zJo5Svp-AxgtuQVPVZ43slEXf6t_"))
        link.place(x=250, y=540)

        root4.mainloop()

#**************************************
    if materialText.get() == "TM111":
        root4 = Toplevel()
        root4.title("TM111")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Introduction to Computing and Information Technology (I)", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="8 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="EL111", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year in second semester or in second year first semester.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="A good material to take to understand about pseudo code and how write one, and to understand about the flow of any code.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You must study from the course material and from some videos about pseudo code on the internet, and you could check the material on the LMS, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.TM111_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1efiAx59o9mKaWTjDlmP86-cGxeBWZTyO"))
        link.place(x=538, y=540)

        root4.mainloop()


#**************************************
    if materialText.get() == "TM112":
        root4 = Toplevel()
        root4.title("TM112")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Introduction to Computing and Information Technology (II)", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="8 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="TM111", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="Second year in first semester or in second semester.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='coral1')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="A good material to take to understand more about how a compuer works, and to understand about PYTHON with a little introduction about it.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You must study from the course material and from some videos on python, and you could check the material on the LMS, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.TM112_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1MyubGnIOcQO8LqjoIHV3rgyygHVTls6o"))
        link.place(x=250, y=540)

        root4.mainloop()

#**************************************
    if materialText.get() == "M251":
        root4 = Toplevel()
        root4.title("M251")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Object-Oriented Programming using Java", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="8 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="TM105", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="Second year in first semester or in second semester.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="One of the most important materials, you will underdstand about the oop concept using java, and it will talk in depth about the oop pillars.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You must study from the course material and from some videos on Java and you could read some articles on oop, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.M251_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1u8a9jZHu7lqqxk0rZizai2kw59XetF_x"))
        link.place(x=250, y=540)

        root4.mainloop()

#**************************************
    if materialText.get() == "M269":
        root4 = Toplevel()
        root4.title("M269")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Algorithms, Data Structures and Computability", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="8 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="TM105 & MT131", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="Second year in second semester.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="One of the most important materials, you will underdstand about the data starcture and algorithm concept using python.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You must study from the course material and from some videos on data structure, and solve some problems on the internet, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.M269_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1MEu_KQOv_OHoGHCOCp86_cHoDM5RrV7E"))
        link.place(x=320, y=540)

        root4.mainloop()


#**************************************
    if materialText.get() == "T227":
        root4 = Toplevel()
        root4.title("T227")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Change, Strategy and Project at Work", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="8 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="TM112", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="Third year in first semester or in second semester.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="AN IMPORTANT MATERIAL TO TAKE, AND IT HELPS TO UNDERSTAND MORE ON HOW TO WORK ON A PROJECT WITH PUTTING A STRATEGY.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You must study from the course material , AND WRITE THE THINGS YOU UNDERSTAND BY YOUR OWN WORDS, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.T227_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1GLT_iz4DYF6PajtMS98OFp8QHEOjIWAH"))
        link.place(x=250, y=540)

        root4.mainloop()

#**************************************
    if materialText.get() == "TM240":
        root4 = Toplevel()
        root4.title("TM240")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Computer Graphics and Multimedia", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="4 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="TM105 & MT132", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="Third year in first semester or in second semester.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="A GOOD MATERIAL TO TAKE, IT SHOW GRAPHICAL REPRESENTATION USING JAVA OOP USING A COUPLE OF LIBRARIES IN JAVA.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You must study from the course material , AND TRY TO SOLVE SOME EXAMPLES ON THE INTERNET USING JAVA, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.TM240_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/10O56pnkhCLkuwzsB0QQIcsLDrhSxADJM"))
        link.place(x=250, y=540)

        root4.mainloop()

#**************************************
    if materialText.get() == "MT101":
        root4 = Toplevel()
        root4.title("MT101")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="General Mathematics", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="3 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="None", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year or fourth year.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Computer Science Electives", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="A material you will pick from the university faculty electives, it talks about math in a general perspective.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You must study from the course material , and try to solve some examples, and you could find the course material on the LMS.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        root4.mainloop()


#**************************************
    if materialText.get() == "MT129":
        root4 = Toplevel()
        root4.title("TM240")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Calculus and Probability", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="4 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="EL099", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year, in first semester or in second semester.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=300, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Computer Science Mandatory", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="A material that you must take in the CS field, it talks about calculus and in details about derivatives and integration.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You must study from the course material , AND TRY TO SOLVE SOME EXAMPLES from the internet, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.MT129_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1ALvhoKeC2RsZ7OXACszqMK8FZMxYSRyF"))
        link.place(x=540, y=517)

        root4.mainloop()

#**************************************
    if materialText.get() == "M109":
        root4 = Toplevel()
        root4.title("M109")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text=".NET Programming", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="3 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="EL111", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year or in fourth year.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=390, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Computer Science Electives", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="A material you will pick from the university faculty electives, it talks about C# in a general perspective.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You must study from the course material , and try some problem solving using C#, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.M109_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1iqTi45HNIqT5-7XTuuvgPQkMgAtCN0Mi"))
        link.place(x=405, y=517)

        root4.mainloop()

#**************************************
    if materialText.get() == "MS102":
        root4 = Toplevel()
        root4.title("MS102")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Physics", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="3 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="EL111", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="First year or in fourth year.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=400, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Computer Science Electives", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="A material you will pick from the university faculty electives, it talks about Pyhsics in a general perspective.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You must study from the course material , and study from the LMS material then try to write what you have understood in your own words, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.MS102_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1PVhu2i_RLcByGd4e3tf5rWXH1x_TyRaK"))
        link.place(x=539, y=543)

        root4.mainloop()

#**************************************
    if materialText.get() == "TM298":
        root4 = Toplevel()
        root4.title("TM298")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Operating Systems", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="4 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="TM105 & TM103", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="Third year.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=450, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="It's an important material to take, it'S about the work flow of a process, and some algorithms that free space for the process in memory.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You must study from the course material , and study from the LMS material then try to write what you have understood in your own words, and watch some videos fromthe internet,and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.TM298_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1PBDAJLoC2Hox-9B8CmTmTniM-FCVPcbA"))
        link.place(x=470, y=567)

        root4.mainloop()

#**************************************
    if materialText.get() == "TM351":
        root4 = Toplevel()
        root4.title("TM351")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Data Management and Analysis", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="8 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="M269 & M251", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="Third year.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=450, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="It's an important material to take, you will learn how to analyze the data and manage it, very important material for data science, and you will use it in the graduation project.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=360)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You must study from the course material , and study from the LMS material then try to write what you have understood in your own words, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.TM351_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg="#6EBFC3")
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1Sl4rK_MAvfMgNWJl787hLOHGLuRqVTwR"))
        link.place(x=538, y=542)

        root4.mainloop()

#**************************************
    if materialText.get() == "TM354":
        root4 = Toplevel()
        root4.title("TM354")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Software Engineering", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=450, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="8 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=470, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="M251", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=470, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="Third year", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=470, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="It's an important material to take, you will learn about the Software Engineering concepts, and the workflow of a software project, and you will use it in the graduation project.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=360)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You must study from the course material, and study from the LMS material, and try to think of a project and apply Software Engineering concepts, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.TM354_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/11qUZ4v9SvemSUicMyOcFZkNbUI5CTWQ4"))
        link.place(x=320, y=542)

        root4.mainloop()


#**************************************
    if materialText.get() == "TM366":
        root4 = Toplevel()
        root4.title("TM366")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Artificial Intelligence", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="8 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="M269", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="Third year or fourth year.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=450, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="It's an important material to take, you will learn about feature field which is Artificial Intelligence, and the wonderful concept of Machine Learning.", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=250, y=360)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="You must study from the course material , and study from the LMS material, and try to describe what have you understood in your own words, and solve some exams from:", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=250, y=470)

        link = Label(root4, text="www.TM366_EXAMS.com", font=('Helveticabold', 15), fg="blue", cursor="hand2", bg='#6EBFC3')
        link.pack()
        link.bind("<Button-1>", lambda e:callback("https://drive.google.com/drive/u/0/folders/1gd80KnzpAvx4asVj0xHJDgQq1ZgniuhW"))
        link.place(x=540, y=542)

        root4.mainloop()


#**************************************
    if materialText.get() == "TM471A":
        root4 = Toplevel()
        root4.title("TM471A")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Graduation Project Part A", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=300, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="4 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=500, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="TM351 & TM354 & TM366", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=500, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="Third year IN SECOND semester or fourth year.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=380, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=465, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="None", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=470, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="None", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=470, y=490)

        root4.mainloop()


#**************************************
    if materialText.get() == "TM471B":
        root4 = Toplevel()
        root4.title("TM471B")
        root4.config(bg="#6EBFC3")
        root4.geometry('890x600+200+50')
        root4.resizable(False, False)
        root4.grab_set()

        nameLabel = Label(root4, text='Name', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        nameLabel.place(x=20, y=30)

        titlenameLabel = Label(root4, text="Graduation Project Part B", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        titlenameLabel.place(x=450, y=30)

        hoursLabel = Label(root4, text='Number Of Hours', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        hoursLabel.place(x=20, y=100)

        hoursEntry = Label(root4, text="4 Hours", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        hoursEntry.place(x=450, y=100)

        preLabel = Label(root4, text='Prerequisite', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        preLabel.place(x=20, y=170)

        prenameLabel = Label(root4, text="Graduation Project Part A", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        prenameLabel.place(x=450, y=170)

        runtimeLabel = Label(root4, text='When To Take It', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        runtimeLabel.place(x=20, y=240)

        runtimenameLabel = Label(root4, text="fourth year.", wraplength=550, font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        runtimenameLabel.place(x=450, y=240)

        TypeLabel = Label(root4, text='Material Type', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        TypeLabel.place(x=20, y=310)

        typenameLabel = Label(root4, text="Specialization", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3')
        typenameLabel.place(x=450, y=310)

        AboutLabel = Label(root4, text='About', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        AboutLabel.place(x=20, y=380)

        AboutnameLabel = Label(root4, text="None", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3', wraplength=615, justify=LEFT)
        AboutnameLabel.place(x=470, y=380)

        castLabel = Label(root4, text='Way to study', font=('Helvetica', 20, 'bold'), fg='black', bg='#6EBFC3')
        castLabel.place(x=20, y=480)

        castnameLabel = Label(root4, text="None", font=('Helvetica', 16, 'bold'), fg='white', bg='#6EBFC3',
                              wraplength=615, justify=LEFT)
        castnameLabel.place(x=470, y=490)

        root4.mainloop()

    if materialText.get() == "":
        messagebox.showerror("Error", "Please enter the material name to search for!")

    else:
        messagebox.showerror("Error", "Please enter a valid material name, if you need some help press the CS material button.")



def view():
    root3 = Toplevel()
    root3.title("CS Plan")
    root3.config(bg="#727272")
    root3.geometry('300x300+150+100')
    root3.resizable(False, False)
    root3.overrideredirect(1)

    def yearThree():



        def show_frame(frame):
            frame.grid(row=0, column=0)


        def delete2(frame):
            frame.grid_remove()

        window = Tk()

        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)

        frame1 = Frame(window, bg="#727272")
        frame2 = Frame(window, bg="#727272")
        frame3 = Frame(window, bg="#727272")
        frame4 = Frame(window, bg="#727272")




        # ==================Frame 1 code
        # ************ First Year **********************

        materialFirst = Label(frame1, text="First Year", font=("arial", 16, "bold"), bg="#727272", fg="white")
        materialFirst.pack()

        firstSemester = Label(frame1, text="First Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        firstSemester.pack()
        # Add a Treeview widget
        tree = ttk.Treeview(frame1, column=("c1", "c2", "c3"), show='headings', height=6)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Number")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Material Name")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree.insert('', 'end', text="1", values=('1', 'EL112', '3'))
        tree.insert('', 'end', text="2", values=('2', 'AR111', '3'))
        tree.insert('', 'end', text="3", values=('3', 'TU170', '3'))
        tree.insert('', 'end', text="4", values=('4', 'GR101', '3'))
        tree.insert('', 'end', text="5", values=('5', 'GR131', '3'))
        tree.insert('', 'end', text="6", values=('6', 'MT129', '4'))
        tree.pack()

        secondSemester = Label(frame1, text="Second Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        secondSemester.pack()
        tree2 = ttk.Treeview(frame1, column=("c1", "c2", "c3"), show='headings', height=4)
        tree2.column("# 1", anchor=CENTER)
        tree2.heading("# 1", text="Number")
        tree2.column("# 2", anchor=CENTER)
        tree2.heading("# 2", text="Material Name")
        tree2.column("# 3", anchor=CENTER)
        tree2.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree2.insert('', 'end', text="1", values=('1', 'TM105', '4'))
        tree2.insert('', 'end', text="2", values=('2', 'TM111', '8'))
        tree2.insert('', 'end', text="3", values=('3', 'AR112', '3'))
        tree2.insert('', 'end', text="4", values=('4', 'MT131', '4'))
        tree2.pack()

        all_commands = lambda: [show_frame(frame2), delete2(frame1)]


        frame11_btn = tk.Button(frame1, text='Next', command=all_commands, font=('FELIX TITLING', 12, 'bold'),
                     bg="black", fg='white', cursor='hand2')
        frame11_btn.pack(side=RIGHT)


        # ==================Frame 2 code
        # ************ Second Year **********************


        materialSecond = Label(frame2, text="Second Year", font=("arial", 16, "bold"), bg="#727272", fg="white")
        materialSecond.pack()

        firstSemester = Label(frame2, text="First Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        firstSemester.pack()
        # Add a Treeview widget
        tree = ttk.Treeview(frame2, column=("c1", "c2", "c3"), show='headings', height=3)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Number")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Material Name")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree.insert('', 'end', text="1", values=('1', 'MT132', '4'))
        tree.insert('', 'end', text="2", values=('2', 'TM112', '8'))
        tree.insert('', 'end', text="3", values=('3', 'M251', '8'))
        tree.pack()

        secondSemester = Label(frame2, text="Second Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        secondSemester.pack()
        tree2 = ttk.Treeview(frame2, column=("c1", "c2", "c3"), show='headings', height=4)
        tree2.column("# 1", anchor=CENTER)
        tree2.heading("# 1", text="Number")
        tree2.column("# 2", anchor=CENTER)
        tree2.heading("# 2", text="Material Name")
        tree2.column("# 3", anchor=CENTER)
        tree2.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree2.insert('', 'end', text="1", values=('1', 'M269', '8'))
        tree2.insert('', 'end', text="2", values=('2', 'TM260', '4'))
        tree2.insert('', 'end', text="3", values=('3', 'MS102', '3'))
        tree2.insert('', 'end', text="4", values=('4', 'TM103', '4'))
        tree2.pack()

        all_commands2 = lambda: [show_frame(frame1), delete2(frame2)]
        all_commands22 = lambda: [show_frame(frame3), delete2(frame2)]

        frame2_btn = tk.Button(frame2, text='Previous', command=all_commands2, font=('FELIX TITLING', 12, 'bold'),
                     bg="black", fg='white', cursor='hand2')
        frame2_btn.pack(side=LEFT)


        frame22_btn = tk.Button(frame2, text='Next', command=all_commands22, font=('FELIX TITLING', 12, 'bold'),
                     bg="black", fg='white', cursor='hand2')
        frame22_btn.pack(side=RIGHT)

        # ************ Third Year **********************

        materialThird = Label(frame3, text="Third Year", font=("arial", 16, "bold"), bg="#727272", fg="white")
        materialThird.pack()

        firstSemester = Label(frame3, text="First Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        firstSemester.pack()
        # Add a Treeview widget
        tree = ttk.Treeview(frame3, column=("c1", "c2", "c3"), show='headings', height=3)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Number")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Material Name")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree.insert('', 'end', text="1", values=('1', 'TM354', '8'))
        tree.insert('', 'end', text="2", values=('2', 'TM298', '4'))
        tree.insert('', 'end', text="3", values=('3', 'TM351', '8'))
        tree.pack()

        secondSemester = Label(frame3, text="Second Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        secondSemester.pack()
        tree2 = ttk.Treeview(frame3, column=("c1", "c2", "c3"), show='headings', height=3)
        tree2.column("# 1", anchor=CENTER)
        tree2.heading("# 1", text="Number")
        tree2.column("# 2", anchor=CENTER)
        tree2.heading("# 2", text="Material Name")
        tree2.column("# 3", anchor=CENTER)
        tree2.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree2.insert('', 'end', text="1", values=('1', 'TM240', '4'))
        tree2.insert('', 'end', text="2", values=('2', 'TM471 Part A', '4'))
        tree2.insert('', 'end', text="3", values=('3', 'T227', '8'))
        tree2.insert('', 'end', text="4", values=('4', 'M109', '3'))
        tree2.pack()


        all_commands3 = lambda: [show_frame(frame2), delete2(frame3)]
        all_commands33 = lambda: [show_frame(frame4), delete2(frame3)]


        frame3_btn = tk.Button(frame3, text='Previous', command=all_commands3, font=('FELIX TITLING', 12, 'bold'),
                     bg="black", fg='white', cursor='hand2')
        frame3_btn.pack(side=LEFT)

        frame33_btn = tk.Button(frame3, text='Next', command=all_commands33, font=('FELIX TITLING', 12, 'bold'),
                     bg="black", fg='white', cursor='hand2')
        frame33_btn.pack(side=RIGHT)

        # ************ Fourth Year **********************

        materialFourth = Label(frame4, text="Fourth Year", font=("arial", 16, "bold"), bg="#727272", fg="white")
        materialFourth.pack()

        firstSemester = Label(frame4, text="First Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        firstSemester.pack()
        # Add a Treeview widget
        tree = ttk.Treeview(frame4, column=("c1", "c2", "c3"), show='headings', height=2)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Number")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Material Name")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree.insert('', 'end', text="1", values=('1', 'TM366', '8'))
        tree.insert('', 'end', text="2", values=('2', 'TM471 Part B', '4'))
        tree.pack()

        all_commands4 = lambda: [show_frame(frame3), delete2(frame4)]

        frame4_btn = tk.Button(frame4, text='Previous', command=all_commands4, font=('FELIX TITLING', 12, 'bold'),
                     bg="black", fg='white', cursor='hand2')
        frame4_btn.pack(side=LEFT)


        show_frame(frame1)

        window.mainloop()



    #***********************************************************

    def yearFour():



        def show_frame(frame):
            frame.grid(row=0, column=0)


        def delete2(frame):
            frame.grid_remove()

        window = Tk()


        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)

        frame1 = Frame(window, bg="#727272")
        frame2 = Frame(window, bg="#727272")
        frame3 = Frame(window, bg="#727272")
        frame4 = Frame(window, bg="#727272")




        # ==================Frame 1 code
        # ************ First Year **********************

        materialFirst = Label(frame1, text="First Year", font=("arial", 16, "bold"), bg="#727272", fg="white")
        materialFirst.pack()

        firstSemester = Label(frame1, text="First Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        firstSemester.pack()
        # Add a Treeview widget
        tree = ttk.Treeview(frame1, column=("c1", "c2", "c3"), show='headings', height=6)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Number")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Material Name")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree.insert('', 'end', text="1", values=('1', 'EL112', '3'))
        tree.insert('', 'end', text="2", values=('2', 'AR111', '3'))
        tree.insert('', 'end', text="3", values=('3', 'TU170', '3'))
        tree.insert('', 'end', text="4", values=('4', 'GR101', '3'))
        tree.insert('', 'end', text="5", values=('5', 'GR131', '3'))
        tree.insert('', 'end', text="6", values=('6', 'MT129', '4'))
        tree.pack()

        secondSemester = Label(frame1, text="Second Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        secondSemester.pack()
        tree2 = ttk.Treeview(frame1, column=("c1", "c2", "c3"), show='headings', height=4)
        tree2.column("# 1", anchor=CENTER)
        tree2.heading("# 1", text="Number")
        tree2.column("# 2", anchor=CENTER)
        tree2.heading("# 2", text="Material Name")
        tree2.column("# 3", anchor=CENTER)
        tree2.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree2.insert('', 'end', text="1", values=('1', 'TM105', '4'))
        tree2.insert('', 'end', text="2", values=('2', 'TM111', '8'))
        tree2.insert('', 'end', text="3", values=('3', 'AR112', '3'))
        tree2.insert('', 'end', text="4", values=('4', 'MT131', '4'))
        tree2.pack()

        all_commands = lambda: [show_frame(frame2), delete2(frame1)]


        frame11_btn = tk.Button(frame1, text='Next', command=all_commands, font=('FELIX TITLING', 12, 'bold'),
                     bg="black", fg='white', cursor='hand2')
        frame11_btn.pack(side=RIGHT)


        # ==================Frame 2 code
        # ************ Second Year **********************

        materialSecond = Label(frame2, text="Second Year", font=("arial", 16, "bold"), bg="#727272", fg="white")
        materialSecond.pack()

        firstSemester = Label(frame2, text="First Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        firstSemester.pack()
        # Add a Treeview widget
        tree = ttk.Treeview(frame2, column=("c1", "c2", "c3"), show='headings', height=3)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Number")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Material Name")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree.insert('', 'end', text="1", values=('1', 'MT132', '4'))
        tree.insert('', 'end', text="2", values=('2', 'TM112', '8'))
        tree.insert('', 'end', text="3", values=('3', 'M251', '8'))
        tree.pack()

        secondSemester = Label(frame2, text="Second Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        secondSemester.pack()
        tree2 = ttk.Treeview(frame2, column=("c1", "c2", "c3"), show='headings', height=4)
        tree2.column("# 1", anchor=CENTER)
        tree2.heading("# 1", text="Number")
        tree2.column("# 2", anchor=CENTER)
        tree2.heading("# 2", text="Material Name")
        tree2.column("# 3", anchor=CENTER)
        tree2.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree2.insert('', 'end', text="1", values=('1', 'M269', '8'))
        tree2.insert('', 'end', text="2", values=('2', 'TM260', '4'))
        tree2.insert('', 'end', text="3", values=('3', 'MS102', '3'))
        tree2.insert('', 'end', text="4", values=('4', 'TM103', '4'))
        tree2.pack()

        all_commands2 = lambda: [show_frame(frame1), delete2(frame2)]
        all_commands22 = lambda: [show_frame(frame3), delete2(frame2)]

        frame2_btn = tk.Button(frame2, text='Previous', command=all_commands2, font=('FELIX TITLING', 12, 'bold'),
                     bg="black", fg='white', cursor='hand2')
        frame2_btn.pack(side=LEFT)


        frame22_btn = tk.Button(frame2, text='Next', command=all_commands22, font=('FELIX TITLING', 12, 'bold'),
                     bg="black", fg='white', cursor='hand2')
        frame22_btn.pack(side=RIGHT)

        # ************ Third Year **********************

        materialThird = Label(frame3, text="Third Year", font=("arial", 16, "bold"), bg="#727272", fg="white")
        materialThird.pack()

        firstSemester = Label(frame3, text="First Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        firstSemester.pack()
        # Add a Treeview widget
        tree = ttk.Treeview(frame3, column=("c1", "c2", "c3"), show='headings', height=2)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Number")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Material Name")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree.insert('', 'end', text="1", values=('1', 'TM354', '8'))
        tree.insert('', 'end', text="2", values=('2', 'TM298', '4'))
        tree.pack()

        secondSemester = Label(frame3, text="Second Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        secondSemester.pack()
        tree2 = ttk.Treeview(frame3, column=("c1", "c2", "c3"), show='headings', height=3)
        tree2.column("# 1", anchor=CENTER)
        tree2.heading("# 1", text="Number")
        tree2.column("# 2", anchor=CENTER)
        tree2.heading("# 2", text="Material Name")
        tree2.column("# 3", anchor=CENTER)
        tree2.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree2.insert('', 'end', text="1", values=('1', 'TM240', '4'))
        tree2.insert('', 'end', text="2", values=('2', 'TM351', '8'))
        tree2.insert('', 'end', text="3", values=('3', 'T227', '8'))
        tree2.pack()


        all_commands3 = lambda: [show_frame(frame2), delete2(frame3)]
        all_commands33 = lambda: [show_frame(frame4), delete2(frame3)]


        frame3_btn = tk.Button(frame3, text='Previous', command=all_commands3, font=('FELIX TITLING', 12, 'bold'),
                     bg="black", fg='white', cursor='hand2')
        frame3_btn.pack(side=LEFT)

        frame33_btn = tk.Button(frame3, text='Next', command=all_commands33, font=('FELIX TITLING', 12, 'bold'),
                     bg="black", fg='white', cursor='hand2')
        frame33_btn.pack(side=RIGHT)

        # ************ Fourth Year **********************

        materialFourth = Label(frame4, text="Fourth Year", font=("arial", 16, "bold"), bg="#727272", fg="white")
        materialFourth.pack()

        firstSemester = Label(frame4, text="First Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        firstSemester.pack()
        # Add a Treeview widget
        tree = ttk.Treeview(frame4, column=("c1", "c2", "c3"), show='headings', height=2)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Number")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Material Name")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree.insert('', 'end', text="1", values=('1', 'TM366', '8'))
        tree.insert('', 'end', text="2", values=('2', 'TM471 Part A', '4'))
        tree.pack()

        secondSemester = Label(frame4, text="Second Semester", font=("arial", 16, "bold"), bg="#727272", fg="white")
        secondSemester.pack()
        tree2 = ttk.Treeview(frame4, column=("c1", "c2", "c3"), show='headings', height=2)
        tree2.column("# 1", anchor=CENTER)
        tree2.heading("# 1", text="Number")
        tree2.column("# 2", anchor=CENTER)
        tree2.heading("# 2", text="Material Name")
        tree2.column("# 3", anchor=CENTER)
        tree2.heading("# 3", text="Number of hours")
        # Insert the data in Treeview widget
        tree2.insert('', 'end', text="1", values=('1', 'M109', '3'))
        tree2.insert('', 'end', text="2", values=('2', 'TM471 Part B', '4'))
        tree2.pack()

        all_commands4 = lambda: [show_frame(frame3), delete2(frame4)]

        frame4_btn = tk.Button(frame4, text='Previous', command=all_commands4, font=('FELIX TITLING', 12, 'bold'),
                     bg="black", fg='white', cursor='hand2')
        frame4_btn.pack(side=LEFT)


        show_frame(frame1)

        window.mainloop()

    def cancel():
        root3.destroy()


    choice1 = Button(root3, text='3.5 Years', font=('FELIX TITLING', 20, 'bold'),
                     bg='black', fg='white', cursor='hand2',
                     activebackground='black', activeforeground='white', bd=0, command=yearThree)
    choice1.place(x=70, y=85)


    choice2 = Button(root3, text='4 Years', font=('FELIX TITLING', 20, 'bold'),
                     bg='black', fg='white', cursor='hand2',
                     activebackground='black', activeforeground='white', bd=0, command=yearFour)
    choice2.place(x=70, y=160)

    cancelButton = Button(root3, text='Cancel', font=('FELIX TITLING', 14, 'bold'),
                     bg='#61FFFF', fg='black', cursor='hand2',
                     activebackground='#61FFFF', activeforeground='black', bd=0, command=cancel, width=6, height=1)
    cancelButton.place(x=200, y=255)




    root3.mainloop()





def open():
    root2 = Toplevel()
    root2.title("CS Material")
    root2.config(bg="#9EB7BC")
    root2.geometry('570x415+120+80')

    materialFrame = Frame(root2, bd=10, relief=RIDGE, bg="black")
    materialFrame.pack(side=LEFT)

    materialGrade = LabelFrame(materialFrame, text="Mandatory", font=("arial", 19, "bold"),
                               bd=10, relief=RIDGE, fg="#007ae1")
    materialGrade.pack(side=LEFT)

    materialGrade2 = LabelFrame(materialFrame, text="Specialization", font=("arial", 19, "bold"),
                                bd=10, relief=RIDGE, fg="#007ae1")
    materialGrade2.pack(side=LEFT)

    materialGrade3 = LabelFrame(materialFrame, text="Specialization", font=("arial", 19, "bold"),
                                bd=10, relief=RIDGE, fg="#007ae1")
    materialGrade3.pack(side=LEFT)

    AR111 = Label(materialGrade, text="AR111", font=("arial", 18, "bold"), fg="#384051")
    AR111.grid(row=0, column=0)

    AR112 = Label(materialGrade, text="AR112", font=("arial", 18, "bold"), fg="#384051")
    AR112.grid(row=1, column=0)

    EL111 = Label(materialGrade, text="EL111", font=("arial", 18, "bold"), fg="#384051")
    EL111.grid(row=2, column=0)

    EL112 = Label(materialGrade, text="EL112", font=("arial", 18, "bold"), fg="#384051")
    EL112.grid(row=3, column=0)

    GR101 = Label(materialGrade, text="GR101", font=("arial", 18, "bold"), fg="#384051")
    GR101.grid(row=4, column=0)

    TU170 = Label(materialGrade, text="TU170", font=("arial", 18, "bold"), fg="#384051")
    TU170.grid(row=5, column=0)

    GR131 = Label(materialGrade, text="GR131", font=("arial", 18, "bold"), fg="#384051")
    GR131.grid(row=6, column=0)

    GR111 = Label(materialGrade, text="GR111", font=("arial", 18, "bold"), fg="#384051")
    GR111.grid(row=7, column=0)

    EL118 = Label(materialGrade, text="EL118", font=("arial", 18, "bold"), fg="#384051")
    EL118.grid(row=8, column=0)

    GR121 = Label(materialGrade, text="GR121", font=("arial", 18, "bold"), fg="#384051")
    GR121.grid(row=9, column=0)


    # ******************** Middle Left Frame (Data) **********************
    # ******************** Specialization **********************

    MT131 = Label(materialGrade2, text="MT131", font=("arial", 18, "bold"), fg="#384051")
    MT131.grid(row=0, column=0)

    MT132 = Label(materialGrade2, text="MT132", font=("arial", 18, "bold"), fg="#384051")
    MT132.grid(row=1, column=0)

    TM103 = Label(materialGrade2, text="TM103", font=("arial", 18, "bold"), fg="#384051")
    TM103.grid(row=2, column=0)

    TM105 = Label(materialGrade2, text="TM105", font=("arial", 18, "bold"), fg="#384051")
    TM105.grid(row=3, column=0)

    TM111 = Label(materialGrade2, text="TM111", font=("arial", 18, "bold"), fg="#384051")
    TM111.grid(row=4, column=0)

    TM112 = Label(materialGrade2, text="TM112", font=("arial", 18, "bold"), fg="#384051")
    TM112.grid(row=5, column=0)

    M251 = Label(materialGrade2, text="M251", font=("arial", 18, "bold"), fg="#384051")
    M251.grid(row=6, column=0)

    M269 = Label(materialGrade2, text="M269", font=("arial", 18, "bold"), fg="#384051")
    M269.grid(row=7, column=0)

    T227 = Label(materialGrade2, text="T227", font=("arial", 18, "bold"), fg="#384051")
    T227.grid(row=8, column=0)

    TM240 = Label(materialGrade2, text="TM240", font=("arial", 18, "bold"), fg="#384051")
    TM240.grid(row=9, column=0)

    # ******************** 2 **********************
    # ******************** Middle Left Frame (Data) **********************
    # ******************** Specialization **********************

    MT101 = Label(materialGrade3, text="MT101", font=("arial", 18, "bold"), fg="#384051")
    MT101.grid(row=0, column=0)

    MT129 = Label(materialGrade3, text="MT129", font=("arial", 18, "bold"), fg="#384051")
    MT129.grid(row=1, column=0)

    M109 = Label(materialGrade3, text="M109", font=("arial", 18, "bold"), fg="#384051")
    M109.grid(row=2, column=0)

    MS102 = Label(materialGrade3, text="MS102", font=("arial", 18, "bold"), fg="#384051")
    MS102.grid(row=3, column=0)

    TM298 = Label(materialGrade3, text="TM298", font=("arial", 18, "bold"), fg="#384051")
    TM298.grid(row=4, column=0)

    TM351 = Label(materialGrade3, text="TM351", font=("arial", 18, "bold"), fg="#384051")
    TM351.grid(row=5, column=0)

    TM354 = Label(materialGrade3, text="TM354", font=("arial", 18, "bold"), fg="#384051")
    TM354.grid(row=6, column=0)

    TM366 = Label(materialGrade3, text="TM366", font=("arial", 18, "bold"), fg="#384051")
    TM366.grid(row=7, column=0)

    TM471A = Label(materialGrade3, text="TM471 P.A", font=("arial", 18, "bold"), fg="#384051")
    TM471A.grid(row=8, column=0)

    TM471B = Label(materialGrade3, text="TM471 P.B", font=("arial", 18, "bold"), fg="#384051")
    TM471B.grid(row=9, column=0)


    root2.mainloop()


#*********************** Intro ***********************

root = Tk()
root.geometry("1057x650+100+30")
root.title("Material Details")
root.resizable(False, False)
root.config(bg="black")

#*********************** Top Frame ***********************

titleLabel = Label(root, text="Material Details", font=('arial', 30, 'bold'),
                   fg='white', bg='black', width=45, bd=9, relief=GROOVE)
titleLabel.place(x=0, y=0)

#*********************** Left Frame ***********************


csMaterial = Button(root, text="CS Material", font=("FELIX TITLING", 16, "bold"), command=open, bd=5, relief=GROOVE, bg="#61FFFF", fg="black")
csMaterial.place(x=100, y=300)

planFinish = Button(root, text="CS Plan", font=("FELIX TITLING", 16, "bold"), command=view, bd=5, relief=GROOVE, bg="#61FFFF", fg="black")
planFinish.place(x=310, y=300)

#*********************** Right Frame ***********************

exitButton = Button(root, text="Exit", font=("FELIX TITLING", 16, "bold"), bd=5, relief=GROOVE, bg="#61FFFF", fg="black", command=exit)
exitButton.place(x=880, y=300)


#*********************** Bottom Frame ***********************

materialLabel = Label(root, text="Material Name:", font=("Helvetica", 30, "bold"), bg="black", fg="white")
materialLabel.place(x=145, y=570)

materialText = Entry(root, font=("FELIX TITLING", 20, "bold"), bd=5, relief=GROOVE, justify=CENTER, bg='#D7E9FD')
materialText.place(x=490, y=575)
materialText.focus_set()

searchMaterial = Button(root, text="SEARCH", font=("FELIX TITLING", 20, "bold"), bd=5, relief=GROOVE, command=search, bg="#61FFFF", fg="black")
searchMaterial.place(x=850, y=565)



root.mainloop()
