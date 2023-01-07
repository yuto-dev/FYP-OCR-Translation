import fitz


def pdfCaptureFunc(pageNumber):
    doc = fitz.open('jacatra.pdf')
    page = doc.load_page(pageNumber)
    pix = page.get_pixmap()
    pix.save("page-%i.png" % page.number)

pdfCaptureFunc(6)    