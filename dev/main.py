import PySimpleGUI as sg
import os
from imageOCR.clipboardImage import clipboardImageFunc
from imageOCR.importImage import importImageFunc
#from videoOCR.windowcapture import WindowCapture
from videoOCR.videoOCR import videoOCRFunc
from pdfCapture.pdfOCR import pdfOCRFunc
from pdfCapture.pdfCapture import pdfCaptureFunc  
from pdfReader.reader import pdfReaderFunc
from deepLTranslate import translateFunc
import time

currentWindow = "mainMenu"
currentPage = 1

# ----------- Create the 3 layouts this Window will display -----------
layoutMain = [[sg.Text('This is the main menu')],
            [sg.Button('Image')],
            [sg.Button('Video')],
            [sg.Button('PDF')]]

imageMenuLayout = [[sg.Text('This is the image menu')],
            [sg.Button('Image Clipboard')],
            [sg.Button('Image Import')]]

outputTLLayout = [[sg.Text("Input: ")], [sg.Text("", key='imageInput')],
                  [sg.Text("Output: ")],[sg.Text("", key='imageOutput')]]

videoOCRMenuLayout = [[sg.Text("Window name: "), sg.Input(key="windowNameText")],
                      [sg.Text("Interval (in seconds): "), sg.Input(key="intervalText")],
                      [sg.Text("Duration (in seconds): "), sg.Input(key="durationText")],
                      [sg.Button("Start Video Capture")]]

videoOCRResultLayout = [[sg.Text('This is the input:')],
                        [sg.Multiline("", size=(100, 5), key='videoOCRInputBox')],
                        [sg.Text('This is the output:')],
                        [sg.Multiline("", size=(100, 5), key='videoOCROutputBox')]]
                         

pdfMenuLayout = [[sg.Text('This is the PDF menu')],
                 [sg.Button('PDF OCR')],
                 [sg.Button('PDF Reader')]]

pdfOCRLayout = [[sg.Text('This is the input:')],
                [sg.Multiline("", size=(100, 5), key='pdfOCRInputBox')],
                [sg.Text('This is the output:')],
                [sg.Multiline("", size=(100, 5), key='pdfOCROutputBox')],
                [sg.Text('Page number: '), sg.Text('{currentPage}', key='currentPageText') ],
                [sg.Button('OCR Previous Page')],
                [sg.Button('OCR Next Page')]] 

pdfReaderLayout = [[sg.Text('This is the input:')],
                   [sg.Multiline("", size=(100, 5), key='pdfReaderInputBox')],
                   [sg.Text('This is the output:')],
                   [sg.Multiline("", size=(100, 5), key='pdfReaderOutputBox')],
                   [sg.Text('Page number: '), sg.Text('{currentPage}', key='currentPageText') ],
                   [sg.Button('Reader Previous Page')],
                   [sg.Button('Reader Next Page')]]  # identify the multiline via key option




# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layoutMain, key='mainMenu'),
           sg.Column(imageMenuLayout, visible=False, key='imageMenu'),
           sg.Column(videoOCRMenuLayout, visible=False, key='videoOCRMenu'),
           sg.Column(videoOCRResultLayout, visible=False, key='videoOCRResultMenu'),
           sg.Column(pdfMenuLayout, visible=False, key='pdfMenu'),
           sg.Column(pdfOCRLayout, visible=False, key='pdfOCRMenu'),
           sg.Column(pdfReaderLayout, visible=False, key='pdfReaderMenu'),
           sg.Column(outputTLLayout, visible=False, key='outputMenu')],

          [sg.Button('Back to Main Menu')],[sg.Button('Exit')]]

window = sg.Window('Swapping the contents of a window', layout, size=(500, 500))



while True:
    event, values = window.read()
#    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Back to Main Menu':
        window[f'{currentWindow}'].update(visible=False)
        window[f'mainMenu'].update(visible=True)
        currentWindow = "mainMenu"

    elif event == 'Image':
        window[f'{currentWindow}'].update(visible=False)
        window[f'imageMenu'].update(visible=True)
        currentWindow = "imageMenu"

    elif event == 'Image Clipboard':
        window[f'{currentWindow}'].update(visible=False)
        window[f'outputMenu'].update(visible=True)
        currentWindow = "outputMenu"
        translateInput = clipboardImageFunc()
        translateResult = translateFunc(translateInput)
        window[f'imageInput'].update(value = translateInput)
        window[f'imageOutput'].update(value = translateResult)

    elif event == 'Image Import':
        window[f'{currentWindow}'].update(visible=False)
        window[f'outputMenu'].update(visible=True)
        currentWindow = "outputMenu"
        translateInput = importImageFunc()
        translateResult = translateFunc(translateInput)
        window[f'imageInput'].update(value = translateInput)
        window[f'imageOutput'].update(value = translateResult)  

    elif event == 'Video':
        window[f'{currentWindow}'].update(visible=False)
        window[f'videoOCRMenu'].update(visible=True)
        currentWindow = "videoOCRMenu"

    elif event == 'Start Video Capture':
        window[f'{currentWindow}'].update(visible=False)
        window[f'videoOCRResultMenu'].update(visible=True)
        currentWindow = "videoOCRResultMenu"  

        windowName = 'System Properties'
        interval = values['intervalText']
        print(interval)
        amount = 60
        amountDalam = 5
        translateInput = videoOCRFunc(windowName)
        translateResult = translateFunc(translateInput)
        for x in range(amount):    
            
            window[f'videoOCRInputBox'].update(value = translateInput)
            window[f'videoOCROutputBox'].update(value = translateResult)  
            for y in range(amountDalam):
                translateInput = videoOCRFunc(windowName)
                translateResult = translateFunc(translateInput)
            #time.sleep(int(interval)) 
            print(time.time())
            print(x)   

    elif event == 'PDF':
        window[f'{currentWindow}'].update(visible=False)
        window[f'pdfMenu'].update(visible=True)
        currentWindow = "pdfMenu"  

    elif event == 'PDF OCR':
        window[f'{currentWindow}'].update(visible=False)
        window[f'pdfOCRMenu'].update(visible=True)
        currentWindow = "pdfOCRMenu"  
        currentPage = 1
        print(currentPage)
        pdfCaptureFunc(currentPage)
        translateInput = pdfOCRFunc(currentPage)
        translateResult = translateFunc(translateInput)
        window[f'pdfOCRInputBox'].update(value = translateInput)
        window[f'pdfOCROutputBox'].update(value = translateResult)    

        if os.path.exists('page-%i.png' % currentPage):
            os.remove('page-%i.png' % currentPage)

    elif event == 'OCR Next Page':
        window[f'{currentWindow}'].update(visible=False)
        window[f'pdfOCRMenu'].update(visible=True)
        currentWindow = "pdfOCRMenu"  
        currentPage = currentPage + 1     
        pdfCaptureFunc(currentPage)
        translateInput = pdfOCRFunc(currentPage)
        translateResult = translateFunc(translateInput)
        window[f'pdfOCRInputBox'].update(value = translateInput)
        window[f'pdfOCROutputBox'].update(value = translateResult)
        window[f'currentPageText'].update(value = currentPage)  

        if os.path.exists('page-%i.png' % currentPage):
            os.remove('page-%i.png' % currentPage)  

    elif event == 'OCR Previous Page':
        window[f'{currentWindow}'].update(visible=False)
        window[f'pdfOCRMenu'].update(visible=True)
        currentWindow = "pdfOCRMenu"  
        currentPage = currentPage - 1     
        pdfCaptureFunc(currentPage)
        translateInput = pdfOCRFunc(currentPage)
        translateResult = translateFunc(translateInput)
        window[f'pdfOCRInputBox'].update(value = translateInput)
        window[f'pdfOCROutputBox'].update(value = translateResult)
        window[f'currentPageText'].update(value = currentPage)  

        if os.path.exists('page-%i.png' % currentPage):
            os.remove('page-%i.png' % currentPage)
        
    elif event == 'PDF Reader':
        window[f'{currentWindow}'].update(visible=False)
        window[f'pdfReaderMenu'].update(visible=True)
        currentWindow = "pdfReaderMenu"       
        translateInput = pdfReaderFunc(currentPage)
        translateResult = translateFunc(translateInput)
        window[f'pdfReaderInputBox'].update(value = translateInput)
        window[f'pdfReaderOutputBox'].update(value = translateResult)  

    elif event == 'Reader Next Page':
        window[f'{currentWindow}'].update(visible=False)
        window[f'pdfReaderMenu'].update(visible=True)
        currentWindow = "pdfReaderMenu"  
        currentPage = currentPage + 1     
        translateInput = pdfReaderFunc(currentPage)
        translateResult = translateFunc(translateInput)
        window[f'pdfReaderInputBox'].update(value = translateInput)
        window[f'pdfReaderOutputBox'].update(value = translateResult)
        window[f'currentPageText'].update(value = currentPage)     

    elif event == 'Reader Previous Page':
        window[f'{currentWindow}'].update(visible=False)
        window[f'pdfReaderMenu'].update(visible=True)
        currentWindow = "pdfReaderMenu"  
        currentPage = currentPage - 1     
        translateInput = pdfReaderFunc(currentPage)
        translateResult = translateFunc(translateInput)
        window[f'pdfReaderInputBox'].update(value = translateInput)
        window[f'pdfReaderOutputBox'].update(value = translateResult)
        window[f'currentPageText'].update(value = currentPage)          
         

    else:
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(event)
        window[f'-COL{layout}-'].update(visible=True)   

window.close()