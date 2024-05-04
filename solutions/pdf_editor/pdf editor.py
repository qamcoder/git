# from PyPDF2 import PdfWriter
# import os
#
# merger = PdfWriter()
# pdf_list = [file for file in os.listdir() if file.endswith('.pdf')]
#
# for pdf in pdf_list:
#     merger.append(pdf)
#
# merger.write("merged-pdf.pdf")
# merger.close()
from PyPDF2 import PdfWriter, PdfReader
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    with open(pdf, "rb") as file:
        pdf_reader = PdfReader(file)  # This PdfReader object is not used explicitly in code, but it could be
                                      # utilized to perform additional operations on the PDF files, such as
                                      # extracting text
        merger.append(file)

with open("merged-pdf.pdf", "wb") as output_file:
    merger.write(output_file)
