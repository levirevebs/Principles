from tkinter import *

root = Tk()

r ="#d62b18"
b ="#876f16"
s ="#fa9644"
g = "#6185f8" #background
l =  "#000000" #black
e = "#e1c699"
gr = "#17b217" #green
clear_color = "#4d2d44"
pixel_size = 20

small_mario = [
    [g, g, g, r, r, r, r, r, r, g, g, g, g, g, g, g],
    [g, g, r, r, r, r, r, r, r, r, r, r, g, g, g, g],
    [g, g, b, b, b, s, s, b, s, g, g, g, g, g, g, g],
    [g, b, s, b, s, s, s, b, s, s, s, g, g, g, g, g],
    [g, b, s, b, b, s, s, s, b, s, s, s, g, g, g, g],
    [g, g, b, s, s, s, s, b, b, b, b, g, g, g, g, g],
    [g, g, g, s, s, s, s, s, s, g, g, g, g, g, g, g],
    [g, g, b, b, r, b, b, r, b, b, g, g, g, g, g, g],
    [g, b, b, b, r, b, b, r, b, b, b, g, g, g, g, g],
    [b, b, b, b, r, b, b, r, b, b, b, b, g, g, g, g],
    [s, s, b, r, s ,r, r, s, r, b, s, s, g, g, g, g],
    [s, s, s, r, r, r, r, r, r, s, s, s, g, g, g, g],
    [s, s, r, r, r, r, r, r, r, r, s, s, g, g, g, g],
    [g, g, r, r, r, g, g, r, r, r, g, g, g, g, g, g],
    [g, b, b, b, g, g, g, g, b, b, b, g, g, g, g, g],
    [b, b, b, b, g, g, g, g, b, b, b, b, g, g, g, g]
]
    
goomba = [
    [g, g, g, g, g, g, b, b, b, b, g, g, g, g, g, g],
    [g, g, g, g, g, b, b, b, b, b, b, g, g, g, g, g],
    [g, g, g, g, b, b, b, b, b, b, b, b, g, g, g, g],
    [g, g, g, b, b, b, b, b, b, b, b, b, b, g, g, g],
    [g, g, b, l, l, b, b, b, b, b, b, l, l, b, g, g],
    [g, b, b, b, e, l, b, b, b, b, l, e, b, b, b, g],
    [g, b, b, b, e, l, l, l, l, l, l, e, b, b, b, g],
    [b, b, b, b, e, l, e, b, b, e, l, e, b, b, b, b],
    [b, b, b, b, e, e, e, b, b, e, e, e, b, b, b, b],
    [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
    [g, b, b, b, b, e, e, e, e, e, e, b, b, b, b, g],
    [g, g, g, g, e, e, e, e, e, e, e, e, g, g, g, g],
    [g, g, g, g, e, e, e, e, e, e, e, e, l, l, g, g],
    [g, g, g, l, l, e, e, e, e, e, l, l, l, l, l, g],
    [g, g, g, l, l, l, e, e, e, l, l, l, l, l, l, g],
    [g, g, g, g, l, l, l, g, g, l, l, l, l, l, g, g]
]

big_mario = [
    [g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g, g],
    [g, g, g, g, g, g, g, r, r, r, r, r, g, g, g, g, g, g],
    [g, g, g, g, g, r, r, r, r, r, r, s, g, g, g, g, g, g],
    [g, g, g, g, r, r, r, r, r, r, s, s, g, g, g, g, g, g],
    [g, g, g, g, r, r, r, r, r, r, r, r, r, r, r, g, g, g],
    [g, g, g, g, b, b, b, s, s, b, s, s, s, g, g, g, g, g],
    [g, g, g, b, s, s, b, s, s, b, b, s, s, s, s, g, g, g],
    [g, g, g, b, s, s, b, b, s, s, s, s, s, s, s, s, g, g],
    [g, g, b, b, s, s, b, b, s, s, s, b, s, s, s, s, g, g],
    [g, g, b, b, s, s, s, s, s, b, b, b, b, b, b, g, g, g],
    [g, g, b, b, b, s, s, s, s, s, b, b, b, b, b, g, g, g],
    [g, g, g, g, b, b, s, s, s, s, s, s, s, s, g, g, g, g],
    [g, g, g, g, g, r, s, s, s, s, s, b, g, g, g, g, g, g],
    [g, g, g, g, g, b, r, b, b, b, b, r, b, g, g, g, g, g],
    [g, g, g, g, b, b, r, b, b, b, b, r, b, b, g, g, g, g],
    [g, g, g, b, b, b, r, b, b, b, b, r, b, b, b, g, g, g],
    [g, g, b, b, b, b, r, b, b, b, b, r, b, b, b, b, g, g],
    [g, g, b, b, b, r, r, b, b, b, b, r, r, b, b, b, g, g],
    [g, b, b, b, b, r, r, b, b, b, b, r, r, b, b, b, b, g],
    [g, b, b, b, b, r, r, r, r, r, r, r, r, b, b, b, b, g],
    [g, b, b, b, b, r, s, r, r, r, r, s, r, b, b, b, b, g],
    [g, s, s, s, s, r, r, r, r, r, r, r, r, s, s, s, s, g],
    [g, s, s, s, s, r, r, r, r, r, r, r, r, s, s, s, s, g],
    [g, g, s, s, s, r, r, r, r, r, r, r, r, s, s, s, g, g],
    [g, g, s, s, r, r, r, r, r, r, r, r, r, r, s, s, g, g],
    [g, g, g, r, r, r, r, r, r, r, r, r, r, r, r, g, g, g],
    [g, g, r, r, r, r, r, r, g, g, r, r, r, r, r, r, g, g],
    [g, g, r, r, r, r, r, g, g, g, g, r, r, r, r, r, g, g],
    [g, g, r, r, r, r, r, g, g, g, g, r, r, r, r, r, g, g],
    [g, g, g, b, b, b, b, g, g, g, g, b, b, b, b, g, g, g],
    [g, g, g, b, b, b, b, g, g, g, g, b, b, b, b, g, g, g],
    [g, b, b, b, b, b, b, g, g, g, g, b, b, b, b, b, b, g],
    [g, b, b, b, b, b, b, g, g, g, g, b, b, b, b, b, b, g],
]

peach = [
    []
]

bowser = [
    []
]

screen = Canvas(root, width=320, height=320, bg="#4d2d44")
screen.pack()

current_sprite = small_mario
current_sprite_name = "Small Mario"

options = [
    "Small Mario",
    "Big Mario",
    "Goomba",
    "Princess Peach",
    "Bowser"
]

clicked = StringVar()
clicked.set("Small Mario")

dropDown = OptionMenu(root, clicked, *options)
dropDown.pack()

def draw_rectangle(x, y, width, height, color='#000000'):
    ending_x = x + width
    ending_y = y + height
    screen.create_rectangle(x, y, ending_x, ending_y, fill=color)

def draw_sprite(sprite):
    current_sprite = sprite
    x = 0
    y = 0
    height_in_pixels = len(sprite)
    width_in_pixels = len(sprite[0])
    height = height_in_pixels * pixel_size
    width = width_in_pixels * pixel_size
    screen.config(width=width, height=height)

    for row in sprite:
        for color in row:
            draw_rectangle(x, y, pixel_size, pixel_size, color)
            x += pixel_size
        x = 0
        y += pixel_size

def clear():
   screen.delete("all")

def draw():
    clear()
    current_selection = clicked.get()
    current_sprite_name = current_selection
    if current_selection == "Small Mario":
        draw_sprite(small_mario)
    elif current_selection == "Goomba":
        draw_sprite(goomba)
    elif current_selection == "Big Mario":
        draw_sprite(big_mario)
    elif current_selection == "Princess Peach":
        draw_sprite(peach)
    elif current_selection == "Bowser":
        draw_sprite(bowser)

def luigi():

    pass

def fire():

    pass

draw_button = Button(root, text="Draw Sprite", command=draw)
draw_button.pack()

clear_button = Button(root, text="Clear", command=clear)
clear_button.pack()

mainloop()