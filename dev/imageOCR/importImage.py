import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

def importImageFunc(fileName):

    if os.path.exists(fileName):
        img = cv2.imread(fileName)
        cv2.imshow('image', img)
        return (ocr_core(img))

    else:
        errorMessage = "The image file can not be found, please add the file to the same directory as this program."
        return errorMessage    


