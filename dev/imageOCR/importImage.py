import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

def importImageFunc():

    if os.path.exists('image.jpg'):
        img = cv2.imread('image.jpg')
        cv2.imshow('image', img)
        return (ocr_core(img))

    else:
        errorMessage = "The file image.jpg can not be found, please add the file to the same directory as this program."
        return errorMessage    


