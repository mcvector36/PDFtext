# PDFtext (v1.1)
# Author: MC Vector 36 (Mihai-Cristian Constantin)
# @mcvector36

# Info:
#           This program identifies the text characters from a 'PDF' file
#       in the current location and transposes the identified characters
#       into a text file with the 'TXT' extension.

import fitz  # PyMuPDF
import os

def extrage_text_din_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        text += page.get_text()

    return text

def main():
    # Solicită utilizatorului să introducă numele fișierului PDF
    pdf_filename = input("Introduceți numele fișierului PDF (cu extensia .pdf): ")

    # Verifică dacă fișierul există în directorul curent
    if not os.path.isfile(pdf_filename):
        print(f"Fisierul {pdf_filename} nu există în directorul curent.")
        return

    # Extrage textul din PDF, inclusiv din imagini
    text = extrage_text_din_pdf(pdf_filename)

    # Obține numele fișierului fără extensie
    nume_fisier = os.path.splitext(os.path.basename(pdf_filename))[0]

    # Creează un fișier text cu același nume ca fișierul PDF și salvează textul
    txt_path = f"{nume_fisier}.txt"
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)

    print(f"Textul a fost extras și salvat în {txt_path}")

if __name__ == "__main__":
    main()

