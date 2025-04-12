import PyPDF2

pdf_doc = open("ordinul-MS-nr-119-2014-actualizat-prin-1257-din-aprilie-2023-norme-igiena-mediul-de-viata-al-populatiei-.pdf", "rb")

reader = PyPDF2.PdfReader(pdf_doc)
no_pages = len(reader.pages)

txt_file = open("pdf_in_text.txt", "a", encoding="utf-8")

for p_index in range(no_pages):
    page = reader.pages[p_index]
    text = page.extract_text()
    txt_file.write(text)

pdf_doc.close()
txt_file.close()