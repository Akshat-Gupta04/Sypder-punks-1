from playsound import playsound
from tkinter import*
import pyttsx3
import random2
import winsound
def click():
    playsound("buttonclick.wav")
    return playsound
main=Tk()
main.title("Gaming Console")
main.geometry("1000x800")
main.configure(background="#7ababb")
main.attributes('-fullscreen',True)
pic=PhotoImage(file="gc1.png")
def exit():
    main.destroy()
def page1():
    winsound.PlaySound(None,0)
    g=str(e.get())
    main.destroy()
    def voice():
        proceng=pyttsx3.init('sapi5')
        proceng.setProperty("rate",140)
        proceng.setProperty("volume",100)
        voices=proceng.getProperty('voices')
        proceng.setProperty('voice',voices[1].id)
        proceng.say(f"welcome to world{g}",)
        proceng.runAndWait()
        winsound.PlaySound("t2.wav",winsound.SND_ASYNC + winsound.SND_LOOP)
    w1=Tk()
    w1.geometry("1000x800")
    w1.configure(background="#7ababb")
    pic2=PhotoImage(file="gc1.png")
    lab2=Label(w1,image=pic2,bg="#7ababb")
    lab2.place(x=100,y=50)
    def exit():
        w1.destroy()
    w1.attributes("-fullscreen",True)
    exitt=Button(w1,bitmap="error",command=exit,height=25,width=25)
    exitt.pack(side="bottom",anchor="e")
    w1.after(60,voice)
    w1.mainloop()
winsound.PlaySound("s1.wav",winsound.SND_ASYNC + winsound.SND_LOOP)
lab=Label(main,image=pic,bg="#7ababb")
lab.place(x=100,y=50)
te=Label(main,text=("Enter your name:-"),bg="#7ababb",font=("Arial",24,"bold"),anchor="center",justify="center")
te.place(x=320,y=300)
e = Entry(main,width=35,borderwidth=5,insertbackground="red")
e.place(x=620,y=310)
img=PhotoImage(file="subb.png",)
button1=Button(main,image=img,command=page1,border=0,bg="#7ababb")
button1.place(x=580,y=520)
exitt=Button(main,bitmap="error",command=exit,height=30,width=30,bg="red")
exitt.pack(side="bottom",anchor="e")
main.mainloop()

