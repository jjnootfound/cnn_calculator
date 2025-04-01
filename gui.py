import tkinter as tk


window = tk.Tk()
window.title("calculators")
window.geometry("400x400")
window.config(bg="pink")

label = tk.Label(window, text="Ingesa tu operació matemática")
label.pack()
label.config(fg = "purple")
label.config(font=("Ubuntu", 20))

button = tk.Button(window, text="Empezar")
button.pack()
window.mainloop()

myCanvas = tk.Canvas(root, bg="white", height=300, width=300)

coord = 10, 10, 300, 300
arc = myCanvas.create_arc(coord, start=0, extent=150, fill="red")
arv2 = myCanvas.create_arc(coord, start=150, extent=215, fill="green")

myCanvas.pack()

