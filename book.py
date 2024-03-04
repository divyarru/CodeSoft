import tkinter as tk
from tkinter import messagebox

# Sample data structure to hold contacts
contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({'Name': name, 'Phone': phone, 'Email': email, 'Address': address})
        messagebox.showinfo("Success", "Contact added successfully")
        clear_fields()
    else:
        messagebox.showerror("Error", "Name and Phone number are required")

def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

def search_contact():
    search_term = search_entry.get().lower()
    results = [contact for contact in contacts if search_term in contact['Name'].lower() or search_term in contact['Phone']]
    contact_list.delete(0, tk.END)
    for result in results:
        contact_list.insert(tk.END, f"{result['Name']} - {result['Phone']}")

def update_contact():
    selected_contact_index = contact_list.curselection()
    if selected_contact_index:
        selected_contact = contacts[selected_contact_index[0]]
        selected_contact['Name'] = name_entry.get()
        selected_contact['Phone'] = phone_entry.get()
        selected_contact['Email'] = email_entry.get()
        selected_contact['Address'] = address_entry.get()
        messagebox.showinfo("Success", "Contact updated successfully")
        view_contacts()
    else:
        messagebox.showerror("Error", "No contact selected")

def delete_contact():
    selected_contact_index = contact_list.curselection()
    if selected_contact_index:
        contacts.pop(selected_contact_index[0])
        messagebox.showinfo("Success", "Contact deleted successfully")
        view_contacts()
    else:
        messagebox.showerror("Error", "No contact selected")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Contact Manager")

# Cinematic Light Colors
background_color = "#f2f2f2"  # Light Gray
button_color = "#4CAF50"  # Green
label_color = "#333333"  # Dark Gray
result_label_color = "#cc0000"  # Cinematic Red
entry_color = "#ffffff"  # White

root.config(bg=background_color)

# Create labels
tk.Label(root, text="Name:", font=('Arial', 12), bg=background_color, fg=label_color).grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="Phone:", font=('Arial', 12), bg=background_color, fg=label_color).grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="Email:", font=('Arial', 12), bg=background_color, fg=label_color).grid(row=2, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="Address:", font=('Arial', 12), bg=background_color, fg=label_color).grid(row=3, column=0, sticky="w", padx=10, pady=5)

# Create entry fields
name_entry = tk.Entry(root, font=('Arial', 12), bg=entry_color)
name_entry.grid(row=0, column=1, padx=10, pady=5, ipadx=20)
phone_entry = tk.Entry(root, font=('Arial', 12), bg=entry_color)
phone_entry.grid(row=1, column=1, padx=10, pady=5, ipadx=20)
email_entry = tk.Entry(root, font=('Arial', 12), bg=entry_color)
email_entry.grid(row=2, column=1, padx=10, pady=5, ipadx=20)
address_entry = tk.Entry(root, font=('Arial', 12), bg=entry_color)
address_entry.grid(row=3, column=1, padx=10, pady=5, ipadx=20)

# Create buttons
add_button = tk.Button(root, text="Add Contact", font=('Arial', 12), command=add_contact, bg=button_color, fg="white")
add_button.grid(row=4, column=0, pady=5, sticky="ew", columnspan=2)
view_button = tk.Button(root, text="View Contacts", font=('Arial', 12), command=view_contacts, bg=button_color, fg="white")
view_button.grid(row=5, column=0, pady=5, sticky="ew", columnspan=2)
search_entry = tk.Entry(root, font=('Arial', 12), bg=entry_color)
search_entry.grid(row=6, column=0, padx=10, pady=5, ipadx=20, sticky="ew")
search_button = tk.Button(root, text="Search", font=('Arial', 12), command=search_contact, bg=button_color, fg="white")
search_button.grid(row=6, column=1, padx=10, pady=5, sticky="ew", ipadx=20)
update_button = tk.Button(root, text="Update Contact", font=('Arial', 12), command=update_contact, bg=button_color, fg="white")
update_button.grid(row=7, column=0, pady=5, sticky="ew", columnspan=2)
delete_button = tk.Button(root, text="Delete Contact", font=('Arial', 12), command=delete_contact, bg=button_color, fg="white")
delete_button.grid(row=8, column=0, pady=5, sticky="ew", columnspan=2)

# Create contact list
contact_list = tk.Listbox(root, font=('Arial', 12), bg=entry_color)
contact_list.grid(row=9, column=0, padx=10, pady=5, sticky="ew", columnspan=2)

root.mainloop()
