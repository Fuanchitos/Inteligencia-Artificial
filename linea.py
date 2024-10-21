import tkinter as tk
from PIL import Image

def dibuja_pixel(canvas, x, y, color):
    canvas.create_line(x, y, x + 1, y, fill=color)

def lineaD(x1, y1, x2, y2, color):
    
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))

    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1
    for _ in range(steps + 1):
        dibuja_pixel(canvas, round(x), round(y), color)
        x += x_increment
        y += y_increment

# Tkinter Ventana
root = tk.Tk()
root.title("Pixel Drawing")

# Tama;o de la linea
width, height = 100, 100
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

# Se dibuja la linea
lineaD(10, 10, 90, 90, "black")

# Para iniciar
root.mainloop()
