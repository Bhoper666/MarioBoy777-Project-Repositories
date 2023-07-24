import tkinter as tk
import math

def on_click(btn_text):
    current = display_var.get()
    if btn_text == "=":
        try:
            result = eval(current)
            display_var.set(str(result))
        except Exception as e:
            display_var.set("Error")
    elif btn_text == "C":
        display_var.set("")
    else:
        display_var.set(current + btn_text)

def square_root():
    current = display_var.get()
    try:
        result = math.sqrt(float(current))
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")

def sine():
    current = display_var.get()
    try:
        result = math.sin(math.radians(float(current)))
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")

def cosine():
    current = display_var.get()
    try:
        result = math.cos(math.radians(float(current)))
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")

def tangent():
    current = display_var.get()
    try:
        result = math.tan(math.radians(float(current)))
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("300x400")

display_var = tk.StringVar()

display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), justify="right")
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("√", 5, 1), ("sin", 5, 2), ("cos", 5, 3), ("tan", 5, 4)
]

for btn_text, row, col in buttons:
    btn = tk.Button(root, text=btn_text, font=("Arial", 20), command=lambda text=btn_text: on_click(text))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Additional scientific functions
sqrt_btn = tk.Button(root, text="√", font=("Arial", 20), command=square_root)
sqrt_btn.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")

sin_btn = tk.Button(root, text="sin", font=("Arial", 20), command=sine)
sin_btn.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")

cos_btn = tk.Button(root, text="cos", font=("Arial", 20), command=cosine)
cos_btn.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

tan_btn = tk.Button(root, text="tan", font=("Arial", 20), command=tangent)
tan_btn.grid(row=5, column=4, padx=5, pady=5, sticky="nsew")

for i in range(5):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

root.mainloop()
