from tkinter import *

root = Tk()
root.title('Polish Flag')

screen = Canvas(root, width = 400, height =300, bg = "white")
screen.pack()

screen.create_rectangle(0, 0, 400, 300, fill="white", outline="")
screen.create_rectangle(0, 150, 400, 300, fill="red", outline="")

mainloop()