import tkinter as tk

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

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Create a variable to hold the display text
display_var = tk.StringVar()

# Create the display widget
display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons for digits and operators
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Create and place the buttons
for btn_text, row, col in buttons:
    btn = tk.Button(root, text=btn_text, font=("Arial", 20), command=lambda text=btn_text: on_click(text))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Set the column and row weights to make the buttons expandable
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)

root.mainloop()
