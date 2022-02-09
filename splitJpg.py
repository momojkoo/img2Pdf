# python 3
# splitJpg.py
# Jasuk Koo
# 20.12.15

import os
import cv2
#pip install opencv-python
# numpy : version 1.19.3  (1.19.4 has bug)

print("Start of splitJpg")
img_dir = '.'

if not os.path.exists("output"):
    os.makedirs("output")

for file in os.listdir(img_dir):
    if file.endswith((".jpg", ".png")):
        print(file)
        filename, ext = os.path.splitext(file)
        # Read the image
        img = cv2.imread(file)
        # print(img.shape)
        height = img.shape[0]
        width = img.shape[1]

        # Cut the image in half
        width_cutoff = width // 2
        s1 = img[:, :width_cutoff]
        s2 = img[:, width_cutoff:]

        cv2.imwrite("output\\"+filename+"_01"+ext, s1)
        cv2.imwrite("output\\"+filename+"_02"+ext, s2)

print("End of splitJpg")
