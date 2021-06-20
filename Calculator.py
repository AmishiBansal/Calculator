from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
    else:
        scvalue.set(scvalue.get()+text)

root = Tk()
root.title("Calculator")
root.geometry("250x400+300+300")
root.resizable(0,0)
root.wm_iconbitmap("calculator.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,font=("Helvetica 20"), textvar = scvalue)
screen.pack()

#Frames
btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")

#Row 1 buttons
btn1 = Button(btnrow1, text="7", font="Helvetica 20", relief=GROOVE, border=0)
btn1.bind("<Button-1>",click)
btn1.pack(side = LEFT,expand=True,fill="both")

btn2 = Button(btnrow1, text="8", font="Helvetica 20", relief=GROOVE, border=0)
btn2.bind("<Button-1>",click)
btn2.pack(side = LEFT,expand=True,fill="both")

btn3 = Button(btnrow1, text="9", font="Helvetica 20", relief=GROOVE, border=0)
btn3.bind("<Button-1>",click)
btn3.pack(side = LEFT,expand=True,fill="both")

btn4 = Button(btnrow1, text="/", font="Helvetica 20", relief=GROOVE, border=0)
btn4.bind("<Button-1>",click)
btn4.pack(side = LEFT,expand=True,fill="both")

#Row 2 buttons
btn1 = Button(btnrow2, text="4", font="Helvetica 20", relief=GROOVE, border=0)
btn1.bind("<Button-1>",click)
btn1.pack(side = LEFT,expand=True,fill="both")

btn2 = Button(btnrow2, text="5", font="Helvetica 20", relief=GROOVE, border=0)
btn2.bind("<Button-1>",click)
btn2.pack(side = LEFT,expand=True,fill="both")

btn3 = Button(btnrow2, text="6", font="Helvetica 20", relief=GROOVE, border=0)
btn3.bind("<Button-1>",click)
btn3.pack(side = LEFT,expand=True,fill="both")

btn4 = Button(btnrow2, text="*", font="Helvetica 20", relief=GROOVE, border=0)
btn4.bind("<Button-1>",click)
btn4.pack(side = LEFT,expand=True,fill="both")

#Row 3 buttons
btn1 = Button(btnrow3, text="1", font="Helvetica 20", relief=GROOVE, border=0)
btn1.bind("<Button-1>",click)
btn1.pack(side = LEFT,expand=True,fill="both")

btn2 = Button(btnrow3, text="2", font="Helvetica 20", relief=GROOVE, border=0)
btn2.bind("<Button-1>",click)
btn2.pack(side = LEFT,expand=True,fill="both")

btn3 = Button(btnrow3, text="3", font="Helvetica 20", relief=GROOVE, border=0)
btn3.bind("<Button-1>",click)
btn3.pack(side = LEFT,expand=True,fill="both")

btn4 = Button(btnrow3, text="-", font="Helvetica 20", relief=GROOVE, border=0)
btn4.bind("<Button-1>",click)
btn4.pack(side = LEFT,expand=True,fill="both")

#Row 4 buttons
btn1 = Button(btnrow4, text="C", font="Helvetica 20", relief=GROOVE, border=0)
btn1.bind("<Button-1>",click)
btn1.pack(side = LEFT,expand=True,fill="both")

btn2 = Button(btnrow4, text="0", font="Helvetica 20", relief=GROOVE, border=0)
btn2.bind("<Button-1>",click)
btn2.pack(side = LEFT,expand=True,fill="both")

btn3 = Button(btnrow4, text=".", font="Helvetica 20", relief=GROOVE, border=0)
btn3.bind("<Button-1>",click)
btn3.pack(side = LEFT,expand=True,fill="both")

btn4 = Button(btnrow4, text="=", font="Helvetica 20", relief=GROOVE, border=0)
btn4.bind("<Button-1>",click)
btn4.pack(side = LEFT,expand=True,fill="both")

root.mainloop()
