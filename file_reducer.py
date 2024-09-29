import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import pymupdf as fitz
from docx import Document
import openpyxl
import os

# Watermark text
watermark_text = "hariespalaniappan_compress_tool"

# Function to add watermark to images
def add_watermark_to_image(image_path, output_path):
    img = Image.open(image_path).convert("RGBA")
    txt = Image.new('RGBA', img.size, (255, 255, 255, 0))  # Transparent background
    font = ImageFont.load_default()  # Use default font

    # Get text size
    draw = ImageDraw.Draw(txt)
    text_width, text_height = draw.textsize(watermark_text, font)

    # Position the watermark at the bottom right corner
    position = (img.width - text_width - 10, img.height - text_height - 10)

    # Draw text on the transparent layer
    draw.text(position, watermark_text, fill=(255, 255, 255, 128), font=font)  # White text with transparency
    watermarked = Image.alpha_composite(img, txt)
    watermarked = watermarked.convert("RGB")  # Convert back to RGB
    watermarked.save(output_path, quality=85)

# Function to compress images with watermark
def compress_image(file_path, output_path):
    add_watermark_to_image(file_path, output_path)
    return os.path.getsize(output_path)

# Function to compress PDFs with watermark
def compress_pdf(file_path, output_path):
    pdf = fitz.open(file_path)
    for page in pdf:
        rect = fitz.Rect(0, 0, page.rect.width, page.rect.height)
        page.insert_text(rect.tl, watermark_text, fontsize=30, color=(0, 0, 0), overlay=True)
    pdf.save(output_path, garbage=4, deflate=True)
    pdf.close()
    return os.path.getsize(output_path)

# Function to add watermark to Word documents
def compress_word(file_path, output_path):
    doc = Document(file_path)
    # Add watermark to each section
    for section in doc.sections:
        header = section.header
        header.text = watermark_text  # Set watermark text as header
    doc.save(output_path)
    return os.path.getsize(output_path)

# Function to add watermark to Excel files
def compress_excel(file_path, output_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    sheet["A1"] = watermark_text  # Add watermark in cell A1
    sheet["A1"].font = openpyxl.styles.Font(size=16, italic=True)
    workbook.save(output_path)
    return os.path.getsize(output_path)

# Function to handle file selection and preview sizes
def select_files():
    file_paths = filedialog.askopenfilenames()
    if not file_paths:
        return

    for file_path in file_paths:
        try:
            original_size = os.path.getsize(file_path)
            original_size_label.config(text=f"Original Size: {original_size / 1024:.2f} KB")
            output_file_name = f"compressed_{watermark_text}_{os.path.basename(file_path)}"
            output_path = os.path.join(os.path.dirname(file_path), output_file_name)

            if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                new_size = compress_image(file_path, output_path)
            elif file_path.lower().endswith('.pdf'):
                new_size = compress_pdf(file_path, output_path)
            elif file_path.lower().endswith('.docx'):
                new_size = compress_word(file_path, output_path)
            elif file_path.lower().endswith('.xlsx'):
                new_size = compress_excel(file_path, output_path)
            else:
                messagebox.showerror("Error", f"Unsupported file format for {file_path}")
                continue

            new_size_label.config(text=f"New Size: {new_size / 1024:.2f} KB")
            messagebox.showinfo("Success", f"File compressed successfully: {output_file_name}\nNew size: {new_size / 1024:.2f} KB")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while processing {file_path}:\n{str(e)}")

# Create GUI
root = tk.Tk()
root.title("Universal File Size Reducer | Haries Palaniappan")
root.geometry("500x300")
root.configure(bg="#f5f5f5")

# Header Frame
header_frame = tk.Frame(root, bg="#4CAF50")
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="File Size Reducer", font=("Helvetica", 16), bg="#4CAF50", fg="white")
header_label.pack(pady=10)

# Content Frame
content_frame = tk.Frame(root, bg="#f5f5f5")
content_frame.pack(pady=20)

# Slider for image quality
quality_scale = tk.Scale(content_frame, from_=1, to=100, orient=tk.HORIZONTAL, label="Reducer Percentage", length=300, bg="#f5f5f5", sliderlength=20)
quality_scale.set(85)  # Default value
quality_scale.pack(pady=10)

# Button to select files
select_btn = tk.Button(content_frame, text="Select Files to Compress", command=select_files, bg="#4CAF50", fg="white", font=("Helvetica", 12))
select_btn.pack(pady=10, padx=20)

# Labels for original and new sizes
original_size_label = tk.Label(content_frame, text="Original Size: N/A", bg="#f5f5f5", font=("Helvetica", 12))
original_size_label.pack(pady=5)

new_size_label = tk.Label(content_frame, text="New Size: N/A", bg="#f5f5f5", font=("Helvetica", 12))
new_size_label.pack(pady=5)

# Run the main loop
root.mainloop()
