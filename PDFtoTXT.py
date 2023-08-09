import PyPDF2

def pdf_to_txt(pdf_path, text_path):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        with open(text_path, "w", encoding='utf-8') as text_file:
            text_file.write(text)
        return True, "PDF converted successfully!"
    except Exception as e:
        return False, f"An error occurred: {e}"

print("PDF TO TXT CONVERTER")
pdf_path = input("Enter the path of the PDF: ")
text_path = input("Enter the path to save the TXT file (e.g., FilePath\\example.txt): ")

success, message = pdf_to_txt(pdf_path, text_path)
if success:
    print(message)
else:
    print(message)
