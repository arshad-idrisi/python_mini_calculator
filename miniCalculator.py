from tkinter import *

def click(event):
    #print("Hello")
    #pass
    global str
    text = event.widget.cget("text")
    #print(text)
    if text == "=":
        if str.get().isdigit():
            value = int(str.get())
        else:
            value = eval(entr.get())

        str.set(value)
        entr.update()

    elif text == "C":
        str.set("")
        entr.update()
    else:
        str.set(str.get()+ text)
        entr.update()


root = Tk()
root.geometry("300x500")
root.minsize(300, 500)
root.maxsize(300, 500)
root.title("Mini Calculator!!")
root.wm_iconbitmap("")

str = StringVar()
str.set("")

entr = Entry(root, textvariable=str, font="lucida 20 bold")
entr.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="lightgreen")
f.pack()
b = Button(f, text="1", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)

b = Button(f, text="2", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)

b = Button(f, text="3", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)

b = Button(f, text="+", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)


f = Frame(root, bg="lightgreen")
f.pack()
b = Button(f, text="4", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)

b = Button(f, text="5", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)


b = Button(f, text="6", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)

b = Button(f, text="-", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)

f = Frame(root, bg="lightgreen")
f.pack()
b = Button(f, text="7", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)



b = Button(f, text="8", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)

b = Button(f, text="9", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)

b = Button(f, text="*", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)


f = Frame(root, bg="lightgreen")
f.pack()
b = Button(f, text="0", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)

b = Button(f, text="C", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)

b = Button(f, text="=", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)

b = Button(f, text="/", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)

f = Frame(root, bg="lightgreen")
f.pack()
b = Button(f, text=".", font="lucida 20 bold", padx=10, pady=10)
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>",click)

root.mainloop()
