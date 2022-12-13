import fitz

print(fitz.__doc__)

doc = fitz.open('jacatra.pdf')

toc = doc.get_toc()
print(toc)

page = doc.load_page(6)
pix = page.get_pixmap()
pix.save("page-%i.png" % page.number)