from fishingbot import FishingBot
from puzzle import PuzzleBot
from interface import PyWindow
import PySimpleGUI as sg

window = PyWindow().window
fishbot = FishingBot()
puzzleBot = PuzzleBot()

while True:

    event, values = window.read(timeout=1)
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event != sg.TIMEOUT_KEY:
        if event == '-BUTTONSTART-':
            fishbot.set_to_begin(values)
            fishbot.botting = not fishbot.botting
            puzzleBot.botting = False
        if event == '-BUTTONPUZZLESTART-':
            puzzleBot.set_to_begin(values)
            puzzleBot.botting = not puzzleBot.botting
            fishbot.botting = False

    if fishbot.botting:
        fishbot.runHack()
        window.FindElement('-BUTTONSTART-').update('STOP')
    else:
        window.FindElement('-BUTTONSTART-').update('START')

    if puzzleBot.botting:
        try:
            puzzleBot.runHack()
            window.FindElement('-BUTTONPUZZLESTART-').update('STOP')
        except:
            puzzleBot.botting = not puzzleBot.botting
            fishbot.botting = False

    else:
        window.FindElement('-BUTTONPUZZLESTART-').update('START')

window.close()
