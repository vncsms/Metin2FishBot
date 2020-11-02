#!/usr/bin/env python
import PySimpleGUI as sg
from interface import PyWindow
# Simple example of TabGroup element and the options available to it

# window = sg.Window('Metin2FishingBOT', layout, no_titlebar=False)
window = PyWindow().window

while True:
    event, values = window.read(timeout=1)        # Poll every 100 ms
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    # If a button was pressed, display it on the GUI by updating the text element
    if event != sg.TIMEOUT_KEY:
        print('teste')

window.close()