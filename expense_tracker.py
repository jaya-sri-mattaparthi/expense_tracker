import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Global list to store expenses
expenses = []

def add_expense():
    try:
        amount = float(amount_entry.get())
        description = description_entry.get()
        category = category_var.get()
        date = datetime.now().strftime("%Y-%m-%d %H:%M")

        if description == "" or category == "":
            raise ValueError("Missing fields")

        expense = {"date": date, "amount": amount, "description": description, "category": category}
        expenses.append(expense)
        update_expense_list()
        update_total()

        # Clear fields
        amount_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid values.")

def update_expense_list():
    expense_listbox.delete(0, tk.END)
    for exp in expenses:
        display = f"{exp['date']} - ₹{exp['amount']:.2f} - {exp['description']} [{exp['category']}]"
        expense_listbox.insert(tk.END, display)

def update_total():
    total = sum(exp["amount"] for exp in expenses)
    total_label.config(text=f"Total: ₹{total:.2f}")

# GUI setup
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x500")
root.resizable(False, False)

# Input fields
tk.Label(root, text="Amount (₹):").pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Description:").pack(pady=5)
description_entry = tk.Entry(root)
description_entry.pack()

tk.Label(root, text="Category:").pack(pady=5)
category_var = tk.StringVar()
category_menu = ttk.Combobox(root, textvariable=category_var)
category_menu['values'] = ("Food", "Transport", "Utilities", "Entertainment", "Other")
category_menu.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)

# Expense list display
tk.Label(root, text="Expenses:").pack(pady=5)
expense_listbox = tk.Listbox(root, width=60)
expense_listbox.pack(pady=5)

# Total label
total_label = tk.Label(root, text="Total: ₹0.00", font=("Arial", 12, "bold"))
total_label.pack(pady=10)

root.mainloop()
