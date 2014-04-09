import sys
from Tkinter import *

Tweet = """Latest Tweet

Feeling amazing with my first ever tweet :)"""

Ltweet = """
Last Tweet

Hello all i am now in twitter"""

def clickAbout():
    toplevel = Toplevel()
    label1 = Label(toplevel, text=Tweet, height=0, width=100)
    label1.pack()
    label2 = Label(toplevel, text=Ltweet, height=0, width=100)
    label2.pack()


app = Tk()
app.title("STREAMING TWITTER")
app.geometry("500x300+200+200")

label = Label(app, text="TRENDING TWEETS", height=0, width=100)
b = Button(app, text="Quit", width=20, command=app.destroy)
button1 = Button(app, text="FOLLOWER_Name", width=20, command=clickAbout)
label.pack()
b.pack(side='bottom',padx=0,pady=0)
button1.pack(side='bottom',padx=5,pady=5)

app.mainloop()
