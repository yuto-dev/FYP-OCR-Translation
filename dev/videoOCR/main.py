import cv2 as cv
import numpy as np
import os
import time
from windowcapture import WindowCapture


import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(input):
        text = pytesseract.image_to_string(input)
        return text

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('APIKey.txt - Notepad')

#loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    cv.imshow('Computer Vision', screenshot)

    # debug the loop rate
    #print('FPS {}'.format(1 / (time() - loop_time)))
    print(ocr_core(screenshot))
    #loop_time = time()
    #time.sleep(5)

    
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
