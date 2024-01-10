import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Create a task entry field
task_entry = tk.Entry(root, width=30,bg='skyblue')
task_entry.pack(pady=10)

# Create an "Add Task" button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Create a task listbox
task_list = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40,bg='pink')
task_list.pack(padx=10, pady=10)

# Create a "Remove Task" button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Start the GUI application
root.mainloop()