import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Advanced Text Editor")
root.geometry("900x600")

current_font_size = 18
default_font = "Helvetica"

# ---------------- Text Area ----------------
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=(default_font, current_font_size)
)
text.pack(expand=True, fill=tk.BOTH)

# ---------------- File Functions ----------------
def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Saved", "File saved successfully")

# ---------------- Formatting Functions ----------------
def change_text_color():
    try:
        color = colorchooser.askcolor()[1]
        if color:
            text.tag_add("color", "sel.first", "sel.last")
            text.tag_configure("color", foreground=color)
    except tk.TclError:
        messagebox.showwarning("No Selection", "Please select text first")

def make_bold():
    try:
        text.tag_add("bold", "sel.first", "sel.last")
        text.tag_configure(
            "bold",
            font=(default_font, current_font_size, "bold")
        )
    except tk.TclError:
        messagebox.showwarning("No Selection", "Please select text first")

# ---------------- Font Family Feature ----------------
available_fonts = [
    "Helvetica",
    "Arial",
    "Times New Roman",
    "Courier New",
    "Verdana",
    "Georgia"
]

def change_font_family(font_name):
    try:
        text.tag_add(font_name, "sel.first", "sel.last")
        text.tag_configure(
            font_name,
            font=(font_name, current_font_size)
        )
    except tk.TclError:
        messagebox.showwarning("No Selection", "Please select text first")

# ---------------- Dark Mode ----------------
def dark_mode():
    root.config(bg="#1e1e1e")
    text.config(
        bg="#1e1e1e",
        fg="white",
        insertbackground="white"
    )

# ---------------- Menu Bar ----------------
menu = tk.Menu(root)
root.config(menu=menu)

# File Menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Format Menu
format_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Format", menu=format_menu)

format_menu.add_command(label="Text Color", command=change_text_color)
format_menu.add_command(label="Bold", command=make_bold)

# Font Family Submenu
font_menu = tk.Menu(format_menu, tearoff=0)
format_menu.add_cascade(label="Font Family", menu=font_menu)

for font in available_fonts:
    font_menu.add_command(
        label=font,
        command=lambda f=font: change_font_family(f)
    )

# View Menu
view_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Dark Mode", command=dark_mode)

# ---------------- Run Application ----------------
root.mainloop()
