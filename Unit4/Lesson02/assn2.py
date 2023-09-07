from tkinter import *

root = Tk()
root.title('My Flag')

screen = Canvas(root, width = 400, height =300, bg = "white")
screen.pack()

screen.create_rectangle(0, 0, 400, 300, fill="light blue", outline="")
screen.create_oval(100, 100, 200, 200, fill="beige", outline="black")
screen.create_text(200, 270, text='The new flag for antarctica!')

mainloop()