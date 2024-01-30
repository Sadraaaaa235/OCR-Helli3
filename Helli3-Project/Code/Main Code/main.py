#vared kardan ketab khane ha
import cv2 
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from docx import Document
from PIL import Image
import os
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


#function convert format rangi az rgb be grayscale
def convert_to_grayscale(rgb_image):
    #print(img.shape) #return the height,width and channels : (386,493,3)
    height, width, channels = image.shape
    gray_image = np.zeros((height, width), dtype=np.uint8) #height:rows width:columns
    for i in range(height):
        for j in range(width):
            pixel = rgb_image[i,j] #image[i,j] => [r,g,b] : [255,255,255]
            weighted_average = 0.0722*pixel[2] + 0.7152*pixel[1] + 0.2126*pixel[0] #return black or white
            gray_image[i,j] = weighted_average
    return gray_image

#functon convert format rang az grayscale be Binary
def Binaryimage(gray_image):
    binimage = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    binimage = list(binimage)
    return binimage[1]


def convert_text_to_word(input_file, output_file):

    with open(input_file, 'r') as file:
        text = file.read()

    document = Document()


    document.add_paragraph(text)

    document.save(output_file)
#import vorodi
image = cv2.imread(r'C:\Users\SONY\Desktop\Programming\Helli3-Project\example\download.png')

image_name = "test.txt"

# file=open(image_name,"w")


text = pytesseract.image_to_string(image)

cv2.imshow('test',convert_to_grayscale(image))


# file.close()

#input_file = r'C:\Users\SONY\Desktop\Programming\Helli3-Project\test.txt'
# output_file = 'output.docx'
# convert_text_to_word(input_file, output_file)
