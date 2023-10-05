from tkinter import*

root = Tk()

canvas_width = 600
canvas_height = 400
num_circles = 40
diameter = canvas_width / num_circles  
radius = diameter / 2
circle_center_y = canvas_height / 2
worm_color_even = "blue"
worm_color_odd = "yellow"

screen = Canvas(root, width=canvas_width, height=canvas_height)
screen.pack()

for circle in range(num_circles):
    top_x = circle * diameter
    top_y = circle_center_y - radius
    bot_x = (circle + 1) * diameter
    bot_y = circle_center_y + radius
    if circle % 2 == 0:
        screen.create_oval(top_x, top_y, bot_x, bot_y, fill=worm_color_even)
    else:
        screen.create_oval(top_x, top_y, bot_x, bot_y, fill=worm_color_odd)
# screen.create_oval(0 * diameter, 0, (0 + 1) * diameter, diameter) 
# screen.create_oval(1 * diameter, 0, (0 + 2) * diameter, diameter)
# screen.create_oval(2 * diameter, 0, (0 + 3) * diameter, diameter)

mainloop()