#vared kardan ketab khane ha
import cv2 
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output
from docx import Document
from PIL import Image
import os
from functions import *
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#import vorodi
image = cv2.imread(r'C:\Users\SONY\Desktop\Programming\Helli3-Project\example\windmill-rotated-90deg.jpg')
#image_name = "test.txt"
# file=open(image_name,"w")
image = Rotate(image)
results = pytesseract.image_to_data(image,output_type=Output.DICT)
#word detection:
for i in range(0, len(results["text"])):
   x = results["left"][i]
   y = results["top"][i]

   w = results["width"][i]
   h = results["height"][i]

   text = results["text"][i]
   conf = int(results["conf"][i])

   if conf > 70:
       text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
       cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
       #cv2.putText(image, text, (x, y - 10), #neveshtan natije roye aks
#cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2) #marbot be code bala!



cv2.imshow('test',image)
cv2.waitKey()

# file.close()

#input_file = r'C:\Users\SONY\Desktop\Programming\Helli3-Project\test.txt'
# output_file = 'output.docx'
# convert_text_to_word(input_file, output_file)
