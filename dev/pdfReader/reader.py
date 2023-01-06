# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('jacatra.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(6)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

img = cv2.imread('image.jpg')

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image, 5)


def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#img = get_grayscale(img)
#img = thresholding(img)
#img = remove_noise(img)

cv2.imshow('image', img)
print(ocr_core(img))

cv2.waitKey(0)
 
# closing all open windows
cv2.destroyAllWindows()