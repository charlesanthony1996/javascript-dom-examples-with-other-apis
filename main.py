import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Simple GUI")

# Create a label widget
label = tk.Label(window, text="Hello, World!")
label.pack()

# Create a button widget
button = tk.Button(window, text="Click me!")
button.pack()

# Run the main loop
window.mainloop()
