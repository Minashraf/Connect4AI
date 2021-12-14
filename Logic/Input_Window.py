from tkinter import *


def popup_box():
    depth = 0
    alpha_beta = False

    def set_depth():
        nonlocal depth
        depth = int(d.get())

    def set_pruning():
        nonlocal alpha_beta
        alpha_beta = True
        destroy()

    def destroy():
        nonlocal depth
        nonlocal alpha_beta
        root.destroy()

    root = Tk()
    root.geometry('800x300+100+200')
    root.title('Connect 4')
    Label(root, text="Enter the depth of tree K: ").pack()
    d = Spinbox(root, from_=0, to=7)
    d.pack()
    Label(root, text='').pack()

    k_button = Button(root, text='Insert K', width=13, height=1, command=set_depth)
    k_button.pack()
    Label(root, text='').pack()
    Label(root, text='').pack()
    frame = Frame(root)
    frame.pack()
    pruning_button = Button(frame, text='α-β pruning', width=25, height=4, fg='green', command=set_pruning)
    pruning_button.pack(side=LEFT)
    no_pruning_button = Button(frame, text='No pruning', width=25, height=4, fg='red', command=destroy)
    no_pruning_button.pack(side=LEFT)
    Label(root, text='').pack()
    Label(root, text='').pack()
    f = Frame(root)
    f.pack()
    root.mainloop()

    return depth, alpha_beta
