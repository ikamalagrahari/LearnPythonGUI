import tkinter as tk
from PIL import Image, ImageTk

def display_image(canvas, image_path):
    image = Image.open(image_path)
    photo_image = ImageTk.PhotoImage(image)
    image_item = canvas.create_image(0, 0, image=photo_image, anchor="nw")
    return image_item, photo_image

# Create the main window
root = tk.Tk()

# Create a canvas
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

# Display the image on the canvas
image_path = "C:/Users/Gyandev/Downloads/xlogo.png"  # Replace this with the correct path
image_item, photo_image = display_image(canvas, image_path)

root.mainloop()
