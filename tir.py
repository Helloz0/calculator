import tkinter as tk
window =tk.Tk()
window.title:("Notepad")
window.geometry("679x345")
display = tk.Entry(window, font=("Arial", 20), justify="left")
display.pack()
window.mainloop()