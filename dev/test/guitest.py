import PySimpleGUI as sg

layout = [
    [sg.Text("Name: "), sg.Input(key='INPUT')],
    [sg.Ok()],
    [sg.Text("", size=(0, 1), key='OUTPUT')]
]

window = sg.Window("Just a window", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Ok':
        name = values['INPUT']
        window['OUTPUT'].update(value=name)

window.close()