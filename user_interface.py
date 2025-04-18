import tkinter as tk
from tkinter import *
from tkinter import ttk

class UserInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora inteligente")
        self.geometry("400x300")

        # grid configuration
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

def savePosn(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    canvas.create_line((lastx, lasty, event.x, event.y))
    savePosn(event)

def clear_canvas():
    canvas.delete("all")

# Window config
root = Tk()
root.title("Calculadora inteligente")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame = Frame(root)
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

# Canvas config
canvas = Canvas(main_frame, background="white", width=400, height=300)
canvas.grid(row=0, column=0, columnspan=2, sticky=(N, W, E, S))
canvas.bind("<Button-1>", savePosn)
canvas.bind("<B1-Motion>", addLine)

def update_result_label(text):
    result_label.config(text=text)

# Action buttons
clear_button = Button(main_frame, text="Borrar", command=clear_canvas)
clear_button.grid(row=1, column=0, sticky=(W, E))

 # Button for calculating, actions undefined because of the lack of other processes such as opencv and pytorch
calculate_button = Button(
    main_frame,
    text="Calcular",
    command=lambda: update_result_label("Tu resultado es: [en proceso]"),
)
calculate_button.grid(row=1, column=1, sticky=(W, E))

# Label for printing the results of the calculation
result_label = Label(
    main_frame, text="Tu resultado es: [en proceso]", background="white"
)
result_label.grid(row=2, column=0, columnspan=2, sticky=(W, E))

root.mainloop()