
# Metin2 Fishing Bot

A Metin2 fishing bot. The bot will play the minigame and automatically put the bait in the rod and throw the bait.
The code was build from scrap from the repository: [https://github.com/learncodebygaming/opencv_tutorials](https://github.com/learncodebygaming/opencv_tutorials)

## Requirements:
`python 3.8.5` and `pip`

- Preferable use the version 3.8.5, because others versions is getting few errors in the Opencv library installation.

## Case you don't know how to install these requirements:

- Download python https://www.python.org/downloads/release/python-385/ bottom of the page. You may download the executable.
- Install Python.
- Copy the path of your python. Is something like that: `C:\Users\yourwindowsusername\AppData\Local\Programs\Python\Python38-32`.
- And paste inside your enviroment variables:

   <img src="/images/python.png" width="600">

- Also add a new one, but with the name `\Scripts` in the end. Like that: `C:\Users\yourwindowsusername\AppData\Local\Programs\Python\Python38-32\Scripts`.
- YOU HAVE TO PAY ATTENTION IN THE PATH, EVERY COMPUTER HAS A DIFERENT PATH, BECAUSE THE NAME OF THE USER.
- Download https://bootstrap.pypa.io/get-pip.py (You can just press CTRL + S)
- Now you need to know how navigate inside console. To learn about: https://www.digitalcitizen.life/command-prompt-how-use-basic-commands
- Open a CMD console and execute the file: `python get-pip.py`. You need to be in the same folder of the file to do That.
- Now enter inside the bot folder and execute the command: `pip install virtualenv`
- In the same folder: `virtualenv metin2`
- In the same folder: `metin2\Scripts\activate`
- Since you activated the virtualenv you can install all requirements: `pip install -r requirements.txt`. Pip will install these following libraries:

```
numpy==1.19.1
opencv-python==4.3.0.36
PyDirectInput==1.0.2
pywin32==228
pytesseract==0.3.6
PySimpleGUI==4.30.0
pyinstaller==4.3
```

- To generate the executable run: `pyinstaller --onefile hack.py`. When it's end move the executable file in the folder `dist` to the project's root.

- You also can watch the video to learn how run the bot

<a href="http://www.youtube.com/watch?feature=player_embedded&v=Kcvmzz3MXnQ
" target="_blank"><img src="http://img.youtube.com/vi/Kcvmzz3MXnQ/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="480" height="360" border="10" /></a>

## How to use:

- First open the game in `800x600` resolution and `not fullscreen`, Otherwise the bot will detect and click the wrong place in the screen.
- The code will look for a window that has the name: `Metin2`. If you have another window that also has this same name it is possible that the script will capture this other window instead. But if you want to run the bot and keep all windows open you need to grab the metin2 icon from taskbar and move it to the beginning. If you only have a game open you don't need to worry about this.
- If your game has a diferent name you must change the name in the constant files: `constants.py`
- Put the fish skill in the `1` hotkey and the bait in `2` hotkey. Equip your fishing rod.

   <img src="/images/actionbar.png" width="300">

- The game window must to be totally visible and not minimized.

- Open the executable as admin.
- Will open a screen like that:

   <img src="/images/interface1.jpg" width="300">
   
- You can set a limit time in minutes to stop the bot.
- To start the bot you need to press start, and to stop you can press the same button.

   <img src="/images/interface2.jpg" width="300">

- In the options you can set the delay time to bait, throw and start the minigame.
   
- When the bot is executing, the game window must be visible at all times and your mouse will be used by the bot. This is a visual bot, so it's kind of impossible for you to use your pc at the same time the bot is running because the bot needs to click with your mouse.

- To stop the bot you can use time condition or press the button `STOP`.

- Now you also can use the bot to solve the mini game puzzle. Just Select Puzzle Tab and open the mini game puzzle. Don't move the mini game puzzle window.


## Check list


- [x] Detect the daily bonus and select any option.
- [ ] Use the fish bait item.
- [ ] Use fish item from the inventory to save space.
- [ ] Throw away the fish item from the inventory.
- [ ] Detect bait quantity.
- [ ] Text Detection to skip fish. Was not working well the last version.

