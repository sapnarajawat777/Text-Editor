import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

BASE_DIR = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(BASE_DIR, "images")

if not os.path.exists(IMAGE_FOLDER):
    messagebox.showerror("Error", "Images folder not found!")
    exit()

images = [
    img for img in os.listdir(IMAGE_FOLDER)
    if img.lower().endswith((".png", ".jpg", ".jpeg"))
]

if not images:
    messagebox.showerror("Error", "No images found!")
    exit()

root = tk.Tk()
root.title("Image Slideshow")
root.geometry("800x500")

label = tk.Label(root)
label.pack(expand=True)

index = 0

def show_image():
    global index
    img_path = os.path.join(IMAGE_FOLDER, images[index])

    img = Image.open(img_path)
    img = img.resize((700, 400))
    photo = ImageTk.PhotoImage(img)

    label.config(image=photo)
    label.image = photo

    index = (index + 1) % len(images)
    root.after(2000, show_image)

show_image()
root.mainloop()
