from tkinter import *
import tkinter as ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import csv

Expenses = []
special_symbols = "!@#$%&*()"


def add_expensive():
    name = entry_name.get()
    amount = int(entry_amount.get())
    category = entry_category.get()

    if not (name and amount and category):
        messagebox.showerror("Error", "Please fill in all fields")
    else:
        Expenses.append({"name": name, "amount": amount, "category": category})
        messagebox.showinfo("Expenses added", "Expense added successfully!")


def calculate_total():
    summ = 0
    for item in Expenses:
        summ += item["amount"]
    label_total['text'] = "Total Expenses: $" + str(summ)


def view_results():
    listBox_one.delete(0, END)
    for item in Expenses:
        display_res = item["name"] + ": " + "$" + str(item["amount"]) + " (" + item["category"] + ")"
        listBox_one.insert(END, display_res)


def filter_category():
    filter_cat = entry_filter.get()
    listBox_filter.delete(0, END)

    found = False

    for item in Expenses:
        if filter_cat.lower() == item["category"].lower():
            display_filter = item["category"] + "    $" + str(item["amount"])
            listBox_filter.insert(END, display_filter)
            found = True

    if not found:
        messagebox.showerror("Error", "No matching category found")


def display_diagram():
    categories = []
    amounts = []
    for item in Expenses:
        categories.append(item["category"])
        amounts.append(item["amount"])

    plt.figure(figsize=(4, 2))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title('Expense Distribution by Category')
    plt.show()


def export_to_csv():
    filename = entry_export.get()

    if not filename:
        messagebox.showerror("Error", "Please enter a filename")
    elif any(i in special_symbols for i in filename):
        messagebox.showerror("Error", "Filename contains invalid characters")
    else:
        with open(filename + '.csv', mode='w', newline='\n', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Amount", "Category"])

            for item in Expenses:
                writer.writerow([item["name"], item["amount"], item["category"]])

            messagebox.showinfo("Export Complete", "Expenses exported to " + filename + ".csv successfully!")


def exit_program():
    exit()


root = Tk()
root.title("Expense Tracker")
root.geometry("500x680+100+100")

root.minsize(500, 680)
root.maxsize(500, 680)
root.config(background='white')


frame_name_app = ttk.Frame(root, relief='solid', borderwidth=1, background='#9c9c9c')
frame_name_app.pack(side=TOP)

frame_1 = ttk.Frame(root, background='white')
frame_1.pack(side=LEFT, anchor=NW)

frame_2 = ttk.Frame(root, background='white')
frame_2.pack(side=TOP, anchor=NE)

frame_3 = ttk.Frame(root, background='white')
frame_3.pack(side=RIGHT, anchor=SE)

name_app = ttk.Label(frame_name_app, text='Expense Tracker', width=70, height=2,
                     font=('Microsoft YaHei UI Light', 15, 'bold'),
                     background='#57a1f8')
name_app.pack()

button_add_expense = ttk.Button(frame_1, text='Add an Expense', width=15, cursor='hand2', border=3, relief=GROOVE,
                                command=add_expensive)
button_add_expense.pack(padx=5, pady=5)

label_name = ttk.Label(frame_1, text='Enter the name of the expense: ', background='white')
label_name.pack(padx=5, pady=3)

entry_name = ttk.Entry(frame_1, relief=SOLID)
entry_name.pack(padx=5, pady=3)

label_amount = ttk.Label(frame_1, text='Enter the expense amount: (in numbers)', background='white')
label_amount.pack(padx=5, pady=3)

entry_amount = ttk.Entry(frame_1, relief=SOLID)
entry_amount.pack(padx=5, pady=3)

label_category = ttk.Label(frame_1, text='Enter the category of the expense: ', background='white')
label_category.pack(padx=5, pady=3)

entry_category = ttk.Entry(frame_1, relief=SOLID)
entry_category.pack(padx=5, pady=3)

button_total = ttk.Button(frame_1, text='Calculate Total', width=15, font=('Arial', 10), border=3,
                          relief=GROOVE, command=calculate_total)
button_total.pack(padx=5, pady=5)

label_total = ttk.Label(frame_1, text='Total Expenses: ', background='white', font=('Arial', 10, 'bold'))
label_total.pack(padx=5, pady=3)

button_view_res = ttk.Button(frame_2, text='View Expenses', width=15, font=('Arial', 10), border=3,
                             relief=GROOVE, command=view_results)
button_view_res.pack(padx=5, pady=5)

listBox_one = ttk.Listbox(frame_2, relief=SOLID, width=35, height=10)
listBox_one.pack(padx=5, pady=5)

button_filter = ttk.Button(frame_2, text='Filter expenses by category', width=20, font=('Arial', 10), border=3,
                           relief=GROOVE, command=filter_category)
button_filter.pack(padx=5, pady=5)

label_filter = ttk.Label(frame_2, text='Enter the category: ', background='white')
label_filter.pack(padx=5, pady=3)

entry_filter = ttk.Entry(frame_2, relief=SOLID)
entry_filter.pack(padx=5, pady=3)

listBox_filter = ttk.Listbox(frame_2, relief=SOLID, width=35, height=10)
listBox_filter.pack(padx=5, pady=5)

button_diagram = ttk.Button(frame_2, text='Display a diagram', width=20, font=('Arial', 10), border=3,
                            relief=GROOVE, command=display_diagram)
button_diagram.pack(padx=5, pady=5)

button_export = ttk.Button(frame_1, text='Export Expenses to File', width=20, font=('Arial', 10), border=3,
                           relief=GROOVE, command=export_to_csv)
button_export.pack(padx=5, pady=5)

label_export = ttk.Label(frame_1, text='Enter the filename: ', background='white', font=('Arial', 10))
label_export.pack(padx=5, pady=3)

entry_export = ttk.Entry(frame_1, relief=SOLID)
entry_export.pack(padx=5, pady=3)

button_exit = ttk.Button(frame_3, text='Exit', width=13, height=3, font=('Montserrat', 10, 'bold'), relief=SOLID,
                         background='red', foreground='black', activebackground='dark red', command=exit_program)
button_exit.pack(padx=5, pady=5)


root.mainloop()