import platform
import psutil
import psutil
import platform
import socket
import uuid
import re
import PySimpleGUI as sg
from app import App


apps = ("System","CPU","RAM","DISK","Network")
layout = [
    [sg.Listbox(values=apps, size=(20,20), enable_events=True, key='-LIST-'), sg.Output(size=(50,20), key="-OUTPUT-")],
    [sg.Button("Show"), sg.Button("Exit")]
]

window = sg.Window("Analyzer" , layout, element_justification='r')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED,"Exit"):
        break
    if event == "Show":
        window['-OUTPUT-'].update('')
        if values["-LIST-"][0] == "System":
            window['-OUTPUT-'].update(App.System())
            window.refresh()
        elif values["-LIST-"][0] == "CPU":
            window['-OUTPUT-'].update(App.CPU())
            window.refresh()
        elif values["-LIST-"][0] == "RAM":
            window['-OUTPUT-'].update(App.RAM())
            window.refresh()
        elif values["-LIST-"][0] == "DISK":
            window['-OUTPUT-'].update(App.DISK())
            window.refresh()
        elif values["-LIST-"][0] == "Network":
            window['-OUTPUT-'].update(App.Network())
            window.refresh()

window.close()