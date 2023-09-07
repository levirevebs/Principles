from tkinter import*

root = Tk()

screen = Canvas(root, width=700, height=500)
screen.pack()

width = 300
height = 90
top_left_x = 90
top_left_y = 20
bot_right_x = top_left_x + width
bot_right_y = top_left_y + height

screen.create_rectangle(top_left_x, top_left_y, bot_right_x, bot_right_y, fill="salmon", outline="black", width=(5))

width = 100
height = 200
top_left_x = 90
top_left_y = 20
bot_right_x = top_left_x + width
bot_right_y = top_left_y + height

screen.create_rectangle(top_left_x, top_left_y, bot_right_x, bot_right_y, fill="blue", outline="black")

screen.create_arc(300, 300, 200, 200, start="180", extent="270", fill="yellow")

screen.create_oval(202, 202, 90, 100, fill="light blue")

center_x = 400
center_y = 450
radius = 50

screen.create_oval(202, 202, 90, 100, fill="light blue")

screen.create_text(50, 490, text="brand new game!")
screen.create_text(303, 400, text="Click Here To Start!")

mainloop()