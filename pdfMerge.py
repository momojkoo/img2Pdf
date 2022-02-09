# python 3
# makePdf
# Jasuk Koo
# 2020.12.9

# REMARK
# There is a korean encoding problem in PyPDF2
# following below, you can resolve this problem.
# PyPDF2/generic.py
#     line 484 : utf-8 --> CP949
# PyPDF2/utils.py
#     line 238 : latin-1 --> utf-8

import os
from PyPDF2 import PdfFileMerger, PdfFileReader

print("Start of pdfMerge")
mergedObject = PdfFileMerger()

if os.path.exists("merged.pdf"):
    print("merged.pdf is removed")
    os.remove("merged.pdf")

pdf_dir = '.'
for file in os.listdir(pdf_dir):
    if file.endswith((".pdf")):
        print("  "+file)
        print(PdfFileReader(open(pdf_dir+"\\"+file, 'rb')).getDocumentInfo())
        mergedObject.append(PdfFileReader(open(pdf_dir+"\\"+file, 'rb')))
print("gogo")
try:
    mergedObject.write("merged.pdf")
except UnicodeDecodeError:
    pass

print("End of pdfMerge")
