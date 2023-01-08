from PIL import ImageGrab, Image
import os
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(input):
        text = pytesseract.image_to_string(input)
        return text

def clipboardImageFunc():
          
    if os.path.exists('pil.jpg'):
        os.remove('pil.jpg')

    img = ImageGrab.grabclipboard()
    img.save('pil.jpg')
 
    img = cv2.imread('pil.jpg')

    cv2.imshow('Image on clipboard', img)
    return ocr_core(img)
