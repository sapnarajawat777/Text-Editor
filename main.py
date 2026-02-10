# Import required libraries
import tkinter as tk
from tkinter import filedialog, messagebox

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

# ---------------- Text Area ----------------
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 18)
)
text.pack(expand=True, fill=tk.BOTH)

# ---------------- Functions ----------------

# Function 1: Create New File
def new_file():
    text.delete(1.0, tk.END)

# Function 2: Open File
def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

# Function 3: Save File
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Info", "File saved successfully")

# ---------------- Menu Bar ----------------
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# ---------------- Run Application ----------------
root.mainloop()


