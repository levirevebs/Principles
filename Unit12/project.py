from tkinter import *

root = Tk()

r ="#d62b18"
b ="#876f16"
s ="#fa9644"
g = "#6185f8"
clear_color = "#4d2d44"

start_x = 0
start_y = 0
size = 20

screen = Canvas(root, width=320, height=320, bg="#4d2d44")
screen.pack()

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
    x = start_x
    y = start_y 
    for row in range(16):
        for color in range(16):
            draw_rectangle(x, y, size, size, clear_color)
            x += size
        x = start_x
        y = y + size

draw_rectangle(0, 0, 20, 20, r)
draw_sprite(small_mario)


mainloop()