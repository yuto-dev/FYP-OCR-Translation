import fitz


def pdfCaptureFunc(fileName, pageNumber):
    doc = fitz.open(fileName)
    page = doc.load_page(pageNumber)
    pix = page.get_pixmap()
    pix.save("page-%i.png" % page.number)

  