from tkinter import *
from tkinter import messagebox

def add_task():
    new_task = entry_task.get()
    if new_task:
        listbox_tasks.insert(END, new_task)
        entry_task.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def remove_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        listbox_tasks.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Select a task to remove!")

def clear_tasks():
    listbox_tasks.delete(0, END)

root = Tk()
root.title("To-Do List")

frame = Frame(root)
frame.pack(padx=11, pady=11)

listbox_tasks = Listbox(frame, selectmode=SINGLE)
listbox_tasks.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

entry_task = Entry(root, width=30)
entry_task.pack(pady=10)

button_add = Button(root, text="Add Task", command=add_task, fg='blue')
button_add.pack(side=LEFT, padx=5)

button_remove = Button(root, text="Remove Task", command=remove_task, fg='red')
button_remove.pack(side=LEFT, padx=5)

button_clear = Button(root, text="Clear List", command=clear_tasks, fg='black')
button_clear.pack(side=LEFT, padx=5)

root.mainloop()
