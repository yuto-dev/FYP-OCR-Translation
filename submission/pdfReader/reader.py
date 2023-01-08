# importing required modules
import PyPDF2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

def pdfReaderFunc(pdfFile, pageNum):

    pdfFileObj = open(pdfFile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(pageNum)
    pdfText = (pageObj.extractText())
    pdfFileObj.close()

    return pdfText

