from tkinter import *

root = Tk()

screen = Canvas(root, width=200, height=200, bg="#FF0000")
screen.pack()

screen.create_line(0, 67, 300, 67)
screen.create_line(0, 134, 300, 134)

screen.create_line(67, 0, 67, 300)
screen.create_line(134, 0, 134, 300)

mainloop()