import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("User Registration PowerLiner")
window.geometry("400x450")
window.resizable(False, False)

# Application title
title_label = tk.Label(
    window,
    text="Your Information",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=15)

# Name field
name_label = tk.Label(window, text="Full Name:")
name_label.pack()

name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=5)

# Phone number field
phone_label = tk.Label(window, text="Phone Number:")
phone_label.pack()

phone_entry = tk.Entry(window, width=30)
phone_entry.pack(pady=5)

# Age field
age_label = tk.Label(window, text="Age:")
age_label.pack()

age_entry = tk.Entry(window, width=30)
age_entry.pack(pady=5)

# Function to check user information
def check_user():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    age_text = age_entry.get().strip()

    # Check if all fields are filled
    if name == "" or phone == "" or age_text == "":
        messagebox.showwarning(
            "Missing Information",
            "Please fill in all fields."
        )
        return

    # Check if age is a valid integer
    try:
        age = int(age_text)
    except ValueError:
        messagebox.showerror(
            "Invalid Age",
            "Please enter a valid whole number for age."
        )
        return

    # Check if age is negative
    if age < 0:
        messagebox.showerror(
            "Invalid Age",
            "Age cannot be negative."
        )
        return

    # Check legal age requirement
    if age < 18:
        messagebox.showwarning(
            "Access Denied",
            "You are under the legal age. Access denied."
        )
        result_label.config(text="")
        return

    # Display user information
    result = (
        f"Name: {name}\n"
        f"Phone Number: {phone}\n"
        f"Age: {age}"
    )

    result_label.config(text=result)

    # Print information to the console
    print("Name:", name)
    print("Phone Number:", phone)
    print("Age:", age)

# Submit button
submit_button = tk.Button(
    window,
    text="Check",
    command=check_user,
    width=22
)
submit_button.pack(pady=15)

# Label to display the result
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 10),
    justify="left"
)
result_label.pack(pady=5)

# Start the application
window.mainloop()