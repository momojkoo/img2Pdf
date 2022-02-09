# python 3
# makePdf
# Jasuk Koo
# 2020.12.9

import os
import img2pdf

print("Start of makePdf from image files")

img_dir = '.'
with open(img_dir+"\\"+"output.pdf", "wb") as f:
	img_list=[]
	for file in os.listdir(img_dir):
		if file.endswith((".jpg", ".gif", ".png")):
			img_list.append(img_dir+"\\"+file)
	print("  img file count : %d"%len(img_list))
	if not len(img_list) == 0 :
		pdf = img2pdf.convert(img_list)
		f.write(pdf)

print("End of makePdf from image files")
