import tkinter as tk
import subprocess
import todolist


class TodoList:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
# Define function to start the CLI program
def start_todo():
    subprocess.Popen(["python", "todolist.py"])

# Create a GUI window
window = tk.Tk()
window.title("Todo List")

# Create a frame for the todo list
list_frame = tk.Frame(window)
list_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Create a label for the todo list
list_label = tk.Label(list_frame, text="Todo List", font=("Arial", 14))
list_label.pack(side=tk.TOP)

# Create a text box for the todo list
list_box = tk.Text(list_frame, height=20, width=40)
list_box.pack(side=tk.TOP)

# Create a frame for the buttons
button_frame = tk.Frame(window)
button_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Create a button to add a new item
add_button = tk.Button(button_frame, text="Add", command=start_todo)
add_button.pack(side=tk.TOP, pady=5)

# Create a button to edit an existing item
edit_button = tk.Button(button_frame, text="Edit", command=start_todo)
edit_button.pack(side=tk.TOP, pady=5)

# Create a button to remove an existing item
remove_button = tk.Button(button_frame, text="Remove", command=start_todo)
remove_button.pack(side=tk.TOP, pady=5)

# Create a button to mark an item as completed
complete_button = tk.Button(button_frame, text="Complete", command=start_todo)
complete_button.pack(side=tk.TOP, pady=5)

# Start the GUI event loop
window.mainloop()

