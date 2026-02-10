
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# ------------------ MAIN WINDOW ------------------
root = tk.Tk()
root.title("Photo Viewer App")
root.geometry("600x600")
root.resizable(False, False)

# ------------------ IMAGE FOLDER ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_FOLDER = os.path.join(BASE_DIR, "images")

if not os.path.exists(IMAGE_FOLDER):
    messagebox.showerror("Error", "Images folder not found")
    root.destroy()

image_files = [
    f for f in os.listdir(IMAGE_FOLDER)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
]

if not image_files:
    messagebox.showerror("Error", "No images found in folder")
    root.destroy()

# ------------------ VARIABLES ------------------
index = 0
autoplay = False

# ------------------ LOAD IMAGE FUNCTION ------------------
def load_image():
    global photo
    img_path = os.path.join(IMAGE_FOLDER, image_files[index])
    img = Image.open(img_path)
    img = img.resize((450, 350))
    photo = ImageTk.PhotoImage(img)

    image_label.config(image=photo)
    counter_label.config(text=f"{index + 1} / {len(image_files)}")

# ------------------ BUTTON FUNCTIONS ------------------
def next_image(event=None):
    global index
    index = (index + 1) % len(image_files)
    load_image()

def prev_image(event=None):
    global index
    index = (index - 1) % len(image_files)
    load_image()

def toggle_autoplay():
    global autoplay
    autoplay = not autoplay
    autoplay_btn.config(text="Stop Auto Play" if autoplay else "Auto Play")
    if autoplay:
        auto_play()

def auto_play():
    if autoplay:
        next_image()
        root.after(2000, auto_play)

# ------------------ UI ELEMENTS ------------------
image_label = tk.Label(root)
image_label.pack(pady=20)

counter_label = tk.Label(root, text="", font=("Arial", 12))
counter_label.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

prev_btn = tk.Button(btn_frame, text="◀ Previous", width=12, command=prev_image)
prev_btn.grid(row=0, column=0, padx=10)

autoplay_btn = tk.Button(btn_frame, text="Auto Play", width=12, command=toggle_autoplay)
autoplay_btn.grid(row=0, column=1, padx=10)

next_btn = tk.Button(btn_frame, text="Next ▶", width=12, command=next_image)
next_btn.grid(row=0, column=2, padx=10)

# Keyboard support
root.bind("<Left>", prev_image)
root.bind("<Right>", next_image)

# Load first image
load_image()

root.mainloop()
