from tkinter import *
root = Tk()
root.title = 'test program'

screen=Canvas(root, width = 200, height = 200, bg = "gray")
screen.pack()

screen.create_line(0, 0, 100, 100, 200, 0)

mainloop()