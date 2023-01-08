import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

def pdfOCRFunc(pageNumber):    

    img = cv2.imread('page-%i.png' % pageNumber)
    cv2.imshow('image', img)

    return ocr_core(img)




