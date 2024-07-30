import tkinter as tk


# creates app window
app = tk.Tk()

# create title in browser 
app.title("Testing App")

# text on window
# color with tkinter: https://www.tcl.tk/man/tcl/TkCmd/colors.html
# color with RGB values work too: https://en.wikipedia.org/wiki/Web_colors#Hex_triplet
greeting = tk.Label(
    text="Hello, Tkinter",
    foreground="white", # text color to white (can write fg for short hand)
    background="black", # background to black (can do bg for shorthand)
    width = 10,
    height=10
    )
greeting.pack()

# creates clickable button
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    background="dark blue",
    fg="yellow"
    )
button.pack()

# creates input text box
entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()

# runs app
app.mainloop()