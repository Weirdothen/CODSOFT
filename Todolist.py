import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
TASKS_FILE = "task_list.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(task_list):
    with open(TASKS_FILE, "w") as file:
        json.dump(task_list, file, indent=4)

# Add a new task
def add_new_task():
    new_task = task_entry.get()
    if new_task:
        task_list.append({"task": new_task, "completed": False})
        save_tasks(task_list)
        refresh_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Refresh the task list display
def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for index, task in enumerate(task_list):
        status = "Done" if task["completed"] else "Not Done"
        task_listbox.insert(tk.END, f"{index + 1}. {task['task']} [{status}]")

# Mark a task as complete
def mark_task_complete():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task_list[task_index]["completed"] = True
        save_tasks(task_list)
        refresh_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task.")

# Delete a task
def delete_selected_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task_list.pop(task_index)
        save_tasks(task_list)
        refresh_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task.")

# Update an existing task
def update_existing_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        updated_task = task_entry.get()
        if updated_task:
            task_list[task_index]["task"] = updated_task
            save_tasks(task_list)
            refresh_task_list()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")
    else:
        messagebox.showwarning("Selection Error", "Please select a task.")

# Initialize the main application
app = tk.Tk()
app.title("To-Do List Application")

# Load tasks from file
task_list = load_tasks()

# Create frame for tasks
tasks_frame = tk.Frame(app)
tasks_frame.pack(pady=10)

# Create and pack task listbox
task_listbox = tk.Listbox(tasks_frame, width=50, height=10)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Create and pack scrollbar for task listbox
task_scrollbar = tk.Scrollbar(tasks_frame)
task_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Configure task listbox and scrollbar
task_listbox.config(yscrollcommand=task_scrollbar.set)
task_scrollbar.config(command=task_listbox.yview)

# Create and pack entry for new tasks
task_entry = tk.Entry(app, width=50)
task_entry.pack(pady=10)

# Create frame for buttons
buttons_frame = tk.Frame(app)
buttons_frame.pack(pady=10)

# Add task button
add_button = tk.Button(buttons_frame, text="Add Task", command=add_new_task)
add_button.pack(side=tk.LEFT, padx=5)

# Update task button
update_button = tk.Button(buttons_frame, text="Update Task", command=update_existing_task)
update_button.pack(side=tk.LEFT, padx=5)

# Complete task button
complete_button = tk.Button(buttons_frame, text="Complete Task", command=mark_task_complete)
complete_button.pack(side=tk.LEFT, padx=5)

# Delete task button
delete_button = tk.Button(buttons_frame, text="Delete Task", command=delete_selected_task)
delete_button.pack(side=tk.LEFT, padx=5)

# Refresh task list display
refresh_task_list()

# Run the main loop
app.mainloop()
