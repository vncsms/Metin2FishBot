from fishingbot import FishingBot
from interface import PyWindow
import PySimpleGUI as sg

window = PyWindow().window
fishbot = FishingBot()

while True:

    event, values = window.read(timeout=1)
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    # import pdb; pdb.set_trace()

    if event != sg.TIMEOUT_KEY:
        if event == '-BUTTONSTART-':
            fishbot.set_to_begin(values)
            fishbot.botting = not fishbot.botting

    if fishbot.botting:
        fishbot.runHack()
        window.FindElement('-BUTTONSTART-').update('STOP')
    else:
        window.FindElement('-BUTTONSTART-').update('START')

window.close()
