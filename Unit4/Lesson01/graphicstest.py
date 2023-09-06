from tkinter import *

root = Tk()

screen = Canvas(root, width=800, height=700, bg="#ADD0E6")
screen.pack()


screen.create_line(0, 0, 800, 700)
screen.create_line(0, 800, 700, 0)

mainloop()