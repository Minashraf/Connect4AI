from tkinter import *

def print_result(ourMessage, color):
    root = Tk()
    root.geometry('300x70+100+200')
    root.title('Connect 4')
    messageVar = Message(root, text=ourMessage)
    messageVar.config(bg=color)
    messageVar.config(width=300)
    messageVar.pack()
    root.mainloop()