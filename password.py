import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()

    if complexity == "Simple":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

    password = ''.join(random.choice(characters) for i in range(length))
    password_var.set(password)

def check_strength(password):
    if len(password) < 8:
        strength_var.set("Weak")
        strength_indicator.config(fg="red")
    elif len(password) < 12:
        strength_var.set("Moderate")
        strength_indicator.config(fg="orange")
    else:
        strength_var.set("Strong")
        strength_indicator.config(fg="green")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")  # Set initial window size

# Colors
background_color = "#DFFFBF"  # Greenish background
button_color = "#4CAF50"  # Green button
label_color = "#2E294E"  # Dark purple text color
entry_color = "#E0E0E0"  # Light grey entry background
password_label_color = "#4CAF50"  # Green password text color

root.config(bg=background_color)

length_label = tk.Label(root, text="Password Length:", bg=background_color, fg=label_color)
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root, bg=entry_color)
length_entry.grid(row=0, column=1, padx=10, pady=10)

complexity_var = tk.StringVar()
complexity_var.set("Simple")

# Radio buttons with green colors
simple_radio = tk.Radiobutton(root, text="Simple", variable=complexity_var, value="Simple", bg=background_color, fg=label_color, selectcolor=button_color)
simple_radio.grid(row=1, column=0, padx=10, pady=5)
medium_radio = tk.Radiobutton(root, text="Medium", variable=complexity_var, value="Medium", bg=background_color, fg=label_color, selectcolor=button_color)
medium_radio.grid(row=1, column=1, padx=10, pady=5)
complex_radio = tk.Radiobutton(root, text="Complex", variable=complexity_var, value="Complex", bg=background_color, fg=label_color, selectcolor=button_color)
complex_radio.grid(row=1, column=2, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg=button_color, fg="white")
generate_button.grid(row=2, columnspan=3, padx=10, pady=10)

password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=('Arial', 12), wraplength=300, bg=background_color, fg=password_label_color)
password_label.grid(row=3, columnspan=3, padx=10, pady=10)

strength_label = tk.Label(root, text="Password Strength:", font=('Arial', 12), bg=background_color, fg=label_color)
strength_label.grid(row=4, column=0, padx=10, pady=5)
strength_var = tk.StringVar()
strength_var.set("Weak")
strength_indicator = tk.Label(root, textvariable=strength_var, font=('Arial', 12), fg="red", bg=background_color)
strength_indicator.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

password_var.trace_add("write", lambda name, index, mode: check_strength(password_var.get()))

root.mainloop()
