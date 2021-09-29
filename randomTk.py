import random
import tkinter

canvas = tkinter.Canvas(bg = "#89CFF0", width = 800, height = 500)
canvas.pack()
for i in range(500):
    farba = random.choice(["#EB96EB", "#AF38EB", "#E05194", "#FF8D85", "#884DFF", "#FAD000"])
    x = random.randint(50, 750)
    y = random.randint(50, 450)
    canvas.create_text(x, y, text = (x, y), fill = farba, font = "Impact 25 bold")
