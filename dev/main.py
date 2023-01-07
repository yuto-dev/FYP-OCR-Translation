import PySimpleGUI as sg
from imageOCR.clipboardImage import clipboardImageFunc
from imageOCR.importImage import importImageFunc
from deepLTranslate import translateFunc

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

layout1 = [[sg.Text('This is layout 1 - It is all Checkboxes')],
           [sg.Button('buttona')]]

layout2 = [[sg.Text('This is layout 2')],
           [sg.Input(key='-IN-')],
           [sg.Input(key='-IN2-')]]

layout3 = [[sg.Text('This is layout 3 - It is all Radio Buttons')],
           *[[sg.R(f'Radio {i}', 1)] for i in range(8)]]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(layoutMain, key='mainMenu'), sg.Column(imageMenuLayout, visible=False, key='imageMenu'), sg.Column(outputTLLayout, visible=False, key='outputMenu')],
          [sg.Button('Back to Main Menu')],[sg.Button('Exit')]]

window = sg.Window('Swapping the contents of a window', layout)

currentWindow = "mainMenu"

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

    else:
        window[f'-COL{layout}-'].update(visible=False)
        layout = int(event)
        window[f'-COL{layout}-'].update(visible=True)   

window.close()