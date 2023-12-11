from tkinter import *

root = Tk()

r ="#d62b18"
b ="#876f16"
s ="#fa9644"
g = "#6185f8"
l =  "#000000"
e = "#e1c699"
clear_color = "#4d2d44"

start_x = 0
start_y = 0
size = 20

screen = Canvas(root, width=320, height=320, bg="#4d2d44")
screen.pack()

options = [
    "Small Mario",
    "Fire Mario",
    "Big Mario",
    "Goomba"
]

clicked = StringVar()
clicked.set("Small Mario")

dropDown = OptionMenu(root, clicked, *options)
dropDown.pack()

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
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

def draw_rectangle(x, y, width, height, color='#000000'):
    ending_x = x + width
    ending_y = y + height
    screen.create_rectangle(x, y, ending_x, ending_y, fill=color)

def draw_sprite(sprite_data):
    x = start_x
    y = start_y 
    for row in sprite_data:
        for color in row:
            draw_rectangle(x, y, size, size, color)
            x += size
        x = start_x
        y = y + size

def clear():
   screen.delete("all")

def draw():
    clear()
    current_option = clicked.get()
    if current_option == "Small Mario":
        draw_sprite(small_mario)
    elif current_option == "Goomba":
        draw_sprite(goomba)


draw_button = Button(root, text="Draw Sprite", command=draw)
draw_button.pack()

draw_button = Button(root, text="Clear Canvas", command=clear)
draw_button.pack()

mainloop()