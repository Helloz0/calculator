import tkinter as tk
window = tk.Tk()
window.title("My Calculator")
window.geometry("300x400")
display = tk.Entry(window, font=("Arial", 20), justify="right")
display.pack()

button_frame=tk.Frame(window)
button_frame.pack()

def button_click(number):
    display.insert(tk.END,number)

def calculate():
    expression=display.get()
    result=eval(expression)

    display.delete(0, tk.END)
    display.insert(tk.END, result)
    

button = tk.Button(button_frame,
 text="1",
command=lambda:button_click(1),
width=9,
height=4)
button.grid(row=0,column=0)

button = tk.Button(button_frame,
text="2", 
command=lambda:button_click(2),
width=9,
height=4)
button.grid(row=0,column=1)

button = tk.Button(button_frame, 
text="3", 
command=lambda:button_click(3),
width=9,
height=4)
button.grid(row=0,column=2)

button=tk.Button(button_frame,
text="/",
command=lambda:button_click("/"),
width=9,
height=4
)
button.grid(row=0,column=3)

button = tk.Button(button_frame, 
text="4", 
command=lambda:button_click(4),
width=9,
height=4)
button.grid(row=1,column=0)

button = tk.Button(button_frame, 
text="5", 
command=lambda:button_click(5),
width=9,
height=4)
button.grid(row=1,column=1)

button = tk.Button(button_frame, 
text="6", 
command=lambda:button_click(6),
width=9,
height=4)
button.grid(row=1,column=2)

button=tk.Button(button_frame,
text="*",
command=lambda:button_click("*"),
width=9,
height=4
)
button.grid(row=1,column=3)

button = tk.Button(button_frame, 
text="7", 
command=lambda:button_click(7),
width=9,
height=4)
button.grid(row=2,column=0)

button = tk.Button(button_frame, 
text="8", 
command=lambda:button_click(8),
width=9,
height=4)
button.grid(row=2,column=1)

button = tk.Button(button_frame, 
text="9", 
command=lambda:button_click(9),
width=9,
height=4)
button.grid(row=2,column=2)

button=tk.Button(button_frame,
text="-",
command=lambda:button_click("-"),
width=9,
height=4
)
button.grid(row=2,column=3)

button=tk.Button(button_frame,
text="c",
command=lambda:button_click("c"),
width=9,
height=4,
)
button.grid(row=3,column=0)

button=tk.Button(button_frame,
text="0",
command=lambda:button_click("0"),
width=9,
height=4
)
button.grid(row=3,column=1)

button=tk.Button(button_frame,
text="=",
command=calculate,
width=9,
height=4
)
button.grid(row=3, column=2)

button=tk.Button(button_frame,
text="+",
command=lambda:button_click("+"),
width=9,
height=4
)
button.grid(row=3, column=3)

window.mainloop()