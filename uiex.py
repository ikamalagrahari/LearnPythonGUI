import tkinter as tk
from tkinter import filedialog
import os
import xlsxwriter
from PIL import Image, ImageTk

class ImageToExcel:
    def __init__(self, master):
        self.master = master
        master.title("Image to Excel")

        # Create a frame for the upload button and the process button
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        # Create and add the upload button to the frame
        self.upload_button = tk.Button(button_frame, text="Upload your file", command=self.upload_file)
        self.upload_button.grid(row=0, column=0, padx=(0, 10))

        # Create and add the process button to the frame
        self.process_button = tk.Button(button_frame, text="Process!", state="disabled", command=self.process)
        self.process_button.grid(row=0, column=1)

        # Create and add the image label to the master window
        self.image_label = tk.Label(master, text="No image selected")
        self.image_label.pack(pady=10)

        # Create and add the excel label to the master window
        self.excel_label = tk.Label(master, text="")
        self.excel_label.pack(pady=10)

        # Initialize the image_file variable
        self.image_file = None

    def upload_file(self):
        # Open a file dialog and get the selected file path
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])

        if file_path:
            # Update the image label text with the selected file name
            self.image_label.config(text=os.path.basename(file_path))

            # Enable the process button
            self.process_button.config(state="normal")

            # Open and store the selected image
            self.image_file = Image.open(file_path)

            # Display the selected image on the canvas
            self.display_image_on_canvas()

    def process(self):
        # Open a file dialog and get the selected output file path
        output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

        if output_file:
            # Update the excel label text with "Processing..."
            self.excel_label.config(text="Processing...")

            try:
                # Create and add a workbook and worksheet
                workbook = xlsxwriter.Workbook(output_file)
                worksheet = workbook.add_worksheet()

                # Add the image to the worksheet
                worksheet.insert_image(0, 0, image_file=self.image_file, width=500, height=500)
                workbook.close()

                # Update the excel label text with "Successfully saved as <output_file>"
                self.excel_label.config(text=f"Successfully saved as {os.path.basename(output_file)}")

            except Exception as e:
                # Update the excel label text with "Error: <str(e)>"
                self.excel_label.config(text=f"Error: {str(e)}")

    def display_image_on_canvas(self):
        # Resize the image to fit the canvas
        resized_image = self.image_file.resize((500, 500), Image.ANTIALIAS)

        # Convert the image to a Tkinter photo image
        tk_image = ImageTk.PhotoImage(resized_image)

        # Create a new canvas with the same size as the resized image
        self.canvas = tk.Canvas(self.master, width=tk_image.width(), height=tk_image.height())
        self.canvas.pack()

        # Add the image to the


        # Add the image to the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

        # Make sure to keep a reference to the PhotoImage to prevent it from being garbage collected
        self.canvas.image = tk_image

def main():
    root = tk.Tk()
    app = ImageToExcel(root)
    root.mainloop()

if __name__ == "__main__":
    main()


