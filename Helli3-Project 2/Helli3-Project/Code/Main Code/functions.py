import cv2 
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output
from docx import Document
from PIL import Image
import os
from imutils.perspective import four_point_transform

def convert_to_grayscale(rgb_image):
    #print(img.shape) #return the height,width and channels : (386,493,3)
    height, width, channels = rgb_image.shape
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
def Rotate(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_contour = max(contours, key=cv2.contourArea)
    rect = cv2.minAreaRect(largest_contour)
    angle = rect[-1]
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h))        
    return rotated_image
