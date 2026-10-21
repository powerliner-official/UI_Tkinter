#python
import tkinter as tk
from tkinter import messagebox

# =========================
# Main Window
# =========================

window = tk.Tk()
window.title("PowerLiner")
window.geometry("1200x750")
window.configure(bg="#2D3250")
window.resizable(False, False)

# =========================
# Right Sidebar
# =========================

sidebar = tk.Frame(
    window,
    bg="#1B2038",
    width=270
)
sidebar.pack(side="right", fill="y")
sidebar.pack_propagate(False)

# Brand
tk.Label(
    sidebar,
    text="PowerLiner",
    font=("Arial", 25, "bold"),
    bg="#1B2038",
    fg="white"
).pack(pady=(35, 5))

tk.Label(
    sidebar,
    text="Industrial Automation",
    font=("Arial", 10),
    bg="#1B2038",
    fg="#8DA9DB"
).pack(pady=(0, 35))

tk.Label(
    sidebar,
    text="MAIN MENU",
    font=("Arial", 10, "bold"),
    bg="#1B2038",
    fg="#8DA9DB",
    anchor="w"
).pack(fill="x", padx=20, pady=10)


def create_menu_button(text):
    button = tk.Button(
        sidebar,
        text=text,
        font=("Arial", 12),
        bg="#1B2038",
        fg="white",
        activebackground="#4A90E2",
        activeforeground="white",
        relief="flat",
        bd=0,
        anchor="w",
        padx=20,
        pady=12,
        cursor="hand2"
    )
    button.pack(fill="x", padx=10, pady=3)
    return button


create_menu_button("  Home")
create_menu_button("  About PowerLiner")
create_menu_button("  Services")
create_menu_button("  Training Courses")
create_menu_button("  Projects")
create_menu_button("  Contact Us")
create_menu_button("  Settings")

tk.Label(
    sidebar,
    text="PowerLiner | Version 1.0",
    font=("Arial", 9),
    bg="#1B2038",
    fg="#7D89A8"
).pack(side="bottom", pady=20)

# =========================
# Main Application Area
# =========================

main_area = tk.Frame(
    window,
    bg="#2D3250"
)
main_area.pack(side="left", fill="both", expand=True)

# Title
tk.Label(
    main_area,
    text="Your Information",
    bg="#2D3250",
    fg="white",
    font=("Arial", 30, "bold")
).pack(pady=(35, 25))

# Name
tk.Label(
    main_area,
    text="Name:",
    bg="#2D3250",
    fg="white",
    font=("Arial", 15, "bold")
).pack()

name_entry = tk.Entry(
    main_area,
    font=("Arial", 13),
    width=40
)
name_entry.pack(pady=(5, 15), ipady=5)

# Phone Number
tk.Label(
    main_area,
    text="Phone Number:",
    bg="#2D3250",
    fg="white",
    font=("Arial", 15, "bold")
).pack()

phone_entry = tk.Entry(
    main_area,
    font=("Arial", 13),
    width=40
)
phone_entry.pack(pady=(5, 15), ipady=5)

# Age
tk.Label(
    main_area,
    text="Age:",
    bg="#2D3250",
    fg="white",
    font=("Arial", 15, "bold")
).pack()

age_entry = tk.Entry(
    main_area,
    font=("Arial", 13),
    width=40
)
age_entry.pack(pady=(5, 20), ipady=5)

# Result
result_label = tk.Label(
    main_area,
    text="",
    font=("Arial", 12, "bold"),
    bg="#2D3250",
    fg="#FFFFFF",
    justify="left"
)
result_label.pack(pady=10)


# =========================
# Registration Function
# =========================

def check_user():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    age_text = age_entry.get().strip()

    if not name or not phone or not age_text:
        messagebox.showwarning(
            "Missing Information",
            "Please fill in all fields."
        )
        return

    try:
        age = int(age_text)
    except ValueError:
        messagebox.showerror(
            "Invalid Age",
            "Please enter a valid whole number for age."
        )
        return

    if age < 0:
        messagebox.showerror(
            "Invalid Age",
            "Age cannot be negative."
        )
        return

    if age < 18:
        messagebox.showwarning(
            "Access Denied",
            "You must be at least 18 years old to continue."
        )
        result_label.config(text="")
        return

    result = (
        f"Name: {name}\n"
        f"Phone Number: {phone}\n"
        f"Age: {age}"
    )

    result_label.config(text=result)

    print("Name:", name)
    print("Phone Number:", phone)
    print("Age:", age)


# Submit Button
tk.Button(
    main_area,
    text="Check",
    command=check_user,
    font=("Arial", 13, "bold"),
    bg="#4A90E2",
    fg="white",
    activebackground="#357ABD",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=20,
    pady=8
).pack(pady=10)

# =========================
# Run Application
# =========================

window.mainloop()
