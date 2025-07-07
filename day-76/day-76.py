#pypdf library
import os

from PyPDF2 import PdfWriter

merger = PdfWriter()
files = [file for file in os.listdir('files') if file.endswith(".pdf")]
print(files)
for pdf in files:
    merger.append(f'files/{pdf}')

merger.write("merged-pdf.pdf")
merger.close()