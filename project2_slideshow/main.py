import tkinter as tk
from PIL import Image, ImageTk
import os

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("600x500")

# ---------------- Image Folder ----------------
IMAGE_FOLDER = "images"

image_files = [
    os.path.join(IMAGE_FOLDER, img)
    for img in os.listdir(IMAGE_FOLDER)
    if img.lower().endswith((".png", ".jpg", ".jpeg"))
]

images = []
for file in image_files:
    img = Image.open(file)
    img = img.resize((400, 300), Image.LANCZOS)
    images.append(ImageTk.PhotoImage(img))

# ---------------- Label ----------------
image_label = tk.Label(root)
image_label.pack(pady=20)

index = 0

# ---------------- Slideshow Function ----------------
def start_slideshow():
    global index
    if images:
        image_label.config(image=images[index])
        image_label.image = images[index]
        index = (index + 1) % len(images)
        root.after(2000, start_slideshow)

# ---------------- Button ----------------
play_button = tk.Button(
    root,
    text="Play the Slideshow",
    font=("Arial", 17),
    command=start_slideshow
)
play_button.pack(pady=40)

root.mainloop()
