from tkinter import *

root = Tk()
root.title("snowman")

canvas_width = 400
canvas_height = 400
circle_radius = 55
circle_radius2 = 35
circle_radius3 = 20
bottom_diameter = canvas_height/2
middle_diameter = bottom_diameter/2
top_diameter = middle_diameter/2
center_x = canvas_width / 2
center_y = canvas_height / 2

top_left_x = center_x - circle_radius
top_left_y = center_y - circle_radius

bot_right_x = center_x + circle_radius
bot_right_y = center_y + circle_radius

top_left_a = bottom_diameter - circle_radius3
top_left_b = top_diameter - circle_radius3

bot_right_a = bottom_diameter + circle_radius3
bot_right_b = top_diameter + circle_radius3

top_left_c = bottom_diameter - circle_radius2
top_left_d = middle_diameter - circle_radius2

bot_right_c = bottom_diameter + circle_radius2
bot_right_d = middle_diameter + circle_radius2

screen = Canvas(root, width = canvas_width, height = canvas_height, bg = "white")
screen.pack()

screen.create_oval(top_left_a, top_left_b, bot_right_a, bot_right_b, fill="#D3D3D3")

screen.create_oval(top_left_x, top_left_y, bot_right_x, bot_right_y, fill="#D3D3D3")

screen.create_oval(top_left_c, top_left_d, bot_right_c, bot_right_d, fill="#D3D3D3")



mainloop()

'''
This is the best I could do within the class time.
'''