import tkinter
canvas = tkinter.Canvas(bg = "#89CFF0", width = 800, height = 500)
canvas.pack()
canvas.create_text(400, 25, text = "Hore", fill = "#FF1964", font = "Nevrada 30 italic")
canvas.create_text(400, 250, text = "Stred", fill = "#0A6522", font = "Nevrada 40 bold")
canvas.create_text(400, 475, text = "Dole", fill = "#FF1964", font = "Nevrada 30 italic")
canvas.create_text(65, 250, text = "Vľavo", fill = "#FF1964", font = "Nevrada 30 italic")
canvas.create_text(735, 250, text = "Vpravo", fill = "#FF1964", font = "Nevrada 30 italic")
