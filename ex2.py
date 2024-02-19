import tkinter as tk
from tkinter import filedialog
import PyPDF2
import io
import messagebox
import textract

# Create the main window
root = tk.Tk()

# Set the window title
root.title("OCR Sense")

# Set the window icon
root.iconbitmap("icon.ico")

# Define the browse function for selecting PDF file
def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    return file_path

# Define the extract text function for performing OCR
def extract_text():
    try:
        # Get the selected PDF file path
        pdf_path = browse_pdf()

        # Open the PDF file
        pdf_file = open(pdf_path, 'rb')

        # Read the PDF file
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()

        # Perform OCR on the extracted text
        text = textract.process(io.StringIO(text), method='tesseract', language='eng').decode('utf-8')

        # Display the extracted text
        text_box.insert(tk.END, text)

    except Exception as e:
        # Display an error message
        messagebox.showerror("Error", str(e))

# Create the browse button for selecting PDF file
browse_button = tk.Button(root, text="Drag and drop your PDF here or click to browse your device", command=browse_pdf)
browse_button.pack(pady=10)

# Create the extract text button for performing OCR
extract_button = tk.Button(root, text="Extract Text", command=extract_text)
extract_button.pack(pady=10)

# Create the text box for displaying the extracted text
text_box = tk.Text(root, height=20, width=50)
text_box.pack(pady=10)

# Run the main loop
root.mainloop()