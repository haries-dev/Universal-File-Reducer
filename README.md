# Universal File Reducer

The Universal File Reducer is a Python-based tool designed to compress images, PDFs, Word documents, and Excel files while adding a watermark for easy identification. This application operates locally, ensuring that your sensitive data remains private and secure, without the need to upload files to online services.

## Key Features

- Local Processing: Maintain privacy by compressing files directly on your machine.
- Multiple File Formats: Supports a variety of file types, including images (PNG, JPG), PDFs, Word documents, and Excel spreadsheets.
- Custom Watermark: Easily add a personalized watermark to your files during compression for identification.
- User-Friendly Interface: A straightforward graphical interface simplifies file selection and compression.

## Changelog

### v1.1
- Removed Licensing Code: Streamlined user experience by eliminating unnecessary license validation.
- Improved Image Processing: Enhanced compression algorithms for better image quality and reduced file size.
- Refined GUI Layout: Optimized graphical interface for easier navigation and file selection.
- Enhanced Error Handling: Added user-friendly messages for unsupported file formats.

### v1.0
- Initial Release: Launched with basic functionality for compressing images, PDFs, Word documents, and Excel files, including watermarking.

## Why Use This Tool?

Unlike online file compressors that may retain copies of your data, Universal File Reducer processes files locally on your machine, making it ideal for handling confidential or private information.

## Screenshots

### File Reducer GUI

![File Reducer GUI](https://github.com/haries-dev/Universal-File-Reducer/blob/main/screenshots/File_Reducer_GUI.png)

### Before Compression

![Before Compression](https://github.com/haries-dev/Universal-File-Reducer/blob/main/screenshots/Before_&_After_Result.png)

### After Compression

![After Compression](https://github.com/haries-dev/Universal-File-Reducer/blob/main/screenshots/File_Reducer_GUI_Result.png)

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/haries-dev/Universal-File-Reducer.git
   cd Universal-File-Reducer
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python file_reducer.py
   ```

4. Use the graphical interface to select files for compression.

## Requirements

- Python 3.x
- Libraries:
  - tkinter (for the graphical interface)
  - Pillow (for image processing)
  - PyMuPDF (for PDF compression)
  - python-docx (for Word document processing)
  - openpyxl (for Excel file processing)

Install the required libraries by running:
```bash
pip install -r requirements.txt
```

## Example Workflow

1. Select an image, PDF, Word document, or Excel file using the tool's interface.
2. The file will be compressed, and a watermark with the text "hariespalaniappan_compress_tool" will be added.
3. The compressed file will be saved with a new name in the same directory as the original file.

## Contribute

If you find this project helpful and would like to support my open-source efforts, consider buying me a coffee: [Buy Me a Coffee](https://buymeacoffee.com/hariespalaniappan).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or feedback, feel free to contact me at [hariespalaniappan@gmail.com].
