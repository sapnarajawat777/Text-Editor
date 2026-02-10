import tkinter as tk
from PIL import Image, ImageTk
import os

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("600x500")

# ---------------- Safe Image Path (FIXED) ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_FOLDER = os.path.join(BASE_DIR, "images")

# ---------------- Load Images ----------------
images = []

if not os.path.exists(IMAGE_FOLDER):
    tk.messagebox.showerror(
        "Folder Missing",
        "images folder not found.\nPlease create 'images' folder and add images."
    )
    root.destroy()

else:
    image_files = [
        os.path.join(IMAGE_FOLDER, img)
        for img in os.listdir(IMAGE_FOLDER)
        if img.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    for file in image_files:
        img = Image.open(file)
        img = img.resize((400, 300), Image.LANCZOS)
        images.append(ImageTk.PhotoImage(img))

# ---------------- Label ----------------
image_label = tk.Label(root)
image_label.pack(pady=20)

index = 0

# ---------------- Slideshow Logic ----------------
def start_slideshow():
    global index
    if images:
        image_label.config(image=images[index])
        image_label.image = images[index]
        index = (index + 1) % len(images)
        root.after(2000, start_slideshow)
    else:
        tk.messagebox.showwarning(
            "No Images",
            "No images found in images folder."
        )

# ---------------- Button ----------------
play_button = tk.Button(
    root,
    text="Play Slideshow",
    font=("Arial", 16),
    command=start_slideshow
)
play_button.pack(pady=20)

root.mainloop()

