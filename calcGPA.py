import time
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import random
import pywhatkit as pwt
import requests as requests
import datetime


#******************** Functions *********************

def send():
    if textRight.get(1.0,END) == "\n":
        messagebox.showerror("Error", "Please Fill Your Information In So You Could Send The File")
    else:
        def send_msg():
            now = datetime.datetime.now()
            hour = now.hour
            minute = now.minute
            message = textArea.get(1.0,END)
            number = numField.get()
            pwt.sendwhatmsg(number, message, hour, minute+1)



        root2 = Toplevel()

        root2.title("Send GPA Details")
        root2.config(bg="white")
        root2.geometry('485x620+50+50')

        logoImage = PhotoImage(file="Images/sender.png")
        label = Label(root2, image=logoImage, bg="white")
        label.pack(pady=5)

        numberLabel = Label(root2, text="Mobile Number", font=("arial", 18,"bold underline"),
                             bg="white", fg="black")
        numberLabel.pack(pady=5)
        numField = Entry(root2, font=("helvetica", 22, "bold"), bd=3, width=24)
        numField.pack(pady=5)

        gpaDetails = Label(root2, text="GPA Details", font=("arial", 18, "bold underline"),
                            bg="white", fg="white")
        gpaDetails.pack(pady=5)

        textArea = Text(root2, font=("arial", 12, "bold"), bd=3, width=42, height=14)
        textArea.pack(pady=5)

        sendIT = Button(root2, text="Send", font=("arial", 19, "bold"), bg="#61FFFF",
                        fg="black", bd=7, relief=GROOVE, command=send_msg)
        sendIT.pack(pady=5)

        data_Now = textRight.get(1.0, END)
        textArea.insert(END,data_Now)


        root2.mainloop()

def save():
    if textRight.get(1.0,END) == '\n':
        messagebox.showerror("Error", "Please Fill Your Information In So You Could Save The File")
    else:
        url = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        if url == None:
            pass
        else:
            data_GPA = textRight.get(1.0,END)
            url.write(data_GPA)
            url.close()
            messagebox.showinfo("Information", "The Data Has Been Saved Successfully")

def reset2():
    textRight.delete(1.0,END)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)

    t_AR111.set("0")
    t_AR112.set("0")
    t_EL111.set("0")
    t_EL112.set("0")
    t_GR101.set("0")
    t_TU170.set("0")
    t_GR131.set("0")
    t_GR111.set("0")
    t_EL118.set("0")
    t_GR121.set("0")
    t_MT131.set("0")
    t_MT132.set("0")
    t_TM103.set("0")
    t_TM105.set("0")
    t_TM111.set("0")
    t_TM112.set("0")
    t_M251.set("0")
    t_M269.set("0")
    t_T227.set("0")
    t_TM240.set("0")
    t_MT129.set("0")
    t_M109.set("0")
    t_MS102.set("0")
    t_MT101.set("0")
    t_TM298.set("0")
    t_TM351.set("0")
    t_TM354.set("0")
    t_TM366.set("0")
    t_TM471A.set("0")
    t_TM471B.set("0")

    gpaCalc.set(" ")
    hoursleft.set(" ")

    textAR111.config(state=DISABLED)
    textAR112.config(state=DISABLED)
    textEL111.config(state=DISABLED)
    textEL112.config(state=DISABLED)
    textGR101.config(state=DISABLED)
    textTU170.config(state=DISABLED)
    textGR131.config(state=DISABLED)
    textGR111.config(state=DISABLED)
    textEL118.config(state=DISABLED)
    textGR121.config(state=DISABLED)
    textMT131.config(state=DISABLED)
    textMT132.config(state=DISABLED)
    textTM103.config(state=DISABLED)
    textTM105.config(state=DISABLED)
    textTM111.config(state=DISABLED)
    textTM112.config(state=DISABLED)
    textM251.config(state=DISABLED)
    textM269.config(state=DISABLED)
    textT227.config(state=DISABLED)
    textTM240.config(state=DISABLED)
    textMT101.config(state=DISABLED)
    textMT129.config(state=DISABLED)
    textM109.config(state=DISABLED)
    textMS102.config(state=DISABLED)
    textTM298.config(state=DISABLED)
    textTM351.config(state=DISABLED)
    textTM354.config(state=DISABLED)
    textTM366.config(state=DISABLED)
    textTM471A.config(state=DISABLED)
    textTM471B.config(state=DISABLED)

    nameField.delete(0, END)
    IDField.delete(0, END)
    hoursField.delete(0, END)
    passwordField.delete(0, END)


def exit():
    try:
        root.destroy()
        import register
    except:
        pass

def loading():
    root2 = Tk()
    root2.geometry("400x100+400+250")
    root2.resizable(0, 0)
    root2.title("Loading")
    root2.config(bg="white")

    loadLabel = Label(root2, text="Loading....", font="Bahnschrift 15",
                      bg="white", fg="#FFBD09")
    loadLabel.place(x=153, y=25)

    prog = ttk.Progressbar(root2, orient=HORIZONTAL, length=150, mode='determinate')
    prog.place(x=130, y=60)
    root2.overrideredirect(1)
    prog.start(6)

    root2.after(4000, root2.destroy)

    root2.mainloop()



def AR111():
    if var1.get() == 1:
        textAR111.config(state=NORMAL)
        textAR111.delete(0,END)
    else:
        textAR111.config(state=DISABLED)
        t_AR111.set("0")

def AR112():
    if var2.get() == 1:
       textAR112.config(state=NORMAL)
       textAR112.delete(0, END)
    else:
        textAR112.config(state=DISABLED)
        t_AR112.set("0")

def EL111():
    if var3.get() == 1:
       textEL111.config(state=NORMAL)
       textEL111.delete(0, END)
    else:
        textEL111.config(state=DISABLED)
        t_EL111.set("0")

def EL112():
    if var4.get() == 1:
       textEL112.config(state=NORMAL)
       textEL112.delete(0, END)
    else:
        textEL112.config(state=DISABLED)
        t_EL112.set("0")

def GR101():
    if var5.get() == 1:
       textGR101.config(state=NORMAL)
       textGR101.delete(0, END)
    else:
        textGR101.config(state=DISABLED)
        t_GR101.set("0")

def TU170():
    if var6.get() == 1:
       textTU170.config(state=NORMAL)
       textTU170.delete(0, END)
    else:
        textTU170.config(state=DISABLED)
        t_TU170.set("0")

def GR131():
    if var7.get() == 1:
       textGR131.config(state=NORMAL)
       textGR131.delete(0, END)
    else:
        textGR131.config(state=DISABLED)
        t_GR131.set("0")

def GR111():
    if var8.get() == 1:
       textGR111.config(state=NORMAL)
       textGR111.delete(0, END)
    else:
        textGR111.config(state=DISABLED)
        t_GR111.set("0")

def EL118():
    if var9.get() == 1:
       textEL118.config(state=NORMAL)
       textEL118.delete(0, END)

    else:
        textEL118.config(state=DISABLED)
        t_EL118.set("0")

def GR121():
    if var10.get() == 1:
       textGR121.config(state=NORMAL)
       textGR121.delete(0, END)
    else:
        textGR121.config(state=DISABLED)
        t_GR121.set("0")

def MT131():
    if var11.get() == 1:
       textMT131.config(state=NORMAL)
       textMT131.delete(0, END)
    else:
        textMT131.config(state=DISABLED)
        t_MT131.set("0")

def MT132():
    if var12.get() == 1:
       textMT132.config(state=NORMAL)
       textMT132.delete(0, END)
    else:
        textMT132.config(state=DISABLED)
        t_MT132.set("0")

def TM103():
    if var13.get() == 1:
       textTM103.config(state=NORMAL)
       textTM103.delete(0, END)
    else:
        textTM103.config(state=DISABLED)
        t_TM103.set("0")

def TM105():
    if var14.get() == 1:
       textTM105.config(state=NORMAL)
       textTM105.delete(0, END)
    else:
        textTM105.config(state=DISABLED)
        t_TM105.set("0")

def TM111():
    if var15.get() == 1:
       textTM111.config(state=NORMAL)
       textTM111.delete(0, END)
    else:
        textTM111.config(state=DISABLED)
        t_TM111.set("0")

def TM112():
    if var16.get() == 1:
       textTM112.config(state=NORMAL)
       textTM112.delete(0, END)
    else:
        textTM112.config(state=DISABLED)
        t_TM112.set("0")

def M251():
    if var17.get() == 1:
       textM251.config(state=NORMAL)
       textM251.delete(0, END)
    else:
        textM251.config(state=DISABLED)
        t_M251.set("0")

def M269():
    if var18.get() == 1:
       textM269.config(state=NORMAL)
       textM269.delete(0, END)
    else:
        textM269.config(state=DISABLED)
        t_M269.set("0")

def T227():
    if var19.get() == 1:
       textT227.config(state=NORMAL)
       textT227.delete(0, END)
    else:
        textT227.config(state=DISABLED)
        t_T227.set("0")

def TM240():
    if var20.get() == 1:
       textTM240.config(state=NORMAL)
       textTM240.delete(0, END)
    else:
        textTM240.config(state=DISABLED)
        t_TM240.set("0")

def MT101():
    if var21.get() == 1:
       textMT101.config(state=NORMAL)
       textMT101.delete(0, END)
    else:
        textMT101.config(state=DISABLED)
        t_MT101.set("0")

def MT129():
    if var22.get() == 1:
       textMT129.config(state=NORMAL)
       textMT129.delete(0, END)
    else:
        textMT129.config(state=DISABLED)
        t_MT129.set("0")

def M109():
    if var23.get() == 1:
       textM109.config(state=NORMAL)
       textM109.delete(0, END)
    else:
        textM109.config(state=DISABLED)
        t_M109.set("0")

def MS102():
    if var24.get() == 1:
       textMS102.config(state=NORMAL)
       textMS102.delete(0, END)

    else:
        textMS102.config(state=DISABLED)
        t_MS102.set("0")

def TM298():
    if var25.get() == 1:
       textTM298.config(state=NORMAL)
       textTM298.delete(0, END)

    else:
        textTM298.config(state=DISABLED)
        t_TM298.set("0")

def TM351():
    if var26.get() == 1:
       textTM351.config(state=NORMAL)
       textTM351.delete(0, END)

    else:
        textTM351.config(state=DISABLED)
        t_TM351.set("0")

def TM354():
    if var27.get() == 1:
       textTM354.config(state=NORMAL)
       textTM354.delete(0, END)

    else:
        textTM354.config(state=DISABLED)
        t_TM354.set("0")

def TM366():
    if var28.get() == 1:
       textTM366.config(state=NORMAL)
       textTM366.delete(0, END)

    else:
        textTM366.config(state=DISABLED)
        t_TM366.set("0")

def TM471A():
    if var29.get() == 1:
       textTM471A.config(state=NORMAL)
       textTM471A.delete(0, END)

    else:
        textTM471A.config(state=DISABLED)
        t_TM471A.set("0")

def TM471B():
    if var30.get() == 1:
       textTM471B.config(state=NORMAL)
       textTM471B.delete(0, END)

    else:
        textTM471B.config(state=DISABLED)
        t_TM471B.set("0")


def review():

    if gpaCalc.get() != '' or hoursleft.get() != '':
        textRight.delete(1.0,END)
        ranX = random.randint(100,10000)
        gpaForm = "Request "+str(ranX)

        date = time.strftime("%d/%m/%Y")
        name = nameField.get()
        ID = IDField.get()
        Hours = hoursField.get()
        year = time.strftime("%Y")

        numNow = int(entryHours.get())
        hoursForm = numNow + int(Hours)

        textRight.insert(END, "Details:\t\t"+gpaForm+"\t\t"+date+"\n")
        textRight.insert(END,"Name: "+name+ "\t\tID: "+ str(ID) +"\t\tHours= "+str(numNow)+"\n")
        textRight.insert(END,"---------------------------------------------------------------------------"+"\n")
        textRight.insert(END,"\t          GPA for year "+year+"\n")
        textRight.insert(END, "---------------------------------------------------------------------------" + "\n")
        textRight.insert(END,"Material\t\t"+"Mark\t"+"Grade"+"\n\n")

        if t_AR111.get() != "0":
            if int(t_AR111.get()) >= 90 and int(t_AR111.get()) <= 100:
                textRight.insert(END,f"AR111\t\t{int(t_AR111.get())}\tA\n\n")
            elif int(t_AR111.get()) >= 82 and int(t_AR111.get()) <= 89:
                textRight.insert(END,f"AR111\t\t{int(t_AR111.get())}\tB+\n\n")
            elif int(t_AR111.get()) >= 74 and int(t_AR111.get()) <= 81:
                textRight.insert(END,f"AR111\t\t{int(t_AR111.get())}\tB\n\n")
            elif int(t_AR111.get()) >= 66 and int(t_AR111.get()) <= 73:
                textRight.insert(END,f"AR111\t\t{int(t_AR111.get())}\tC+\n\n")
            elif int(t_AR111.get()) >= 58 and int(t_AR111.get()) <= 65:
                textRight.insert(END,f"AR111\t\t{int(t_AR111.get())}\tC\n\n")
            elif int(t_AR111.get()) >= 50 and int(t_AR111.get()) <= 57:
                textRight.insert(END,f"AR111\t\t{int(t_AR111.get())}\tD\n\n")
            elif int(t_AR111.get()) < 50 and int(t_AR111.get()) != 0:
                textRight.insert(END,f"AR111\t\t{int(t_AR111.get())}\tF\n\n")
            else:
                textRight.insert(END,f"AR111\t\t{int(t_AR111.get())}\n\n")

        # ******************** pass *********************
        if t_AR112.get() != "0":
            if int(t_AR112.get()) >= 90 and int(t_AR112.get()) <= 100:
                textRight.insert(END,f"AR112\t\t{int(t_AR112.get())}\tA\n\n")
            elif int(t_AR112.get()) >= 82 and int(t_AR112.get()) <= 89:
                textRight.insert(END,f"AR112\t\t{int(t_AR112.get())}\tB+\n\n")
            elif int(t_AR112.get()) >= 74 and int(t_AR112.get()) <= 81:
                textRight.insert(END,f"AR112\t\t{int(t_AR112.get())}\tB\n\n")
            elif int(t_AR112.get()) >= 66 and int(t_AR112.get()) <= 73:
                textRight.insert(END,f"AR112\t\t{int(t_AR112.get())}\tC+\n\n")
            elif int(t_AR112.get()) >= 58 and int(t_AR112.get()) <= 65:
                textRight.insert(END,f"AR112\t\t{int(t_AR112.get())}\tC\n\n")
            elif int(t_AR112.get()) >= 50 and int(t_AR112.get()) <= 57:
                textRight.insert(END,f"AR112\t\t{int(t_AR112.get())}\tD\n\n")
            elif int(t_AR112.get()) < 50 and int(t_AR112.get()) != 0:
                textRight.insert(END,f"AR112\t\t{int(t_AR112.get())}\tF\n\n")
            else:
                textRight.insert(END,f"AR112\t\t{int(t_AR112.get())}\n\n")
    # ******************** pass *********************
        if t_EL111.get() != "0":
            if int(t_EL111.get()) >= 90 and int(t_EL111.get()) <= 100:
                textRight.insert(END,f"EL111\t\t{int(t_EL111.get())}\tA\n\n")
            elif int(t_EL111.get()) >= 82 and int(t_EL111.get()) <= 89:
                textRight.insert(END,f"EL111\t\t{int(t_EL111.get())}\tB+\n\n")
            elif int(t_EL111.get()) >= 74 and int(t_EL111.get()) <= 81:
                textRight.insert(END,f"EL111\t\t{int(t_EL111.get())}\tB\n\n")
            elif int(t_EL111.get()) >= 66 and int(t_EL111.get()) <= 73:
                textRight.insert(END,f"EL111\t\t{int(t_EL111.get())}\tC+\n\n")
            elif int(t_EL111.get()) >= 58 and int(t_EL111.get()) <= 65:
                textRight.insert(END,f"EL111\t\t{int(t_EL111.get())}\tC\n\n")
            elif int(t_EL111.get()) >= 50 and int(t_EL111.get()) <= 57:
                textRight.insert(END,f"EL111\t\t{int(t_EL111.get())}\tD\n\n")
            elif int(t_EL111.get()) < 50 and int(t_EL111.get()) != 0:
                textRight.insert(END,f"EL111\t\t{int(t_EL111.get())}\tF\n\n")
            else:
                textRight.insert(END,f"EL111\t\t{int(t_EL111.get())}\n\n")

    # ******************** pass *********************
        if t_EL112.get() != "0":
            if int(t_EL112.get()) >= 90 and int(t_EL112.get()) <= 100:
                textRight.insert(END,f"EL112\t\t{int(t_EL112.get())}\tA\n\n")
            elif int(t_EL112.get()) >= 82 and int(t_EL112.get()) <= 89:
                textRight.insert(END,f"EL112\t\t{int(t_EL112.get())}\tB+\n\n")
            elif int(t_EL112.get()) >= 74 and int(t_EL112.get()) <= 81:
                textRight.insert(END,f"EL112\t\t{int(t_EL112.get())}\tB\n\n")
            elif int(t_EL112.get()) >= 66 and int(t_EL112.get()) <= 73:
                textRight.insert(END,f"EL112\t\t{int(t_EL112.get())}\tC+\n\n")
            elif int(t_EL112.get()) >= 58 and int(t_EL112.get()) <= 65:
                textRight.insert(END,f"EL112\t\t{int(t_EL112.get())}\tC\n\n")
            elif int(t_EL112.get()) >= 50 and int(t_EL112.get()) <= 57:
                textRight.insert(END,f"EL112\t\t{int(t_EL112.get())}\tD\n\n")
            elif int(t_EL112.get()) < 50 and int(t_EL112.get()) != 0:
                textRight.insert(END,f"EL112\t\t{int(t_EL112.get())}\tF\n\n")
            else:
                textRight.insert(END,f"EL112\t\t{int(t_EL112.get())}\n\n")

    # ******************** pass *********************
        if t_GR101.get() != "0":
            if int(t_GR101.get()) >= 90 and int(t_GR101.get()) <= 100:
                textRight.insert(END,f"GR101\t\t{int(t_GR101.get())}\tA\n\n")
            elif int(t_GR101.get()) >= 82 and int(t_GR101.get()) <= 89:
                textRight.insert(END,f"GR101\t\t{int(t_GR101.get())}\tB+\n\n")
            elif int(t_GR101.get()) >= 74 and int(t_GR101.get()) <= 81:
                textRight.insert(END,f"GR101\t\t{int(t_GR101.get())}\tB\n\n")
            elif int(t_GR101.get()) >= 66 and int(t_GR101.get()) <= 73:
                textRight.insert(END,f"GR101\t\t{int(t_GR101.get())}\tC+\n\n")
            elif int(t_GR101.get()) >= 58 and int(t_GR101.get()) <= 65:
                textRight.insert(END,f"GR101\t\t{int(t_GR101.get())}\tC\n\n")
            elif int(t_GR101.get()) >= 50 and int(t_GR101.get()) <= 57:
                textRight.insert(END,f"GR101\t\t{int(t_GR101.get())}\tD\n\n")
            elif int(t_GR101.get()) < 50 and int(t_GR101.get()) != 0:
                textRight.insert(END,f"GR101\t\t{int(t_GR101.get())}\tF\n\n")
            else:
                textRight.insert(END,f"GR101\t\t{int(t_GR101.get())}\n\n")

    # ******************** pass *********************
        if t_TU170.get() != "0":
            if int(t_TU170.get()) >= 90 and int(t_TU170.get()) <= 100:
                textRight.insert(END,f"TU170\t\t{int(t_TU170.get())}\tA\n\n")
            elif int(t_TU170.get()) >= 82 and int(t_TU170.get()) <= 89:
                textRight.insert(END,f"TU170\t\t{int(t_TU170.get())}\tB+\n\n")
            elif int(t_TU170.get()) >= 74 and int(t_TU170.get()) <= 81:
                textRight.insert(END,f"TU170\t\t{int(t_TU170.get())}\tB\n\n")
            elif int(t_TU170.get()) >= 66 and int(t_TU170.get()) <= 73:
                textRight.insert(END,f"TU170\t\t{int(t_TU170.get())}\tC+\n\n")
            elif int(t_TU170.get()) >= 58 and int(t_TU170.get()) <= 65:
                textRight.insert(END,f"TU170\t\t{int(t_TU170.get())}\tC\n\n")
            elif int(t_TU170.get()) >= 50 and int(t_TU170.get()) <= 57:
                textRight.insert(END,f"TU170\t\t{int(t_TU170.get())}\tD\n\n")
            elif int(t_TU170.get()) < 50 and int(t_TU170.get()) != 0:
                textRight.insert(END,f"TU170\t\t{int(t_TU170.get())}\tF\n\n")
            else:
                textRight.insert(END,f"TU170\t\t{int(t_TU170.get())}\n\n")

    # ******************** pass *********************
        if t_GR131.get() != "0":
            if int(t_GR131.get()) >= 90 and int(t_GR131.get()) <= 100:
                textRight.insert(END,f"GR131\t\t{int(t_GR131.get())}\tA\n\n")
            elif int(t_GR131.get()) >= 82 and int(t_GR131.get()) <= 89:
                textRight.insert(END,f"GR131\t\t{int(t_GR131.get())}\tB+\n\n")
            elif int(t_GR131.get()) >= 74 and int(t_GR131.get()) <= 81:
                textRight.insert(END,f"GR131\t\t{int(t_GR131.get())}\tB\n\n")
            elif int(t_GR131.get()) >= 66 and int(t_GR131.get()) <= 73:
                textRight.insert(END,f"GR131\t\t{int(t_GR131.get())}\tC+\n\n")
            elif int(t_GR131.get()) >= 58 and int(t_GR131.get()) <= 65:
                textRight.insert(END,f"GR131\t\t{int(t_GR131.get())}\tC\n\n")
            elif int(t_GR131.get()) >= 50 and int(t_GR131.get()) <= 57:
                textRight.insert(END,f"GR131\t\t{int(t_GR131.get())}\tD\n\n")
            elif int(t_GR131.get()) < 50 and int(t_GR131.get()) != 0:
                textRight.insert(END,f"GR131\t\t{int(t_GR131.get())}\tF\n\n")
            else:
                textRight.insert(END,f"GR131\t\t{int(t_GR131.get())}\n\n")

    # ******************** pass *********************
        if t_GR111.get() != "0":
            if int(t_GR111.get()) >= 90 and int(t_GR111.get()) <= 100:
                textRight.insert(END,f"GR111\t\t{int(t_GR111.get())}\tA\n\n")
            elif int(t_GR111.get()) >= 82 and int(t_GR111.get()) <= 89:
                textRight.insert(END,f"GR111\t\t{int(t_GR111.get())}\tB+\n\n")
            elif int(t_GR111.get()) >= 74 and int(t_GR111.get()) <= 81:
                textRight.insert(END,f"GR111\t\t{int(t_GR111.get())}\tB\n\n")
            elif int(t_GR111.get()) >= 66 and int(t_GR111.get()) <= 73:
                textRight.insert(END,f"GR111\t\t{int(t_GR111.get())}\tC+\n\n")
            elif int(t_GR111.get()) >= 58 and int(t_GR111.get()) <= 65:
                textRight.insert(END,f"GR111\t\t{int(t_GR111.get())}\tC\n\n")
            elif int(t_GR111.get()) >= 50 and int(t_GR111.get()) <= 57:
                textRight.insert(END,f"GR111\t\t{int(t_GR111.get())}\tD\n\n")
            elif int(t_GR111.get()) < 50 and int(t_GR111.get()) != 0:
                textRight.insert(END,f"GR111\t\t{int(t_GR111.get())}\tF\n\n")
            else:
                textRight.insert(END,f"GR111\t\t{int(t_GR111.get())}\n\n")

    # ******************** pass *********************
        if t_EL118.get() != "0":
            if int(t_EL118.get()) >= 90 and int(t_EL118.get()) <= 100:
                textRight.insert(END,f"EL118\t\t{int(t_EL118.get())}\tA\n\n")
            elif int(t_EL118.get()) >= 82 and int(t_EL118.get()) <= 89:
                textRight.insert(END,f"EL118\t\t{int(t_EL118.get())}\tB+\n\n")
            elif int(t_EL118.get()) >= 74 and int(t_EL118.get()) <= 81:
                textRight.insert(END,f"EL118\t\t{int(t_EL118.get())}\tB\n\n")
            elif int(t_EL118.get()) >= 66 and int(t_EL118.get()) <= 73:
                textRight.insert(END,f"EL118\t\t{int(t_EL118.get())}\tC+\n\n")
            elif int(t_EL118.get()) >= 58 and int(t_EL118.get()) <= 65:
                textRight.insert(END,f"EL118\t\t{int(t_EL118.get())}\tC\n\n")
            elif int(t_EL118.get()) >= 50 and int(t_EL118.get()) <= 57:
                textRight.insert(END,f"EL118\t\t{int(t_EL118.get())}\tD\n\n")
            elif int(t_EL118.get()) < 50 and int(t_EL118.get()) != 0:
                textRight.insert(END,f"EL118\t\t{int(t_EL118.get())}\tF\n\n")
            else:
                textRight.insert(END,f"EL118\t\t{int(t_EL118.get())}\n\n")

    # ******************** pass *********************
        if t_GR121.get() != "0":
            if int(t_GR121.get()) >= 90 and int(t_GR121.get()) <= 100:
                textRight.insert(END,f"GR121\t\t{int(t_GR121.get())}\tA\n\n")
            elif int(t_GR121.get()) >= 82 and int(t_GR121.get()) <= 89:
                textRight.insert(END,f"GR121\t\t{int(t_GR121.get())}\tB+\n\n")
            elif int(t_GR121.get()) >= 74 and int(t_GR121.get()) <= 81:
                textRight.insert(END,f"GR121\t\t{int(t_GR121.get())}\tB\n\n")
            elif int(t_GR121.get()) >= 66 and int(t_GR121.get()) <= 73:
                textRight.insert(END,f"GR121\t\t{int(t_GR121.get())}\tC+\n\n")
            elif int(t_GR121.get()) >= 58 and int(t_GR121.get()) <= 65:
                textRight.insert(END,f"GR121\t\t{int(t_GR121.get())}\tC\n\n")
            elif int(t_GR121.get()) >= 50 and int(t_GR121.get()) <= 57:
                textRight.insert(END,f"GR121\t\t{int(t_GR121.get())}\tD\n\n")
            elif int(t_GR121.get()) < 50 and int(t_GR121.get()) != 0:
                textRight.insert(END,f"GR121\t\t{int(t_GR121.get())}\tF\n\n")
            else:
                textRight.insert(END,f"GR121\t\t{int(t_GR121.get())}\n\n")

    # ******************** pass *********************
        if t_MT131.get() != "0":
            if int(t_MT131.get()) >= 90 and int(t_MT131.get()) <= 100:
                textRight.insert(END,f"MT131\t\t{int(t_MT131.get())}\tA\n\n")
            elif int(t_MT131.get()) >= 82 and int(t_MT131.get()) <= 89:
                textRight.insert(END,f"MT131\t\t{int(t_MT131.get())}\tB+\n\n")
            elif int(t_MT131.get()) >= 74 and int(t_MT131.get()) <= 81:
                textRight.insert(END,f"MT131\t\t{int(t_MT131.get())}\tB\n\n")
            elif int(t_MT131.get()) >= 66 and int(t_MT131.get()) <= 73:
                textRight.insert(END,f"MT131\t\t{int(t_MT131.get())}\tC+\n\n")
            elif int(t_MT131.get()) >= 58 and int(t_MT131.get()) <= 65:
                textRight.insert(END,f"MT131\t\t{int(t_MT131.get())}\tC\n\n")
            elif int(t_MT131.get()) >= 50 and int(t_MT131.get()) <= 57:
                textRight.insert(END,f"MT131\t\t{int(t_MT131.get())}\tD\n\n")
            elif int(t_MT131.get()) < 50 and int(t_MT131.get()) != 0:
                textRight.insert(END,f"MT131\t\t{int(t_MT131.get())}\tF\n\n")
            else:
                textRight.insert(END,f"MT131\t\t{int(t_MT131.get())}\n\n")

    # ******************** pass *********************
        if t_MT132.get() != "0":
            if int(t_MT132.get()) >= 90 and int(t_MT132.get()) <= 100:
                textRight.insert(END,f"MT132\t\t{int(t_MT132.get())}\tA\n\n")
            elif int(t_MT132.get()) >= 82 and int(t_MT132.get()) <= 89:
                textRight.insert(END,f"MT132\t\t{int(t_MT132.get())}\tB+\n\n")
            elif int(t_MT132.get()) >= 74 and int(t_MT132.get()) <= 81:
                textRight.insert(END,f"MT132\t\t{int(t_MT132.get())}\tB\n\n")
            elif int(t_MT132.get()) >= 66 and int(t_MT132.get()) <= 73:
                textRight.insert(END,f"MT132\t\t{int(t_MT132.get())}\tC+\n\n")
            elif int(t_MT132.get()) >= 58 and int(t_MT132.get()) <= 65:
                textRight.insert(END,f"MT132\t\t{int(t_MT132.get())}\tC\n\n")
            elif int(t_MT132.get()) >= 50 and int(t_MT132.get()) <= 57:
                textRight.insert(END,f"MT132\t\t{int(t_MT132.get())}\tD\n\n")
            elif int(t_MT132.get()) < 50 and int(t_MT132.get()) != 0:
                textRight.insert(END,f"MT132\t\t{int(t_MT132.get())}\tF\n\n")
            else:
                textRight.insert(END,f"MT132\t\t{int(t_MT132.get())}\n\n")

    # ******************** pass *********************
        if t_TM103.get() != "0":
            if int(t_TM103.get()) >= 90 and int(t_TM103.get()) <= 100:
                textRight.insert(END,f"TM103\t\t{int(t_TM103.get())}\tA\n\n")
            elif int(t_TM103.get()) >= 82 and int(t_TM103.get()) <= 89:
                textRight.insert(END,f"TM103\t\t{int(t_TM103.get())}\tB+\n\n")
            elif int(t_TM103.get()) >= 74 and int(t_TM103.get()) <= 81:
                textRight.insert(END,f"TM103\t\t{int(t_TM103.get())}\tB\n\n")
            elif int(t_TM103.get()) >= 66 and int(t_TM103.get()) <= 73:
                textRight.insert(END,f"TM103\t\t{int(t_TM103.get())}\tC+\n\n")
            elif int(t_TM103.get()) >= 58 and int(t_TM103.get()) <= 65:
                textRight.insert(END,f"TM103\t\t{int(t_TM103.get())}\tC\n\n")
            elif int(t_TM103.get()) >= 50 and int(t_TM103.get()) <= 57:
                textRight.insert(END,f"TM103\t\t{int(t_TM103.get())}\tD\n\n")
            elif int(t_TM103.get()) < 50 and int(t_TM103.get()) != 0:
                textRight.insert(END,f"TM103\t\t{int(t_TM103.get())}\tF\n\n")
            else:
                textRight.insert(END,f"TM103\t\t{int(t_TM103.get())}\n\n")

    # ******************** pass *********************
        if t_TM105.get() != "0":
            if int(t_TM105.get()) >= 90 and int(t_TM105.get()) <= 100:
                textRight.insert(END,f"TM105\t\t{int(t_TM105.get())}\tA\n\n")
            elif int(t_TM105.get()) >= 82 and int(t_TM105.get()) <= 89:
                textRight.insert(END,f"TM105\t\t{int(t_TM105.get())}\tB+\n\n")
            elif int(t_TM105.get()) >= 74 and int(t_TM105.get()) <= 81:
                textRight.insert(END,f"TM105\t\t{int(t_TM105.get())}\tB\n\n")
            elif int(t_TM105.get()) >= 66 and int(t_TM105.get()) <= 73:
                textRight.insert(END,f"TM105\t\t{int(t_TM105.get())}\tC+\n\n")
            elif int(t_TM105.get()) >= 58 and int(t_TM105.get()) <= 65:
                textRight.insert(END,f"TM105\t\t{int(t_TM105.get())}\tC\n\n")
            elif int(t_TM105.get()) >= 50 and int(t_TM105.get()) <= 57:
                textRight.insert(END,f"TM105\t\t{int(t_TM105.get())}\tD\n\n")
            elif int(t_TM105.get()) < 50 and int(t_TM105.get()) != 0:
                textRight.insert(END,f"TM105\t\t{int(t_TM105.get())}\tF\n\n")
            else:
                textRight.insert(END,f"TM105\t\t{int(t_TM105.get())}\n\n")


    # ******************** pass *********************
        if t_TM111.get() != "0":
            if int(t_TM111.get()) >= 90 and int(t_TM111.get()) <= 100:
                textRight.insert(END,f"TM111\t\t{int(t_TM111.get())}\tA\n\n")
            elif int(t_TM111.get()) >= 82 and int(t_TM111.get()) <= 89:
                textRight.insert(END,f"TM111\t\t{int(t_TM111.get())}\tB+\n\n")
            elif int(t_TM111.get()) >= 74 and int(t_TM111.get()) <= 81:
                textRight.insert(END,f"TM111\t\t{int(t_TM111.get())}\tB\n\n")
            elif int(t_TM111.get()) >= 66 and int(t_TM111.get()) <= 73:
                textRight.insert(END,f"TM111\t\t{int(t_TM111.get())}\tC+\n\n")
            elif int(t_TM111.get()) >= 58 and int(t_TM111.get()) <= 65:
                textRight.insert(END,f"TM111\t\t{int(t_TM111.get())}\tC\n\n")
            elif int(t_TM111.get()) >= 50 and int(t_TM111.get()) <= 57:
                textRight.insert(END,f"TM111\t\t{int(t_TM111.get())}\tD\n\n")
            elif int(t_TM111.get()) < 50 and int(t_TM111.get()) != 0:
                textRight.insert(END,f"TM111\t\t{int(t_TM111.get())}\tF\n\n")
            else:
                textRight.insert(END,f"TM111\t\t{int(t_TM111.get())}\n\n")

    # ******************** pass *********************
        if t_TM112.get() != "0":
            if int(t_TM112.get()) >= 90 and int(t_TM112.get()) <= 100:
                textRight.insert(END,f"TM112\t\t{int(t_TM112.get())}\tA\n\n")
            elif int(t_TM112.get()) >= 82 and int(t_TM112.get()) <= 89:
                textRight.insert(END,f"TM112\t\t{int(t_TM112.get())}\tB+\n\n")
            elif int(t_TM112.get()) >= 74 and int(t_TM112.get()) <= 81:
                textRight.insert(END,f"TM112\t\t{int(t_TM112.get())}\tB\n\n")
            elif int(t_TM112.get()) >= 66 and int(t_TM112.get()) <= 73:
                textRight.insert(END,f"TM112\t\t{int(t_TM112.get())}\tC+\n\n")
            elif int(t_TM112.get()) >= 58 and int(t_TM112.get()) <= 65:
                textRight.insert(END,f"TM112\t\t{int(t_TM112.get())}\tC\n\n")
            elif int(t_TM112.get()) >= 50 and int(t_TM112.get()) <= 57:
                textRight.insert(END,f"TM112\t\t{int(t_TM112.get())}\tD\n\n")
            elif int(t_TM112.get()) < 50 and int(t_TM112.get()) != 0:
                textRight.insert(END,f"TM112\t\t{int(t_TM112.get())}\tF\n\n")
            else:
                textRight.insert(END,f"TM112\t\t{int(t_TM112.get())}\n\n")


    # ******************** pass *********************
        if t_M251.get() != "0":
            if int(t_M251.get()) >= 90 and int(t_M251.get()) <= 100:
                textRight.insert(END,f"M251\t\t{int(t_M251.get())}\tA\n\n")
            elif int(t_M251.get()) >= 82 and int(t_M251.get()) <= 89:
                textRight.insert(END,f"M251\t\t{int(t_M251.get())}\tB+\n\n")
            elif int(t_M251.get()) >= 74 and int(t_M251.get()) <= 81:
                textRight.insert(END,f"M251\t\t{int(t_M251.get())}\tB\n\n")
            elif int(t_M251.get()) >= 66 and int(t_M251.get()) <= 73:
                textRight.insert(END,f"M251\t\t{int(t_M251.get())}\tC+\n\n")
            elif int(t_M251.get()) >= 58 and int(t_M251.get()) <= 65:
                textRight.insert(END,f"M251\t\t{int(t_M251.get())}\tC\n\n")
            elif int(t_M251.get()) >= 50 and int(t_M251.get()) <= 57:
                textRight.insert(END,f"M251\t\t{int(t_M251.get())}\tD\n\n")
            elif int(t_M251.get()) < 50 and int(t_M251.get()) != 0:
                textRight.insert(END,f"M251\t\t{int(t_M251.get())}\tF\n\n")
            else:
                textRight.insert(END,f"M251\t\t{int(t_M251.get())}\n\n")


    # ******************** pass *********************
        if t_M269.get() != "0":
            if int(t_M269.get()) >= 90 and int(t_M269.get()) <= 100:
                textRight.insert(END,f"M269\t\t{int(t_M269.get())}\tA\n\n")
            elif int(t_M269.get()) >= 82 and int(t_M269.get()) <= 89:
                textRight.insert(END,f"M269\t\t{int(t_M269.get())}\tB+\n\n")
            elif int(t_M269.get()) >= 74 and int(t_M269.get()) <= 81:
                textRight.insert(END,f"M269\t\t{int(t_M269.get())}\tB\n\n")
            elif int(t_M269.get()) >= 66 and int(t_M269.get()) <= 73:
                textRight.insert(END,f"M269\t\t{int(t_M269.get())}\tC+\n\n")
            elif int(t_M269.get()) >= 58 and int(t_M269.get()) <= 65:
                textRight.insert(END,f"M269\t\t{int(t_M269.get())}\tC\n\n")
            elif int(t_M269.get()) >= 50 and int(t_M269.get()) <= 57:
                textRight.insert(END,f"M269\t\t{int(t_M269.get())}\tD\n\n")
            elif int(t_M269.get()) < 50 and int(t_M269.get()) != 0:
                textRight.insert(END,f"M269\t\t{int(t_M269.get())}\tF\n\n")
            else:
                textRight.insert(END,f"M269\t\t{int(t_M269.get())}\n\n")

    # ******************** pass *********************
        if t_T227.get() != "0":
            if int(t_T227.get()) >= 90 and int(t_T227.get()) <= 100:
                textRight.insert(END,f"T227\t\t{int(t_T227.get())}\tA\n\n")
            elif int(t_T227.get()) >= 82 and int(t_T227.get()) <= 89:
                textRight.insert(END,f"T227\t\t{int(t_T227.get())}\tB+\n\n")
            elif int(t_T227.get()) >= 74 and int(t_T227.get()) <= 81:
                textRight.insert(END,f"T227\t\t{int(t_T227.get())}\tB\n\n")
            elif int(t_T227.get()) >= 66 and int(t_T227.get()) <= 73:
                textRight.insert(END,f"T227\t\t{int(t_T227.get())}\tC+\n\n")
            elif int(t_T227.get()) >= 58 and int(t_T227.get()) <= 65:
                textRight.insert(END,f"T227\t\t{int(t_T227.get())}\tC\n\n")
            elif int(t_T227.get()) >= 50 and int(t_T227.get()) <= 57:
                textRight.insert(END,f"T227\t\t{int(t_T227.get())}\tD\n\n")
            elif int(t_T227.get()) < 50 and int(t_T227.get()) != 0:
                textRight.insert(END,f"T227\t\t{int(t_T227.get())}\tF\n\n")
            else:
                textRight.insert(END,f"T227\t\t{int(t_T227.get())}\n\n")

    # ******************** pass *********************
        if t_TM240.get() != "0":
            if int(t_TM240.get()) >= 90 and int(t_TM240.get()) <= 100:
                textRight.insert(END,f"TM240\t\t{int(t_TM240.get())}\tA\n\n")
            elif int(t_TM240.get()) >= 82 and int(t_TM240.get()) <= 89:
                textRight.insert(END,f"TM240\t\t{int(t_TM240.get())}\tB+\n\n")
            elif int(t_TM240.get()) >= 74 and int(t_TM240.get()) <= 81:
                textRight.insert(END,f"TM240\t\t{int(t_TM240.get())}\tB\n\n")
            elif int(t_TM240.get()) >= 66 and int(t_TM240.get()) <= 73:
                textRight.insert(END,f"TM240\t\t{int(t_TM240.get())}\tC+\n\n")
            elif int(t_TM240.get()) >= 58 and int(t_TM240.get()) <= 65:
                textRight.insert(END,f"TM240\t\t{int(t_TM240.get())}\tC\n\n")
            elif int(t_TM240.get()) >= 50 and int(t_TM240.get()) <= 57:
                textRight.insert(END,f"TM240\t\t{int(t_TM240.get())}\tD\n\n")
            elif int(t_TM240.get()) < 50 and int(t_TM240.get()) != 0:
                textRight.insert(END,f"TM240\t\t{int(t_TM240.get())}\tF\n\n")
            else:
                textRight.insert(END,f"TM240\t\t{int(t_TM240.get())}\n\n")


    # ******************** pass *********************
        if t_MT101.get() != "0":
            if int(t_MT101.get()) >= 90 and int(t_MT101.get()) <= 100:
                textRight.insert(END,f"MT101\t\t{int(t_MT101.get())}\tA\n\n")
            elif int(t_MT101.get()) >= 82 and int(t_MT101.get()) <= 89:
                textRight.insert(END,f"MT101\t\t{int(t_MT101.get())}\tB+\n\n")
            elif int(t_MT101.get()) >= 74 and int(t_MT101.get()) <= 81:
                textRight.insert(END,f"MT101\t\t{int(t_MT101.get())}\tB\n\n")
            elif int(t_MT101.get()) >= 66 and int(t_MT101.get()) <= 73:
                textRight.insert(END,f"MT101\t\t{int(t_MT101.get())}\tC+\n\n")
            elif int(t_MT101.get()) >= 58 and int(t_MT101.get()) <= 65:
                textRight.insert(END,f"MT101\t\t{int(t_MT101.get())}\tC\n\n")
            elif int(t_MT101.get()) >= 50 and int(t_MT101.get()) <= 57:
                textRight.insert(END,f"MT101\t\t{int(t_MT101.get())}\tD\n\n")
            elif int(t_MT101.get()) < 50 and int(t_MT101.get()) != 0:
                textRight.insert(END,f"MT101\t\t{int(t_MT101.get())}\tF\n\n")
            else:
                textRight.insert(END,f"MT101\t\t{int(t_MT101.get())}\n\n")


    # ******************** pass *********************
        if t_MT129.get() != "0":
            if int(t_MT129.get()) >= 90 and int(t_MT129.get()) <= 100:
                textRight.insert(END,f"MT129\t\t{int(t_MT129.get())}\tA\n\n")
            elif int(t_MT129.get()) >= 82 and int(t_MT129.get()) <= 89:
                textRight.insert(END,f"MT129\t\t{int(t_MT129.get())}\tB+\n\n")
            elif int(t_MT129.get()) >= 74 and int(t_MT129.get()) <= 81:
                textRight.insert(END,f"MT129\t\t{int(t_MT129.get())}\tB\n\n")
            elif int(t_MT129.get()) >= 66 and int(t_MT129.get()) <= 73:
                textRight.insert(END,f"MT129\t\t{int(t_MT129.get())}\tC+\n\n")
            elif int(t_MT129.get()) >= 58 and int(t_MT129.get()) <= 65:
                textRight.insert(END,f"MT129\t\t{int(t_MT129.get())}\tC\n\n")
            elif int(t_MT129.get()) >= 50 and int(t_MT129.get()) <= 57:
                textRight.insert(END,f"MT129\t\t{int(t_MT129.get())}\tD\n\n")
            elif int(t_MT129.get()) < 50 and int(t_MT129.get()) != 0:
                textRight.insert(END,f"MT129\t\t{int(t_MT129.get())}\tF\n\n")
            else:
                textRight.insert(END,f"MT129\t\t{int(t_MT129.get())}\n\n")


    # ******************** pass *********************
        if t_M109.get() != "0":
            if int(t_M109.get()) >= 90 and int(t_M109.get()) <= 100:
                textRight.insert(END,f"M109\t\t{int(t_M109.get())}\tA\n\n")
            elif int(t_M109.get()) >= 82 and int(t_M109.get()) <= 89:
                textRight.insert(END,f"M109\t\t{int(t_M109.get())}\tB+\n\n")
            elif int(t_M109.get()) >= 74 and int(t_M109.get()) <= 81:
                textRight.insert(END,f"M109\t\t{int(t_M109.get())}\tB\n\n")
            elif int(t_M109.get()) >= 66 and int(t_M109.get()) <= 73:
                textRight.insert(END,f"M109\t\t{int(t_M109.get())}\tC+\n\n")
            elif int(t_M109.get()) >= 58 and int(t_M109.get()) <= 65:
                textRight.insert(END,f"M109\t\t{int(t_M109.get())}\tC\n\n")
            elif int(t_M109.get()) >= 50 and int(t_M109.get()) <= 57:
                textRight.insert(END,f"M109\t\t{int(t_M109.get())}\tD\n\n")
            elif int(t_M109.get()) < 50 and int(t_M109.get()) != 0:
                textRight.insert(END,f"M109\t\t{int(t_M109.get())}\tF\n\n")
            else:
                textRight.insert(END,f"M109\t\t{int(t_M109.get())}\n\n")


    # ******************** pass *********************
        if t_MS102.get() != "0":
            if int(t_MS102.get()) >= 90 and int(t_MS102.get()) <= 100:
                textRight.insert(END,f"MS102\t\t{int(t_MS102.get())}\tA\n\n")
            elif int(t_MS102.get()) >= 82 and int(t_MS102.get()) <= 89:
                textRight.insert(END,f"MS102\t\t{int(t_MS102.get())}\tB+\n\n")
            elif int(t_MS102.get()) >= 74 and int(t_MS102.get()) <= 81:
                textRight.insert(END,f"MS102\t\t{int(t_MS102.get())}\tB\n\n")
            elif int(t_MS102.get()) >= 66 and int(t_MS102.get()) <= 73:
                textRight.insert(END,f"MS102\t\t{int(t_MS102.get())}\tC+\n\n")
            elif int(t_MS102.get()) >= 58 and int(t_MS102.get()) <= 65:
                textRight.insert(END,f"MS102\t\t{int(t_MS102.get())}\tC\n\n")
            elif int(t_MS102.get()) >= 50 and int(t_MS102.get()) <= 57:
                textRight.insert(END,f"MS102\t\t{int(t_MS102.get())}\tD\n\n")
            elif int(t_MS102.get()) < 50 and int(t_MS102.get()) != 0:
                textRight.insert(END,f"MS102\t\t{int(t_MS102.get())}\tF\n\n")
            else:
                textRight.insert(END,f"MS102\t\t{int(t_MS102.get())}\n\n")


    # ******************** pass *********************
        if t_TM298.get() != "0":
            if int(t_TM298.get()) >= 90 and int(t_TM298.get()) <= 100:
                textRight.insert(END,f"TM298\t\t{int(t_TM298.get())}\tA\n\n")
            elif int(t_TM298.get()) >= 82 and int(t_TM298.get()) <= 89:
                textRight.insert(END,f"TM298\t\t{int(t_TM298.get())}\tB+\n\n")
            elif int(t_TM298.get()) >= 74 and int(t_TM298.get()) <= 81:
                textRight.insert(END,f"TM298\t\t{int(t_TM298.get())}\tB\n\n")
            elif int(t_TM298.get()) >= 66 and int(t_TM298.get()) <= 73:
                textRight.insert(END,f"TM298\t\t{int(t_TM298.get())}\tC+\n\n")
            elif int(t_TM298.get()) >= 58 and int(t_TM298.get()) <= 65:
                textRight.insert(END,f"TM298\t\t{int(t_TM298.get())}\tC\n\n")
            elif int(t_TM298.get()) >= 50 and int(t_TM298.get()) <= 57:
                textRight.insert(END,f"TM298\t\t{int(t_TM298.get())}\tD\n\n")
            elif int(t_TM298.get()) < 50 and int(t_TM298.get()) != 0:
                textRight.insert(END,f"TM298\t\t{int(t_TM298.get())}\tF\n\n")
            else:
                textRight.insert(END,f"TM298\t\t{int(t_TM298.get())}\n\n")


    # ******************** pass *********************
        if t_TM351.get() != "0":
            if int(t_TM351.get()) >= 90 and int(t_TM351.get()) <= 100:
                textRight.insert(END,f"TM351\t\t{int(t_TM351.get())}\tA\n\n")
            elif int(t_TM351.get()) >= 82 and int(t_TM351.get()) <= 89:
                textRight.insert(END,f"TM351\t\t{int(t_TM351.get())}\tB+\n\n")
            elif int(t_TM351.get()) >= 74 and int(t_TM351.get()) <= 81:
                textRight.insert(END,f"TM351\t\t{int(t_TM351.get())}\tB\n\n")
            elif int(t_TM351.get()) >= 66 and int(t_TM351.get()) <= 73:
                textRight.insert(END,f"TM351\t\t{int(t_TM351.get())}\tC+\n\n")
            elif int(t_TM351.get()) >= 58 and int(t_TM351.get()) <= 65:
                textRight.insert(END,f"TM351\t\t{int(t_TM351.get())}\tC\n\n")
            elif int(t_TM351.get()) >= 50 and int(t_TM351.get()) <= 57:
                textRight.insert(END,f"TM351\t\t{int(t_TM351.get())}\tD\n\n")
            elif int(t_TM351.get()) < 50 and int(t_TM351.get()) != 0:
                textRight.insert(END,f"TM351\t\t{int(t_TM351.get())}\tF\n\n")
            else:
                textRight.insert(END,f"TM351\t\t{int(t_TM351.get())}\n\n")

    # ******************** pass *********************
        if t_TM354.get() != "0":
            if int(t_TM354.get()) >= 90 and int(t_TM354.get()) <= 100:
                textRight.insert(END,f"TM354\t\t{int(t_TM354.get())}\tA\n\n")
            elif int(t_TM354.get()) >= 82 and int(t_TM354.get()) <= 89:
                textRight.insert(END,f"TM354\t\t{int(t_TM354.get())}\tB+\n\n")
            elif int(t_TM354.get()) >= 74 and int(t_TM354.get()) <= 81:
                textRight.insert(END,f"TM354\t\t{int(t_TM354.get())}\tB\n\n")
            elif int(t_TM354.get()) >= 66 and int(t_TM354.get()) <= 73:
                textRight.insert(END,f"TM354\t\t{int(t_TM354.get())}\tC+\n\n")
            elif int(t_TM354.get()) >= 58 and int(t_TM354.get()) <= 65:
                textRight.insert(END,f"TM354\t\t{int(t_TM354.get())}\tC\n\n")
            elif int(t_TM354.get()) >= 50 and int(t_TM354.get()) <= 57:
                textRight.insert(END,f"TM354\t\t{int(t_TM354.get())}\tD\n\n")
            elif int(t_TM354.get()) < 50 and int(t_TM354.get()) != 0:
                textRight.insert(END,f"TM354\t\t{int(t_TM354.get())}\tF\n\n")
            else:
                textRight.insert(END,f"TM354\t\t{int(t_TM354.get())}\n\n")


    # ******************** pass *********************
        if t_TM366.get() != "0":
            if int(t_TM366.get()) >= 90 and int(t_TM366.get()) <= 100:
                textRight.insert(END,f"TM366\t\t{int(t_TM366.get())}\tA\n\n")
            elif int(t_TM366.get()) >= 82 and int(t_TM366.get()) <= 89:
                textRight.insert(END,f"TM366\t\t{int(t_TM366.get())}\tB+\n\n")
            elif int(t_TM366.get()) >= 74 and int(t_TM366.get()) <= 81:
                textRight.insert(END,f"TM366\t\t{int(t_TM366.get())}\tB\n\n")
            elif int(t_TM366.get()) >= 66 and int(t_TM366.get()) <= 73:
                textRight.insert(END,f"TM366\t\t{int(t_TM366.get())}\tC+\n\n")
            elif int(t_TM366.get()) >= 58 and int(t_TM366.get()) <= 65:
                textRight.insert(END,f"TM366\t\t{int(t_TM366.get())}\tC\n\n")
            elif int(t_TM366.get()) >= 50 and int(t_TM366.get()) <= 57:
                textRight.insert(END,f"TM366\t\t{int(t_TM366.get())}\tD\n\n")
            elif int(t_TM366.get()) < 50 and int(t_TM366.get()) != 0:
                textRight.insert(END,f"TM366\t\t{int(t_TM366.get())}\tF\n\n")
            else:
                textRight.insert(END,f"TM366\t\t{int(t_TM366.get())}\n\n")

    # ******************** pass *********************
        if t_TM471A.get() != "0":
            if int(t_TM471A.get()) >= 90 and int(t_TM471A.get()) <= 100:
                textRight.insert(END,f"TM471A\t\t{int(t_TM471A.get())}\tA\n\n")
            elif int(t_TM471A.get()) >= 82 and int(t_TM471A.get()) <= 89:
                textRight.insert(END,f"TM471A\t\t{int(t_TM471A.get())}\tB+\n\n")
            elif int(t_TM471A.get()) >= 74 and int(t_TM471A.get()) <= 81:
                textRight.insert(END,f"TM471A\t\t{int(t_TM471A.get())}\tB\n\n")
            elif int(t_TM471A.get()) >= 66 and int(t_TM471A.get()) <= 73:
                textRight.insert(END,f"TM471A\t\t{int(t_TM471A.get())}\tC+\n\n")
            elif int(t_TM471A.get()) >= 58 and int(t_TM471A.get()) <= 65:
                textRight.insert(END,f"TM471A\t\t{int(t_TM471A.get())}\tC\n\n")
            elif int(t_TM471A.get()) >= 50 and int(t_TM471A.get()) <= 57:
                textRight.insert(END,f"TM471A\t\t{int(t_TM471A.get())}\tD\n\n")
            elif int(t_TM471A.get()) < 50 and int(t_TM471A.get()) != 0:
                textRight.insert(END,f"TM471A\t\t{int(t_TM471A.get())}\tF\n\n")
            else:
                textRight.insert(END,f"TM471A\t\t{int(t_TM471A.get())}\n\n")

    # ******************** pass *********************
        if t_TM471B.get() != "0":
            if int(t_TM471B.get()) >= 90 and int(t_TM471B.get()) <= 100:
                textRight.insert(END,f"TM471B\t\t{int(t_TM471B.get())}\tA\n\n")
            elif int(t_TM471B.get()) >= 82 and int(t_TM471B.get()) <= 89:
                textRight.insert(END,f"TM471B\t\t{int(t_TM471B.get())}\tB+\n\n")
            elif int(t_TM471B.get()) >= 74 and int(t_TM471B.get()) <= 81:
                textRight.insert(END,f"TM471B\t\t{int(t_TM471B.get())}\tB\n\n")
            elif int(t_TM471B.get()) >= 66 and int(t_TM471B.get()) <= 73:
                textRight.insert(END,f"TM471B\t\t{int(t_TM471B.get())}\tC+\n\n")
            elif int(t_TM471B.get()) >= 58 and int(t_TM471B.get()) <= 65:
                textRight.insert(END,f"TM471B\t\t{int(t_TM471B.get())}\tC\n\n")
            elif int(t_TM471B.get()) >= 50 and int(t_TM471B.get()) <= 57:
                textRight.insert(END,f"TM471B\t\t{int(t_TM471B.get())}\tD\n\n")
            elif int(t_TM471B.get()) < 50 and int(t_TM471B.get()) != 0:
                textRight.insert(END,f"TM471B\t\t{int(t_TM471B.get())}\tF\n\n")
            else:
                textRight.insert(END,f"TM471B\t\t{int(t_TM471B.get())}\n\n")

        hoursLeft = 132 - hoursForm

        textRight.insert(END, "---------------------------------------------------------------------------" + "\n")
        textRight.insert(END, "Total Hours = " + str(hoursForm) + "\t\tHours Left = " + str(hoursLeft) +"\t\tGPA : " + str(entryGPA.get())+"\n")

    else:
        messagebox.showerror("Error", "Please Fill The Fields With Your Information")

def calcIt():

    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var7.get() != 0 or \
            var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or \
            var15.get() != 0 or var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or var21.get() != 0 or \
            var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or var26.get() != 0 or var27.get() != 0 or var28.get() != 0 or \
            var29.get() != 0 or var30.get() != 0 :


        if int(t_AR111.get()) >= 90 and int(t_AR111.get()) <= 100:
            mat1 = 3 * 4
            hour1 = 3
        elif int(t_AR111.get()) >= 82 and int(t_AR111.get()) <= 89:
            mat1 = 3 * 3.5
            hour1 = 3
        elif int(t_AR111.get()) >= 74 and int(t_AR111.get()) <= 81:
            mat1 = 3 * 3
            hour1 = 3
        elif int(t_AR111.get()) >= 66 and int(t_AR111.get()) <= 73:
            mat1 = 3 * 2.5
            hour1 = 3
        elif int(t_AR111.get()) >= 58 and int(t_AR111.get()) <= 65:
            mat1 = 3 * 2
            hour1 = 3
        elif int(t_AR111.get()) >= 50 and int(t_AR111.get()) <= 57:
            mat1 = 3 * 1.5
            hour1 = 3
        elif int(t_AR111.get()) < 50 and int(t_AR111.get()) != 0:
            mat1 = 0
            hour1 = 0
        else:
            mat1=0
            hour1=0

        # ******************** pass *********************
        if int(t_AR112.get()) >= 90 and int(t_AR112.get()) <= 100:
            mat2 = 3 * 4
            hour2 = 3
        elif int(t_AR112.get()) >= 82 and int(t_AR112.get()) <= 89:
            mat2 = 3 * 3.5
            hour2 = 3
        elif int(t_AR112.get()) >= 74 and int(t_AR112.get()) <= 81:
            mat2 = 3 * 3
            hour2 = 3
        elif int(t_AR112.get()) >= 66 and int(t_AR112.get()) <= 73:
            mat2 = 3 * 2.5
            hour2 = 3
        elif int(t_AR112.get()) >= 58 and int(t_AR112.get()) <= 65:
            mat2 = 3 * 2
            hour2 = 3
        elif int(t_AR112.get()) >= 50 and int(t_AR112.get()) <= 57:
            mat2 = 3 * 1.5
            hour2 = 3
        elif int(t_AR112.get()) < 50 and int(t_AR112.get()) != 0:
            mat2 = 0
            hour2 = 0
        else:
            mat2 = 0
            hour2 = 0

        # ******************** pass *********************
        if int(t_EL111.get()) >= 90 and int(t_EL111.get()) <= 100:
            mat3 = 3 * 4
            hour3 = 3
        elif int(t_EL111.get()) >= 82 and int(t_EL111.get()) <= 89:
            mat3 = 3 * 3.5
            hour3 = 3
        elif int(t_EL111.get()) >= 74 and int(t_EL111.get()) <= 81:
            mat3 = 3 * 3
            hour3 = 3
        elif int(t_EL111.get()) >= 66 and int(t_EL111.get()) <= 73:
            mat3 = 3 * 2.5
            hour3 = 3
        elif int(t_EL111.get()) >= 58 and int(t_EL111.get()) <= 65:
            mat3 = 3 * 1.5
            hour3 = 3
        elif int(t_EL111.get()) >= 50 and int(t_EL111.get()) <= 57:
            mat3 = 3 * 2
            hour3 = 3
        elif int(t_EL111.get()) < 50 and int(t_EL111.get()) != 0:
            mat3 = 0
            hour3 = 0
        else:
            mat3 = 0
            hour3 = 0

            # ******************** pass *********************
        if int(t_EL112.get()) >= 90 and int(t_EL112.get()) <= 100:
            mat4 = 3 * 4
            hour4 = 3
        elif int(t_EL112.get()) >= 82 and int(t_EL112.get()) <= 89:
            mat4 = 3 * 3.5
            hour4 = 3
        elif int(t_EL112.get()) >= 74 and int(t_EL112.get()) <= 81:
            mat4 = 3 * 3
            hour4 = 3
        elif int(t_EL112.get()) >= 66 and int(t_EL112.get()) <= 73:
            mat4 = 3 * 2.5
            hour4 = 3
        elif int(t_EL112.get()) >= 58 and int(t_EL112.get()) <= 65:
            mat4 = 3 * 2
            hour4 = 3
        elif int(t_EL112.get()) >= 50 and int(t_EL112.get()) <= 57:
            mat4 = 3 * 1.5
            hour4 = 3
        elif int(t_EL112.get()) < 50 and int(t_EL112.get()) != 0:
            mat4 = 0
            hour4 = 0
        else:
            mat4 = 0
            hour4 = 0

            # ******************** pass *********************
        if int(t_GR101.get()) >= 90 and int(t_GR101.get()) <= 100:
            mat5 = 3 * 4
            hour5 = 3
        elif int(t_GR101.get()) >= 82 and int(t_GR101.get()) <= 89:
            mat5 = 3 * 3.5
            hour5 = 3
        elif int(t_GR101.get()) >= 74 and int(t_GR101.get()) <= 81:
            mat5 = 3 * 3
            hour5 = 3
        elif int(t_GR101.get()) >= 66 and int(t_GR101.get()) <= 73:
            mat5 = 3 * 2.5
            hour5 = 3
        elif int(t_GR101.get()) >= 58 and int(t_GR101.get()) <= 65:
            mat5 = 3 * 2
            hour5 = 3
        elif int(t_GR101.get()) >= 50 and int(t_GR101.get()) <= 57:
            mat5 = 3 * 1.5
            hour5 = 3
        elif int(t_GR101.get()) < 50 and int(t_GR101.get()) != 0:
            mat5 = 0
            hour5 = 0
        else:
            mat5 = 0
            hour5 = 0

            # ******************** pass *********************
        if int(t_TU170.get()) >= 90 and int(t_TU170.get()) <= 100:
            mat6 = 3 * 4
            hour6 = 3
        elif int(t_TU170.get()) >= 82 and int(t_TU170.get()) <= 89:
            mat6 = 3 * 3.5
            hour6 = 3
        elif int(t_TU170.get()) >= 74 and int(t_TU170.get()) <= 81:
            mat6 = 3 * 3
            hour6 = 3
        elif int(t_TU170.get()) >= 66 and int(t_TU170.get()) <= 73:
            mat6 = 3 * 2.5
            hour6 = 3
        elif int(t_TU170.get()) >= 58 and int(t_TU170.get()) <= 65:
            mat6 = 3 * 2
            hour6 = 3
        elif int(t_TU170.get()) >= 50 and int(t_TU170.get()) <= 57:
            mat6 = 3 * 1.5
            hour6 = 3
        elif int(t_TU170.get()) < 50 and int(t_TU170.get()) != 0:
            mat6 = 0
            hour6 = 0
        else:
            mat6 = 0
            hour6 = 0

            # ******************** pass *********************
        if int(t_GR131.get()) >= 90 and int(t_GR131.get()) <= 100:
            mat7 = 3 * 4
            hour7 = 3
        elif int(t_GR131.get()) >= 82 and int(t_GR131.get()) <= 89:
            mat7 = 3 * 3.5
            hour7 = 3
        elif int(t_GR131.get()) >= 74 and int(t_GR131.get()) <= 81:
            mat7 = 3 * 3
            hour7 = 3
        elif int(t_GR131.get()) >= 66 and int(t_GR131.get()) <= 73:
            mat7 = 3 * 2.5
            hour7 = 3
        elif int(t_GR131.get()) >= 58 and int(t_GR131.get()) <= 65:
            mat7 = 3 * 2
            hour7 = 3
        elif int(t_GR131.get()) >= 50 and int(t_GR131.get()) <= 57:
            mat7 = 3 * 1.5
            hour7 = 3
        elif int(t_GR131.get()) < 50 and int(t_GR131.get()) != 0:
            mat7 = 0
            hour7 = 0
        else:
            mat7 = 0
            hour7 = 0

            # ******************** pass *********************
        if int(t_GR111.get()) >= 90 and int(t_GR111.get()) <= 100:
            mat8 = 3 * 4
            hour8 = 3
        elif int(t_GR111.get()) >= 82 and int(t_GR111.get()) <= 89:
            mat8 = 3 * 3.5
            hour8 = 3
        elif int(t_GR111.get()) >= 74 and int(t_GR111.get()) <= 81:
            mat8 = 3 * 3
            hour8 = 3
        elif int(t_GR111.get()) >= 66 and int(t_GR111.get()) <= 73:
            mat8 = 3 * 2.5
            hour8 = 3
        elif int(t_GR111.get()) >= 58 and int(t_GR111.get()) <= 65:
            mat8 = 3 * 2
            hour8 = 3
        elif int(t_GR111.get()) >= 50 and int(t_GR111.get()) <= 57:
            mat8 = 3 * 1.5
            hour8 = 3
        elif int(t_GR111.get()) < 50 and int(t_GR111.get()) != 0:
            mat8 = 0
            hour8 = 0
        else:
            mat8 = 0
            hour8 = 0

            # ******************** pass *********************
        if int(t_EL118.get()) >= 90 and int(t_EL118.get()) <= 100:
            mat9 = 3 * 4
            hour9 = 3
        elif int(t_EL118.get()) >= 82 and int(t_EL118.get()) <= 89:
            mat9 = 3 * 3.5
            hour9 = 3
        elif int(t_EL118.get()) >= 74 and int(t_EL118.get()) <= 81:
            mat9 = 3 * 3
            hour9 = 3
        elif int(t_EL118.get()) >= 66 and int(t_EL118.get()) <= 73:
            mat9 = 3 * 2.5
            hour9 = 3
        elif int(t_EL118.get()) >= 58 and int(t_EL118.get()) <= 65:
            mat9 = 3 * 2
            hour9 = 3
        elif int(t_EL118.get()) >= 50 and int(t_EL118.get()) <= 57:
            mat9 = 3 * 1.5
            hour9 = 3
        elif int(t_EL118.get()) < 50 and int(t_EL118.get()) != 0:
            mat9 = 0
            hour9 = 0
        else:
            mat9 = 0
            hour9 = 0


            # ******************** pass *********************
        if int(t_GR121.get()) >= 90 and int(t_GR121.get()) <= 100:
            mat10 = 3 * 4
            hour10 = 3
        elif int(t_GR121.get()) >= 82 and int(t_GR121.get()) <= 89:
            mat10 = 3 * 3.5
            hour10 = 3
        elif int(t_GR121.get()) >= 74 and int(t_GR121.get()) <= 81:
            mat10 = 3 * 3
            hour10 = 3
        elif int(t_GR121.get()) >= 66 and int(t_GR121.get()) <= 73:
            mat10 = 3 * 2.5
            hour10 = 3
        elif int(t_GR121.get()) >= 58 and int(t_GR121.get()) <= 65:
            mat10 = 3 * 2
            hour10 = 3
        elif int(t_GR121.get()) >= 50 and int(t_GR121.get()) <= 57:
            mat10 = 3 * 1.5
            hour10 = 3
        elif int(t_GR121.get()) < 50 and int(t_GR121.get()) != 0:
            mat10 = 0
            hour10 = 0
        else:
            mat10 = 0
            hour10 = 0

            # ******************** pass *********************
        if int(t_MT131.get()) >= 90 and int(t_MT131.get()) <= 100:
            mat11 = 4 * 4
            hour11 = 4
        elif int(t_MT131.get()) >= 82 and int(t_MT131.get()) <= 89:
            mat11 = 4 * 3.5
            hour11 = 4
        elif int(t_MT131.get()) >= 74 and int(t_MT131.get()) <= 81:
            mat11 = 4 * 3
            hour11 = 4
        elif int(t_MT131.get()) >= 66 and int(t_MT131.get()) <= 73:
            mat11 = 4 * 2.5
            hour11 = 4
        elif int(t_MT131.get()) >= 58 and int(t_MT131.get()) <= 65:
            mat11 = 4 * 2
            hour11 = 4
        elif int(t_MT131.get()) >= 50 and int(t_MT131.get()) <= 57:
            mat11 = 4 * 1.5
            hour11 = 4
        elif int(t_MT131.get()) < 50 and int(t_MT131.get()) != 0:
            mat11 = 0
            hour11 = 0
        else:
            mat11 = 0
            hour11 = 0

            # ******************** pass *********************
        if int(t_MT132.get()) >= 90 and int(t_MT132.get()) <= 100:
            mat12 = 4 * 4
            hour12 = 4
        elif int(t_MT132.get()) >= 82 and int(t_MT132.get()) <= 89:
            mat12 = 4 * 3.5
            hour12 = 4
        elif int(t_MT132.get()) >= 74 and int(t_MT132.get()) <= 81:
            mat12 = 4 * 3
            hour12 = 4
        elif int(t_MT132.get()) >= 66 and int(t_MT132.get()) <= 73:
            mat12 = 4 * 2.5
            hour12 = 4
        elif int(t_MT132.get()) >= 58 and int(t_MT132.get()) <= 65:
            mat12 = 4 * 2
            hour12 = 4
        elif int(t_MT132.get()) >= 50 and int(t_MT132.get()) <= 57:
            mat12 = 4 * 1.5
            hour12 = 4
        elif int(t_MT132.get()) < 50 and int(t_MT132.get()) != 0:
            mat12 = 0
            hour12 = 0
        else:
            mat12 = 0
            hour12 = 0

            # ******************** pass *********************
        if int(t_TM103.get()) >= 90 and int(t_TM103.get()) <= 100:
            mat13 = 4 * 4
            hour13 = 4
        elif int(t_TM103.get()) >= 82 and int(t_TM103.get()) <= 89:
            mat13 = 4 * 3.5
            hour13 = 4
        elif int(t_TM103.get()) >= 74 and int(t_TM103.get()) <= 81:
            mat13 = 4 * 3
            hour13 = 4
        elif int(t_TM103.get()) >= 66 and int(t_TM103.get()) <= 73:
            mat13 = 4 * 2.5
            hour13 = 4
        elif int(t_TM103.get()) >= 58 and int(t_TM103.get()) <= 65:
            mat13 = 4 * 2
            hour13 = 4
        elif int(t_TM103.get()) >= 50 and int(t_TM103.get()) <= 57:
            mat13 = 4 * 1.5
            hour13 = 4
        elif int(t_TM103.get()) < 50 and int(t_TM103.get()) != 0:
            mat13 = 0
            hour13 = 0
        else:
            mat13 = 0
            hour13 = 0

            # ******************** pass *********************
        if int(t_TM105.get()) >= 90 and int(t_TM105.get()) <= 100:
            mat14 = 4 * 4
            hour14 = 4
        elif int(t_TM105.get()) >= 82 and int(t_TM105.get()) <= 89:
            mat14 = 4 * 3.5
            hour14 = 4
        elif int(t_TM105.get()) >= 74 and int(t_TM105.get()) <= 81:
            mat14 = 4 * 3
            hour14 = 4
        elif int(t_TM105.get()) >= 66 and int(t_TM105.get()) <= 73:
            mat14 = 4 * 2.5
            hour14 = 4
        elif int(t_TM105.get()) >= 58 and int(t_TM105.get()) <= 65:
            mat14 = 4 * 2
            hour14 = 4
        elif int(t_TM105.get()) >= 50 and int(t_TM105.get()) <= 57:
            mat14 = 4 * 1.5
            hour14 = 4
        elif int(t_TM105.get()) < 50 and int(t_TM105.get()) != 0:
            mat14 = 0
            hour14 = 0
        else:
            mat14 = 0
            hour14 = 0

            # ******************** pass *********************
        if int(t_TM111.get()) >= 90 and int(t_TM111.get()) <= 100:
            mat15 = 8 * 4
            hour15 = 8
        elif int(t_TM111.get()) >= 82 and int(t_TM111.get()) <= 89:
            mat15 = 8 * 3.5
            hour15 = 8
        elif int(t_TM111.get()) >= 74 and int(t_TM111.get()) <= 81:
            mat15 = 8 * 3
            hour15 = 8
        elif int(t_TM111.get()) >= 66 and int(t_TM111.get()) <= 73:
            mat15 = 8 * 2.5
            hour15 = 8
        elif int(t_TM111.get()) >= 58 and int(t_TM111.get()) <= 65:
            mat15 = 8 * 2
            hour15 = 8
        elif int(t_TM111.get()) >= 50 and int(t_TM111.get()) <= 57:
            mat15 = 8 * 1.5
            hour15 = 8
        elif int(t_TM111.get()) < 50 and int(t_TM111.get()) != 0:
            mat15 = 0
            hour15 = 0
        else:
            mat15 = 0
            hour15 = 0

            # ******************** pass *********************
        if int(t_TM112.get()) >= 90 and int(t_TM112.get()) <= 100:
            mat16 = 8 * 4
            hour16 = 8
        elif int(t_TM112.get()) >= 82 and int(t_TM112.get()) <= 89:
            mat16 = 8 * 3.5
            hour16 = 8
        elif int(t_TM112.get()) >= 74 and int(t_TM112.get()) <= 81:
            mat16 = 8 * 3
            hour16 = 8
        elif int(t_TM112.get()) >= 66 and int(t_TM112.get()) <= 73:
            mat16 = 8 * 2.5
            hour16 = 8
        elif int(t_TM112.get()) >= 58 and int(t_TM112.get()) <= 65:
            mat16 = 8 * 2
            hour16 = 8
        elif int(t_TM112.get()) >= 50 and int(t_TM112.get()) <= 57:
            mat16 = 8 * 1.5
            hour16 = 8
        elif int(t_TM112.get()) < 50 and int(t_TM112.get()) != 0:
            mat16 = 0
            hour16 = 0
        else:
            mat16 = 0
            hour16 = 0

            # ******************** pass *********************
        if int(t_M251.get()) >= 90 and int(t_M251.get()) <= 100:
            mat17 = 8 * 4
            hour17 = 8
        elif int(t_M251.get()) >= 82 and int(t_M251.get()) <= 89:
            mat17 = 8 * 3.5
            hour17 = 8
        elif int(t_M251.get()) >= 74 and int(t_M251.get()) <= 81:
            mat17 = 8 * 3
            hour17 = 8
        elif int(t_M251.get()) >= 66 and int(t_M251.get()) <= 73:
            mat17 = 8 * 2.5
            hour17 = 8
        elif int(t_M251.get()) >= 58 and int(t_M251.get()) <= 65:
            mat17 = 8 * 2
            hour17 = 8
        elif int(t_M251.get()) >= 50 and int(t_M251.get()) <= 57:
            mat17 = 8 * 1.5
            hour17 = 8
        elif int(t_M251.get()) < 50 and int(t_M251.get()) != 0:
            mat17 = 0
            hour17 = 0
        else:
            mat17 = 0
            hour17 = 0

            # ******************** pass *********************
        if int(t_M269.get()) >= 90 and int(t_M269.get()) <= 100:
            mat18 = 8 * 4
            hour18 = 8
        elif int(t_M269.get()) >= 82 and int(t_M269.get()) <= 89:
            mat18 = 8 * 3.5
            hour18 = 8
        elif int(t_M269.get()) >= 74 and int(t_M269.get()) <= 81:
            mat18 = 8 * 3
            hour18 = 8
        elif int(t_M269.get()) >= 66 and int(t_M269.get()) <= 73:
            mat18 = 8 * 2.5
            hour18 = 8
        elif int(t_M269.get()) >= 58 and int(t_M269.get()) <= 65:
            mat18 = 8 * 2
            hour18 = 8
        elif int(t_M269.get()) >= 50 and int(t_M269.get()) <= 57:
            mat18 = 8 * 1.5
            hour18 = 8
        elif int(t_M269.get()) < 50 and int(t_M269.get()) != 0:
            mat18 = 0
            hour18 = 0
        else:
            mat18 = 0
            hour18 = 0

            # ******************** pass *********************
        if int(t_T227.get()) >= 90 and int(t_T227.get()) <= 100:
            mat19 = 8 * 4
            hour19 = 8
        elif int(t_T227.get()) >= 82 and int(t_T227.get()) <= 89:
            mat19 = 8 * 3.5
            hour19 = 8
        elif int(t_T227.get()) >= 74 and int(t_T227.get()) <= 81:
            mat19 = 8 * 3
            hour19 = 8
        elif int(t_T227.get()) >= 66 and int(t_T227.get()) <= 73:
            mat19 = 8 * 2.5
            hour19 = 8
        elif int(t_T227.get()) >= 58 and int(t_T227.get()) <= 65:
            mat19 = 8 * 2
            hour19 = 8
        elif int(t_T227.get()) >= 50 and int(t_T227.get()) <= 57:
            mat19 = 8 * 1.5
            hour19 = 8
        elif int(t_T227.get()) < 50 and int(t_T227.get()) != 0:
            mat19 = 0
            hour19 = 0
        else:
            mat19 = 0
            hour19 = 0

            # ******************** pass *********************
        if int(t_TM240.get()) >= 90 and int(t_TM240.get()) <= 100:
            mat20 = 4 * 4
            hour20 = 4
        elif int(t_TM240.get()) >= 82 and int(t_TM240.get()) <= 89:
            mat20 = 4 * 3.5
            hour20 = 4
        elif int(t_TM240.get()) >= 74 and int(t_TM240.get()) <= 81:
            mat20 = 4 * 3
            hour20 = 4
        elif int(t_TM240.get()) >= 66 and int(t_TM240.get()) <= 73:
            mat20 = 4 * 2.5
            hour20 = 4
        elif int(t_TM240.get()) >= 58 and int(t_TM240.get()) <= 65:
            mat20 = 4 * 2
            hour20 = 4
        elif int(t_TM240.get()) >= 50 and int(t_TM240.get()) <= 57:
            mat20 = 4 * 1.5
            hour20 = 4
        elif int(t_TM240.get()) < 50 and int(t_TM240.get()) != 0:
            mat20 = 0
            hour20 = 0
        else:
            mat20 = 0
            hour20 = 0

            # ******************** pass *********************
        if int(t_MT101.get()) >= 90 and int(t_MT101.get()) <= 100:
            mat21 = 3 * 4
            hour21 = 3
        elif int(t_MT101.get()) >= 82 and int(t_MT101.get()) <= 89:
            mat21 = 3 * 3.5
            hour21 = 3
        elif int(t_MT101.get()) >= 74 and int(t_MT101.get()) <= 81:
            mat21 = 3 * 3
            hour21 = 3
        elif int(t_MT101.get()) >= 66 and int(t_MT101.get()) <= 73:
            mat21 = 3 * 2.5
            hour21 = 3
        elif int(t_MT101.get()) >= 58 and int(t_MT101.get()) <= 65:
            mat21 = 3 * 2
            hour21 = 3
        elif int(t_MT101.get()) >= 50 and int(t_MT101.get()) <= 57:
            mat21 = 3 * 1.5
            hour21 = 3
        elif int(t_MT101.get()) < 50 and int(t_MT101.get()) != 0:
            mat21 = 0
            hour21 = 0
        else:
            mat21 = 0
            hour21 = 0

            # ******************** pass *********************
        if int(t_MT129.get()) >= 90 and int(t_MT129.get()) <= 100:
            mat22 = 4 * 4
            hour22 = 4
        elif int(t_MT129.get()) >= 82 and int(t_MT129.get()) <= 89:
            mat22 = 4 * 3.5
            hour22 = 4
        elif int(t_MT129.get()) >= 74 and int(t_MT129.get()) <= 81:
            mat22 = 4 * 3
            hour22 = 4
        elif int(t_MT129.get()) >= 66 and int(t_MT129.get()) <= 73:
            mat22 = 4 * 2.5
            hour22 = 4
        elif int(t_MT129.get()) >= 58 and int(t_MT129.get()) <= 65:
            mat22 = 4 * 2
            hour22 = 4
        elif int(t_MT129.get()) >= 50 and int(t_MT129.get()) <= 57:
            mat22 = 4 * 1.5
            hour22 = 4
        elif int(t_MT129.get()) < 50 and int(t_MT129.get()) != 0:
            mat22 = 0
            hour22 = 0
        else:
            mat22 = 0
            hour22 = 0

            # ******************** pass *********************
        if int(t_M109.get()) >= 90 and int(t_M109.get()) <= 100:
            mat23 = 3 * 4
            hour23 = 3
        elif int(t_M109.get()) >= 82 and int(t_M109.get()) <= 89:
            mat23 = 3 * 3.5
            hour23 = 3
        elif int(t_M109.get()) >= 74 and int(t_M109.get()) <= 81:
            mat23 = 3 * 3
            hour23 = 3
        elif int(t_M109.get()) >= 66 and int(t_M109.get()) <= 73:
            mat23 = 3 * 2.5
            hour23 = 3
        elif int(t_M109.get()) >= 58 and int(t_M109.get()) <= 65:
            mat23 = 3 * 2
            hour23 = 3
        elif int(t_M109.get()) >= 50 and int(t_M109.get()) <= 57:
            mat23 = 3 * 1.5
            hour23 = 3
        elif int(t_M109.get()) < 50 and int(t_M109.get()) != 0:
            mat23 = 0
            hour23 = 0
        else:
            mat23 = 0
            hour23 = 0

            # ******************** pass *********************
        if int(t_MS102.get()) >= 90 and int(t_MS102.get()) <= 100:
            mat24 = 3 * 4
            hour24 = 3
        elif int(t_MS102.get()) >= 82 and int(t_MS102.get()) <= 89:
            mat24 = 3 * 3.5
            hour24 = 3
        elif int(t_MS102.get()) >= 74 and int(t_MS102.get()) <= 81:
            mat24 = 3 * 3
            hour24 = 3
        elif int(t_MS102.get()) >= 66 and int(t_MS102.get()) <= 73:
            mat24 = 3 * 2.5
            hour24 = 3
        elif int(t_MS102.get()) >= 58 and int(t_MS102.get()) <= 65:
            mat24 = 3 * 2
            hour24 = 3
        elif int(t_MS102.get()) >= 50 and int(t_MS102.get()) <= 57:
            mat24 = 3 * 1.5
            hour24 = 3
        elif int(t_MS102.get()) < 50 and int(t_MS102.get()) != 0:
            mat24 = 0
            hour24 = 0
        else:
            mat24 = 0
            hour24 = 0

            # ******************** pass *********************
        if int(t_TM298.get()) >= 90 and int(t_TM298.get()) <= 100:
            mat25 = 4 * 4
            hour25 = 4
        elif int(t_TM298.get()) >= 82 and int(t_TM298.get()) <= 89:
            mat25 = 4 * 3.5
            hour25 = 4
        elif int(t_TM298.get()) >= 74 and int(t_TM298.get()) <= 81:
            mat25 = 4 * 3
            hour25 = 4
        elif int(t_TM298.get()) >= 66 and int(t_TM298.get()) <= 73:
            mat25 = 4 * 2.5
            hour25 = 4
        elif int(t_TM298.get()) >= 58 and int(t_TM298.get()) <= 65:
            mat25 = 4 * 2
            hour25 = 4
        elif int(t_TM298.get()) >= 50 and int(t_TM298.get()) <= 57:
            mat25 = 4 * 1.5
            hour25 = 4
        elif int(t_TM298.get()) < 50 and int(t_TM298.get()) != 0:
            mat25 = 0
            hour25 = 0
        else:
            mat25 = 0
            hour25 = 0

            # ******************** pass *********************
        if int(t_TM351.get()) >= 90 and int(t_TM351.get()) <= 100:
            mat26 = 8 * 4
            hour26 = 8
        elif int(t_TM351.get()) >= 82 and int(t_TM351.get()) <= 89:
            mat26 = 8 * 3.5
            hour26 = 8
        elif int(t_TM351.get()) >= 74 and int(t_TM351.get()) <= 81:
            mat26 = 8 * 3
            hour26 = 8
        elif int(t_TM351.get()) >= 66 and int(t_TM351.get()) <= 73:
            mat26 = 8 * 2.5
            hour26 = 8
        elif int(t_TM351.get()) >= 58 and int(t_TM351.get()) <= 65:
            mat26 = 8 * 2
            hour26 = 8
        elif int(t_TM351.get()) >= 50 and int(t_TM351.get()) <= 57:
            mat26 = 8 * 1.5
            hour26 = 8
        elif int(t_TM351.get()) < 50 and int(t_TM351.get()) != 0:
            mat26 = 0
            hour26 = 0
        else:
            mat26 = 0
            hour26 = 0

            # ******************** pass *********************
        if int(t_TM354.get()) >= 90 and int(t_TM354.get()) <= 100:
            mat27 = 8 * 4
            hour27 = 8
        elif int(t_TM354.get()) >= 82 and int(t_TM354.get()) <= 89:
            mat27 = 8 * 3.5
            hour27 = 8
        elif int(t_TM354.get()) >= 74 and int(t_TM354.get()) <= 81:
            mat27 = 8 * 3
            hour27 = 8
        elif int(t_TM354.get()) >= 66 and int(t_TM354.get()) <= 73:
            mat27 = 8 * 2.5
            hour27 = 8
        elif int(t_TM354.get()) >= 58 and int(t_TM354.get()) <= 65:
            mat27 = 8 * 2
            hour27 = 8
        elif int(t_TM354.get()) >= 50 and int(t_TM354.get()) <= 57:
            mat27 = 8 * 1.5
            hour27 = 8
        elif int(t_TM354.get()) < 50 and int(t_TM354.get()) != 0:
            mat27 = 0
            hour27 = 0
        else:
            mat27 = 0
            hour27 = 0

            # ******************** pass *********************
        if int(t_TM366.get()) >= 90 and int(t_TM366.get()) <= 100:
            mat28 = 8 * 4
            hour28 = 8
        elif int(t_TM366.get()) >= 82 and int(t_TM366.get()) <= 89:
            mat28 = 8 * 3.5
            hour28 = 8
        elif int(t_TM366.get()) >= 74 and int(t_TM366.get()) <= 81:
            mat28 = 8 * 3
            hour28 = 8
        elif int(t_TM366.get()) >= 66 and int(t_TM366.get()) <= 73:
            mat28 = 8 * 2.5
            hour28 = 8
        elif int(t_TM366.get()) >= 58 and int(t_TM366.get()) <= 65:
            mat28 = 8 * 2
            hour28 = 8
        elif int(t_TM366.get()) >= 50 and int(t_TM366.get()) <= 57:
            mat28 = 8 * 1.5
            hour28 = 8
        elif int(t_TM366.get()) < 50 and int(t_TM366.get()) != 0:
            mat28 = 0
            hour28 = 0
        else:
            mat28 = 0
            hour28 = 0

            # ******************** pass *********************
        if int(t_TM471A.get()) >= 90 and int(t_TM471A.get()) <= 100:
            mat29 = 4 * 4
            hour29 = 4
        elif int(t_TM471A.get()) >= 82 and int(t_TM471A.get()) <= 89:
            mat29 = 4 * 3.5
            hour29 = 4
        elif int(t_TM471A.get()) >= 74 and int(t_TM471A.get()) <= 81:
            mat29 = 4 * 3
            hour29 = 4
        elif int(t_TM471A.get()) >= 66 and int(t_TM471A.get()) <= 73:
            mat29 = 4 * 2.5
            hour29 = 4
        elif int(t_TM471A.get()) >= 58 and int(t_TM471A.get()) <= 65:
            mat29 = 4 * 2
            hour29 = 4
        elif int(t_TM471A.get()) >= 50 and int(t_TM471A.get()) <= 57:
            mat29 = 4 * 1.5
            hour29 = 4
        elif int(t_TM471A.get()) < 50 and int(t_TM471A.get()) != 0:
            mat29 = 0
            hour29 = 0
        else:
            mat29 = 0
            hour29 = 0

            # ******************** pass *********************
        if int(t_TM471B.get()) >= 90 and int(t_TM471B.get()) <= 100:
            mat30 = 4 * 4
            hour30 = 4
        elif int(t_TM471B.get()) >= 82 and int(t_TM471B.get()) <= 89:
            mat30 = 4 * 3.5
            hour30 = 4
        elif int(t_TM471B.get()) >= 74 and int(t_TM471B.get()) <= 81:
            mat30 = 4 * 3
            hour30 = 4
        elif int(t_TM471B.get()) >= 66 and int(t_TM471B.get()) <= 73:
            mat30 = 4 * 2.5
            hour30 = 4
        elif int(t_TM471B.get()) >= 58 and int(t_TM471B.get()) <= 65:
            mat30 = 4 * 2
            hour30 = 4
        elif int(t_TM471B.get()) >= 50 and int(t_TM471B.get()) <= 57:
            mat30 = 4 * 1.5
            hour30 = 4
        elif int(t_TM471B.get()) < 50 and int(t_TM471B.get()) != 0:
            mat30 = 0
            hour30 = 0
        else:
            mat30 = 0
            hour30 = 0


        sum = (mat1+mat2+mat3+mat4+mat5+mat6+mat7+mat8+mat9+mat10+mat11+mat12+mat13+mat14+mat15+mat16+mat17+mat18+mat19+mat20+mat21+mat22+mat23+mat24+mat25+mat26+mat27+mat28+mat29+mat30)\
              / (hour1+hour2+hour3+hour4+hour5+hour6+hour7+hour8+hour9+hour10+hour11+hour12+hour13+hour14+hour15+hour16+hour17+hour18+hour19+hour20+hour21+hour22+hour23+hour24+hour25+hour26+hour27+hour28+hour29+hour30)
        num = '{0:.2f}'.format(sum)

        gpaCalc.set(str(num))

        hoursCALC = hour1+hour2+hour3+hour4+hour5+hour6+hour7+hour8+hour9+hour10+hour11+hour12+hour13+hour14+hour15+hour16+hour17+hour18+hour19+hour20+hour21+hour22+hour23+hour24+hour25+hour26+hour27+hour28+hour29+hour30
        hoursleft.set(str(hoursCALC))

    else:
        messagebox.showerror("Error", "Please Select A University Material")

#******************** Info *********************

root = Tk()

root.geometry("1170x690+0+0")
root.resizable(0, 0)
root.title("GPA Calculator")
root.config(bg="#61FFFF")

#******************** Top Frame *********************

topFrame = Frame(root, bd=10, relief=RIDGE, bg="white")
topFrame.pack(side=TOP)

titleLabel = Label(topFrame, text="GPA Calculator", font=('arial', 30, 'bold'),
                   fg='white', bg='#4E4E4E', width=55, bd=9)
titleLabel.grid(row=0, column=0)

#******************** Middle Left Frame *********************

materialFrame = Frame(root, bd=5, relief=RIDGE, bg="black")
materialFrame.pack(side=LEFT)

cGPAFrame = Frame(materialFrame, bd=4, relief=RIDGE, bg="black", pady=25)
cGPAFrame.pack(side=BOTTOM)

materialGrade = LabelFrame(materialFrame, text="Mandatory", font=("arial", 19, "bold"),
                       bd=10, relief=RIDGE, fg="#61FFFF", bg="black")
materialGrade.pack(side=LEFT)

materialGrade2 = LabelFrame(materialFrame, text="Specialization", font=("arial", 19, "bold"),
                       bd=10, relief=RIDGE, fg="#61FFFF", bg="black")
materialGrade2.pack(side=LEFT)

materialGrade3 = LabelFrame(materialFrame, text="Specialization", font=("arial", 19, "bold"),
                       bd=10, relief=RIDGE, fg="#61FFFF", bg="black")
materialGrade3.pack(side=LEFT)

#******************** Variables *********************

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()

t_AR111 = StringVar()
t_AR111.set("0")
t_AR112 = StringVar()
t_AR112.set("0")
t_EL111 = StringVar()
t_EL111.set("0")
t_EL112 = StringVar()
t_EL112.set("0")
t_GR101 = StringVar()
t_GR101.set("0")
t_TU170 = StringVar()
t_TU170.set("0")
t_GR131 = StringVar()
t_GR131.set("0")
t_GR111 = StringVar()
t_GR111.set("0")
t_EL118 = StringVar()
t_EL118.set("0")
t_GR121 = StringVar()
t_GR121.set("0")

var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()

t_MT131 = StringVar()
t_MT131.set("0")
t_MT132 = StringVar()
t_MT132.set("0")
t_TM103 = StringVar()
t_TM103.set("0")
t_TM105 = StringVar()
t_TM105.set("0")
t_TM111 = StringVar()
t_TM111.set("0")
t_TM112 = StringVar()
t_TM112.set("0")
t_M251 = StringVar()
t_M251.set("0")
t_M269 = StringVar()
t_M269.set("0")
t_T227 = StringVar()
t_T227.set("0")
t_TM240 = StringVar()
t_TM240.set("0")

var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = IntVar()
var30 = IntVar()

t_MT129 = StringVar()
t_MT129.set("0")
t_M109 = StringVar()
t_M109.set("0")
t_MS102 = StringVar()
t_MS102.set("0")
t_MT101 = StringVar()
t_MT101.set("0")
t_TM298 = StringVar()
t_TM298.set("0")
t_TM351 = StringVar()
t_TM351.set("0")
t_TM354 = StringVar()
t_TM354.set("0")
t_TM366 = StringVar()
t_TM366.set("0")
t_TM471A = StringVar()
t_TM471A.set("0")
t_TM471B = StringVar()
t_TM471B.set("0")

gpaCalc = StringVar()
hoursleft = StringVar()

#******************** Middle Left Frame (Data) *********************
#******************** Mandatory *********************

AR111 = Checkbutton(materialGrade, text="AR111", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var1, command=AR111, fg="white", bg="black")
AR111.grid(row=0, column=0)

AR112 = Checkbutton(materialGrade, text="AR112", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var2, command=AR112, fg="white", bg="black")
AR112.grid(row=1, column=0)

EL111 = Checkbutton(materialGrade, text="EL111", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var3, command=EL111, fg="white", bg="black")
EL111.grid(row=2, column=0)

EL112 = Checkbutton(materialGrade, text="EL112", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var4, command=EL112, fg="white", bg="black")
EL112.grid(row=3, column=0)

GR101 = Checkbutton(materialGrade, text="GR101", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var5, command=GR101, fg="white", bg="black")
GR101.grid(row=4, column=0)

TU170 = Checkbutton(materialGrade, text="TU170", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var6, command=TU170, fg="white", bg="black")
TU170.grid(row=5, column=0)

GR131 = Checkbutton(materialGrade, text="GR131", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var7, command=GR131, fg="white", bg="black")
GR131.grid(row=6, column=0)

GR111 = Checkbutton(materialGrade, text="GR111", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var8, command=GR111, fg="white", bg="black")
GR111.grid(row=7, column=0)

EL118 = Checkbutton(materialGrade, text="EL118", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var9, command=EL118, fg="white", bg="black")
EL118.grid(row=8, column=0)

GR121 = Checkbutton(materialGrade, text="GR121", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var10, command=GR121, fg="white", bg="black")
GR121.grid(row=9, column=0)



#******************** Middle Left Frame (Data) *********************
#******************** Mandatory (Entry Field) *********************

textAR111 = Entry(materialGrade, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_AR111)
textAR111.grid(row=0, column=1)

textAR112 = Entry(materialGrade, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_AR112)
textAR112.grid(row=1, column=1)

textEL111 = Entry(materialGrade, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_EL111)
textEL111.grid(row=2, column=1)

textEL112 = Entry(materialGrade, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_EL112)
textEL112.grid(row=3, column=1)

textGR101 = Entry(materialGrade, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_GR101)
textGR101.grid(row=4, column=1)

textTU170 = Entry(materialGrade, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_TU170)
textTU170.grid(row=5, column=1)

textGR131 = Entry(materialGrade, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_GR131)
textGR131.grid(row=6, column=1)

textGR111 = Entry(materialGrade, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_GR111)
textGR111.grid(row=7, column=1)

textEL118 = Entry(materialGrade, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_EL118)
textEL118.grid(row=8, column=1)

textGR121 = Entry(materialGrade, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_GR121)
textGR121.grid(row=9, column=1)




#******************** Middle Left Frame (Data) **********************
#******************** Specialization **********************

MT131 = Checkbutton(materialGrade2, text="MT131", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var11, command=MT131, fg="white", bg="black")
MT131.grid(row=0, column=0)

MT132 = Checkbutton(materialGrade2, text="MT132", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var12, command=MT132, fg="white", bg="black")
MT132.grid(row=1, column=0)

TM103 = Checkbutton(materialGrade2, text="TM103", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var13, command=TM103, fg="white", bg="black")
TM103.grid(row=2, column=0)

TM105 = Checkbutton(materialGrade2, text="TM105", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var14, command=TM105, fg="white", bg="black")
TM105.grid(row=3, column=0)

TM111 = Checkbutton(materialGrade2, text="TM111", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var15, command=TM111, fg="white", bg="black")
TM111.grid(row=4, column=0)

TM112 = Checkbutton(materialGrade2, text="TM112", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var16, command=TM112, fg="white", bg="black")
TM112.grid(row=5, column=0)

M251 = Checkbutton(materialGrade2, text="M251", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var17, command=M251, fg="white", bg="black")
M251.grid(row=6, column=0)

M269 = Checkbutton(materialGrade2, text="M269", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var18, command=M269, fg="white", bg="black")
M269.grid(row=7, column=0)

T227 = Checkbutton(materialGrade2, text="T227", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var19, command=T227, fg="white", bg="black")
T227.grid(row=8, column=0)

TM240 = Checkbutton(materialGrade2, text="TM240", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var20, command=TM240, fg="white", bg="black")
TM240.grid(row=9, column=0)

#******************** Middle Left Frame (Data) *********************
#******************** Specialization (Entry Field) *********************, command=

textMT131 = Entry(materialGrade2, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_MT131)
textMT131.grid(row=0, column=1)

textMT132 = Entry(materialGrade2, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_MT132)
textMT132.grid(row=1, column=1)

textTM103 = Entry(materialGrade2, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_TM103)
textTM103.grid(row=2, column=1)

textTM105 = Entry(materialGrade2, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_TM105)
textTM105.grid(row=3, column=1)

textTM111 = Entry(materialGrade2, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_TM111)
textTM111.grid(row=4, column=1)

textTM112 = Entry(materialGrade2, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_TM112)
textTM112.grid(row=5, column=1)

textM251 = Entry(materialGrade2, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_M251)
textM251.grid(row=6, column=1)

textM269 = Entry(materialGrade2, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_M269)
textM269.grid(row=7, column=1)

textT227 = Entry(materialGrade2, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_T227)
textT227.grid(row=8, column=1)

textTM240 = Entry(materialGrade2, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_TM240)
textTM240.grid(row=9, column=1)

#******************** 2 **********************
#******************** Middle Left Frame (Data) **********************
#******************** Specialization **********************

MT101 = Checkbutton(materialGrade3, text="MT101", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var21, command=MT101, fg="white", bg="black")
MT101.grid(row=0, column=0)

MT129 = Checkbutton(materialGrade3, text="MT129", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var22, command=MT129, fg="white", bg="black")
MT129.grid(row=1, column=0)

M109 = Checkbutton(materialGrade3, text="M109", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var23, command=M109, fg="white", bg="black")
M109.grid(row=2, column=0)

MS102 = Checkbutton(materialGrade3, text="MS102", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var24, command=MS102, fg="white", bg="black")
MS102.grid(row=3, column=0)

TM298 = Checkbutton(materialGrade3, text="TM298", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var25, command=TM298, fg="white", bg="black")
TM298.grid(row=4, column=0)

TM351 = Checkbutton(materialGrade3, text="TM351", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var26, command=TM351, fg="white", bg="black")
TM351.grid(row=5, column=0)

TM354 = Checkbutton(materialGrade3, text="TM354", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var27, command=TM354, fg="white", bg="black")
TM354.grid(row=6, column=0)

TM366 = Checkbutton(materialGrade3, text="TM366", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var28, command=TM366, fg="white", bg="black")
TM366.grid(row=7, column=0)

TM471A = Checkbutton(materialGrade3, text="TM471 P.A", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var29, command=TM471A, fg="white", bg="black")
TM471A.grid(row=8, column=0)

TM471B = Checkbutton(materialGrade3, text="TM471 P.B", font=("arial", 18, "bold"), onvalue=1, offvalue=0, variable=var30, command=TM471B, fg="white", bg="black")
TM471B.grid(row=9, column=0)


#******************** Middle Left Frame (Data) *********************
#******************** Specialization (Entry Field) *********************


textMT101 = Entry(materialGrade3, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_MT101)
textMT101.grid(row=0, column=1)

textMT129 = Entry(materialGrade3, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_MT129)
textMT129.grid(row=1, column=1)

textM109 = Entry(materialGrade3, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_M109)
textM109.grid(row=2, column=1)

textMS102 = Entry(materialGrade3, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_MS102)
textMS102.grid(row=3, column=1)

textTM298 = Entry(materialGrade3, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_TM298)
textTM298.grid(row=4, column=1)

textTM351 = Entry(materialGrade3, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_TM351)
textTM351.grid(row=5, column=1)

textTM354 = Entry(materialGrade3, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_TM354)
textTM354.grid(row=6, column=1)

textTM366 = Entry(materialGrade3, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_TM366)
textTM366.grid(row=7, column=1)

textTM471A = Entry(materialGrade3, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_TM471A)
textTM471A.grid(row=8, column=1)

textTM471B = Entry(materialGrade3, font=("arial", 18, "bold"), bd=7, width=6, state=DISABLED, textvariable=t_TM471B)
textTM471B.grid(row=9, column=1)

#******************** GPA Label **********************

LabelGPA = Label(cGPAFrame, text="Calculated GPA", font=("arial", 16, "bold"), bg="black", fg="white")
LabelGPA.grid(row=0, column=0)

entryGPA = Entry(cGPAFrame, font=("arial", 16, "bold"), bd=6, width=14, state="readonly", textvariable=gpaCalc)
entryGPA.grid(row=0, column=1, padx=15)

LabelHours = Label(cGPAFrame, text="Total Hours", font=("arial", 16, "bold"), bg="black", fg="white")
LabelHours.grid(row=0, column=4)

entryHours = Entry(cGPAFrame, font=("arial", 16, "bold"), bd=6, width=14, state="readonly", textvariable=hoursleft)
entryHours.grid(row=0, column=5, padx=15)

#******************** Middle Right Frame *********************

rightFrame = Frame(root, bd=15, relief=RIDGE, bg="white")
rightFrame.pack(side=RIGHT)

materialRight = Frame(rightFrame, bd=1, relief=RIDGE, bg="#61FFFF")
materialRight.pack()

infoFrame = Frame(rightFrame, bd=4, relief=RIDGE, bg="#61FFFF")
infoFrame.pack()

editFrame = Frame(rightFrame, bd=3, relief=RIDGE, bg="#61FFFF")
editFrame.pack()

#******************** Middle Right Frame *********************
#******************** Buttons *********************

buttonGPA = Button(editFrame, text="GPA", font=("arial", 14, "bold"), fg="white", bg="black", bd=3, command=calcIt)
buttonGPA.grid(row=0, column=0)

buttonView = Button(editFrame, text="View", font=("arial", 14, "bold"), fg="white", bg="black", bd=3, padx=9, command=review)
buttonView.grid(row=0, column=1)

buttonSave = Button(editFrame, text="Save", font=("arial", 14, "bold"), fg="white", bg="black", bd=3, padx=9, command=save)
buttonSave.grid(row=0, column=2)

buttonSend = Button(editFrame, text="Send", font=("arial", 14, "bold"), fg="white", bg="black", bd=3, padx=9, command=send)
buttonSend.grid(row=0, column=3)

buttonReset = Button(editFrame, text="Reset", font=("arial", 14, "bold"), fg="white", bg="black", bd=3, padx=9, command=reset2)
buttonReset.grid(row=0, column=4)

#******************** Middle Right Frame *********************
#******************** Text Area *********************

textRight = Text(infoFrame, font=("arial", 12, "bold"), bd=3, width=42, height=14)
textRight.grid(row=0, column=0)

#******************** Middle Right Frame *********************
#******************** Register Save Information *********************

nameLabel = Label(materialRight, text="Name", font=("arial", 14, "bold"), fg="black", bd=3, padx=10, width=4, bg='#61FFFF')
nameLabel.grid(row=0, column=0)

nameField = Entry(materialRight, font=("arial", 16, "bold"), width=9, bd=4, bg='#D7E9FD')
nameField.grid(row=0, column=1)

IDLabel = Label(materialRight, text="ID", font=("arial", 14, "bold"), fg="black", bd=3, padx=10, width=4, bg='#61FFFF')
IDLabel.grid(row=0, column=2)

IDField = Entry(materialRight, font=("arial", 16, "bold"), width=9, bd=4, bg='#D7E9FD')
IDField.grid(row=0, column=3)

hoursLabel = Label(materialRight, text="Hours", font=("arial", 14, "bold"), fg="black", bd=3, padx=10, width=4, bg='#61FFFF')
hoursLabel.grid(row=1, column=0)

hoursField = Entry(materialRight, font=("arial", 16, "bold"), width=9, bd=4, bg='#D7E9FD')
hoursField.grid(row=1, column=1, padx=3)

passwordLabel = Label(materialRight, text="Pass", font=("arial", 14, "bold"), fg="black", bd=3, padx=10, width=4, bg='#61FFFF')
passwordLabel.grid(row=1, column=2, padx=3)

passwordField = Entry(materialRight, font=("arial", 16, "bold"), width=9, bd=4, show='*', bg='#D7E9FD')
passwordField.grid(row=1, column=3)

exitInfo = Button(materialRight, text="Exit", font=("arial", 14, "bold"), fg="white", bg="black", bd=3, width=6, command=exit)
exitInfo.grid(row=3, column=0, pady=3, padx =6)

saveInfo = Button(materialRight, text="Save", font=("arial", 14, "bold"), fg="white", bg="black", bd=3, width=6, command=loading)
saveInfo.grid(row=3, column=3, pady=3, padx =6)






root.mainloop()