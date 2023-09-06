from tkinter import*
root = Tk()

screen = Canvas(root, width=260, height=260, bg="#00FFF0")
screen.pack()

screen.create_line(50, 200, 50, 20, fill="#FFFFFF", width=8)
screen.create_line(30, 90, 90, 90, fill="#FFFFFF", width=8)
screen.create_line(47, 26, 90, 26, fill="#FFFFFF", width=8)
mainloop()