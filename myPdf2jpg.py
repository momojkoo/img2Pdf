# python 3
# myPdf2jpg
# Jasuk Koo
# 21.1.4

import os
from pdf2jpg import pdf2jpg

print("Start of myPdf2jpg")

pdf_dir = '.'
out_dir = '.'
dpi = 96

pdf_list=[]
for file in os.listdir(pdf_dir):
    if file.endswith((".pdf")):
        pdf_list.append(pdf_dir+"\\"+file)
if not len(pdf_list) == 0 :
    for pdf_file in pdf_list:
        print(pdf_file)
        result = pdf2jpg.convert_pdf2jpg(pdf_file, out_dir, dpi=dpi, pages="ALL")
        # print(result)
print("End of myPdf2jpg")
