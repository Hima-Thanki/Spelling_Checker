from textblob import TextBlob
from tkinter import *

def correct_spe():
    get_data = enter1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    enter2.delete(0,END)
    enter2.insert(0,data)

def main_window():
    global enter1,enter2
    win = Tk()
    win.geometry("500x350")
    win.resizable(False,False)
    win.config(bg="Green")
    win.title("hello")

    label1 = Label(win,text="Incorrect Spelling",font=("Time New Roman",20,"bold"),bg="Green",fg="White")
    label1.place(x=50,y=20,height=50,width=240)

    enter1 = Entry(win,font=("Time New Roman",16))
    enter1.place(x=50,y=70,height=50,width=400)

    label2 = Label(win, text="Correct Spelling", font=("Time New Roman", 20, "bold"), bg="Green", fg="White")
    label2.place(x=50, y=150, height=50, width=220)

    enter2 = Entry(win, font=("Time New Roman", 16))
    enter2.place(x=50, y=200, height=50, width=400)

    button = Button(win,text="Done",font=("Time New Roman", 18, "bold"), bg="Pink",command=correct_spe)
    button.place(x=150,y=280,height=50,width=200)

    win.mainloop()

main_window()