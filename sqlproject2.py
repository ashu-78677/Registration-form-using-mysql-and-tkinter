import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="oracle",
    database="project"
)
if conn.is_connected():
    print("Successfully connected")

cursor = conn.cursor()

def register():
    name = name_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    gender = gender_var.get()
    country = country_cb.get()
    password = password_entry.get()
    re_password = repassword_entry.get()

    if password != re_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    if name and email and contact and gender and country and password:
        try:
            query = "INSERT INTO user_table (name, email, contact_number, gender, country, password) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (name, email, contact, gender, country, password)
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Success", "Registration successful!")
            clear_entries()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def update():
    name = name_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    gender = gender_var.get()
    country = country_cb.get()
    password = password_entry.get()
    re_password = repassword_entry.get()

    if password != re_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    if name and email and contact and gender and country and password:
        try:
            query = "UPDATE user_table SET name=%s, contact_number=%s, gender=%s, country=%s, password=%s WHERE email=%s"
            values = (name, contact, gender, country, password, email)
            cursor.execute(query, values)
            conn.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Update successful!")
            else:
                messagebox.showwarning("Not Found", "User not found!")
            clear_entries()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def delete():
    email = email_entry.get()
    if email:
        try:
            query = "DELETE FROM user_table WHERE email=%s"
            cursor.execute(query, (email,))
            conn.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "User deleted successfully!")
                clear_entries()
            else:
                messagebox.showwarning("Not Found", "User not found!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
    else:
        messagebox.showwarning("Input Error", "Please enter an email to delete the user!")

def clear_entries():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    repassword_entry.delete(0, tk.END)

scr = tk.Tk()
scr.title("PythonGuides")
scr.geometry("500x550")
frame = tk.Frame(scr, bg="lightgray", bd=5, relief="groove")
frame.pack(padx=20, pady=20, fill="both", expand=True)

# User input fields
tk.Label(frame, text="Enter Name", font=("Arial", 12), bg="lightgray").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Enter Email", font=("Arial", 12), bg="lightgray").grid(row=1, column=0, padx=10, pady=5, sticky="w")
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Contact Number", font=("Arial", 12), bg="lightgray").grid(row=2, column=0, padx=10, pady=5, sticky="w")
contact_entry = tk.Entry(frame, width=30)
contact_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="Select Gender", font=("Arial", 12), bg="lightgray").grid(row=3, column=0, padx=10, pady=5, sticky="w")
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male", bg="lightgray").grid(row=3, column=1, sticky="w")
tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female", bg="lightgray").grid(row=3, column=1, padx=70, sticky="w")
tk.Radiobutton(frame, text="Others", variable=gender_var, value="Others", bg="lightgray").grid(row=3, column=1, padx=150, sticky="w")

tk.Label(frame, text="Select Country", font=("Arial", 12), bg="lightgray").grid(row=4, column=0, padx=10, pady=5, sticky="w")
country_cb = ttk.Combobox(frame, values=["Select","United States", "Canada", "United Kingdom", "India", "Australia"], width=28)
country_cb.grid(row=4, column=1, padx=10, pady=5)
country_cb.set("Select")

tk.Label(frame, text="Enter Password", font=("Arial", 12), bg="lightgray").grid(row=5, column=0, padx=10, pady=5, sticky="w")
password_entry = tk.Entry(frame, width=30, show="*")
password_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(frame, text="Re-Enter Password", font=("Arial", 12), bg="lightgray").grid(row=6, column=0, padx=10, pady=5, sticky="w")
repassword_entry = tk.Entry(frame, width=30, show="*")
repassword_entry.grid(row=6, column=1, padx=10, pady=5)

# Buttons
register_button = tk.Button(frame, text="Register", font=("Arial", 10), command=register)
register_button.grid(row=7, column=0, columnspan=2, padx=2, pady=10)

update_button = tk.Button(frame, text="Update", font=("Arial", 10), command=update)
update_button.grid(row=8, column=0, columnspan=2, padx=2, pady=10)

delete_button = tk.Button(frame, text="Delete", font=("Arial", 10), command=delete)
delete_button.grid(row=9, column=0, columnspan=2, padx=2, pady=10 )

scr.mainloop()
