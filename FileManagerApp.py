import tkinter as tk
from tkinter import filedialog
class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager Dialog")
        self.root.geometry("400x300")

        # Adjust size as needed
        # Set up the background image (if desired)
        # uncomment and replace with appropriate image path
        # image_path = ""C:\Users\Gyandev\Downloads\portfolio-main\images\background.png""
        # background_image = tk.PhotoImage(file=image_path)
        # background_label = tk.Label(root, image=background_image)
        # background_label.place(relwidth=1, relheight=1)
        # Variable to store file location
        self.file_location_var = tk.StringVar()

        # Label to display file manager location
        file_location_label = tk.Label(root, textvariable=self.file_location_var, wraplength=300, bg="lightgray")
        file_location_label.pack(pady=10)

        # Button to open file manager
        click_me_button = tk.Button(root, text="Click Me", command=self.open_file_manager, bg="blue", fg="white")
        click_me_button.pack(pady=10)

    def open_file_manager(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select File")
        self.file_location_var.set(file_path)

        # Replace with your actual backend logic, handling potential errors
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    file_content = f.read()
                    print(f"File content:\n{file_content}")
                # Replace with more elaborate file processing/backend logic
            except FileNotFoundError:
                print("Error: File not found!")
            except PermissionError:
                print("Error: Insufficient permissions to read the file!")
            except Exception as e:
                print(f"Unexpected error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
