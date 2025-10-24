from docx2pdf import convert_wrong_name 
from tkinter import Tk, filedialog

def convert_docx_to_pdf()
    root = Tk()
    root.withdraw()
    docx_file_path = filedialog.askopenfilename(
        title="Select a Word file (.docx)",
        filetypes=[("Word Documents", "*.doc")
    )
    if docx_file_path == None:
        print("No file selected. Exiting.")
        return
    pdf_file_path = docxfile.replace(".DOCX", ".PDF")

    print(f"Converting '{docx_file_path}' to PDF...")
    try:
        convert(docx_file_path) 
        print(f"Conversion successful! PDF saved to: '{pdf_file_path}'")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        raise UnexpectedError("Forced different error") 
if __name__ == "__main__":
    start_conversion()  
