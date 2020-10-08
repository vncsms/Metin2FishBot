
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
- Also add a new one, but with the name `\Scripts` in the end. Like that: `C:\Users\yourwindowsusername\AppData\Local\Programs\Python\Python38-32\Scripts`.
- YOU HAVE PAY ATTENTION IN THE PATH, EVERY COMPUTER HAS A DIFERENT PATH, BECAUSE THE NAME OF THE USER.
- Download https://bootstrap.pypa.io/get-pip.py (You can just press CTRL + S)
- Now you need to know how navigate inside console. To learn about: https://www.digitalcitizen.life/command-prompt-how-use-basic-commands
- Open a CMD console and execute the file: `python get-pip.py`. You need to be in the same folder of the file to do That.
- Now enter inside the bot folder and execute the command: `pip install virtualenv`
- In the same folder: `virtualenv metin2`
- In the same folder: `metin2\Scripts\activate`
- Now you can follow the next topic.

## How to use:

- First open the game in `1024x768` resolution and `not fullscreen`. If the game is not in that resolution you need to change the values of some variables in the code (BAIT_POSITION, FISH_POSITION, FISH_WINDOW_POSITION), otherwise the bot will detect and click the wrong place in the screen.
- The code will look for a window that has the name: `Metin2`. If you have another window that also has this same name it is possible that the script will capture this other window instead. But if you want to run the bot and keep all windows open you need to grab the metin2 icon from taskbar and move it to the beginning. If you only have a game open you don't need to worry about this.
- Put the fish skill in the `1` hotkey and the bait in `2` hotkey. Equip your fishing rod.

   <img src="/images/actionbar.png" width="300">

- The game window must to be totally visible and not minimized.
- Open the Windows CMD as admin. If you open without doing that the script will not be able to click inside the game.
- Activate the virtualenv and install all requirements: `pip install -r requirements.txt`. Pip will install these following libraries:

```
numpy==1.19.1
opencv-python==4.3.0.36
PyDirectInput==1.0.2
pywin32==228
pytesseract==0.3.6
```

- Execute the hack: `python hack.py`
- When the bot is executing, the game window must be visible at all times and your mouse will be used by the bot. This is a visual bot, so it's kind of impossible for you to use your pc at the same time the bot is running because the bot needs to click with your mouse.
- Sometimes you'll find a daily bonus, the bot is not prepared for this yet. You need to click on any option. (This will be fixed soon).

   <img src="/images/atum.png" width="300">

- To quit the bot you need to select the newly created window and press `q` or kill its execution in the command prompt.
- Every time you want to execute the bot remenber to open CMD console as ADMIN and activate the virtualenv `metin2\Scripts\activate`.


## Text detect

This is a feature for only to fish selected fishs. The bot will detect the text from chat and will skip the fish that you don't want.

### WARNING

This feature only works if you have the hability to see what fish you are fishing. In my server you can buy from item mall(real money).
IF YOU CAN'T SEE WHAT FISH YOU ARE FISHING DON'T ENABLE THIS FEATURE, OR THE BOT WILL SKIP EVERY FISH. JUST SKIP THIS TOPIC.

### How to use the text detect

- First you need to download this software, it'll install text detection in your machine: https://github.com/UB-Mannheim/tesseract/wiki
- Pay attention where in your drive you will install this software, we will need this path.
- Now enable the detection variable in the file `fishingbot.py` of this project: `detect_text_enable = False` to `detect_text_enable = True`. This is the line 16.
- The are four configuration you will need change:

   - First select your language:
      - In the line 8 of the file `fishfilter.py`: `language = "eng"`
      - In case your language is not English you need to download the trained data for your language; https://github.com/tesseract-ocr/tessdata
      - Put your language trained data file inside the folder of `tessdata/` where you installed the Tesseract.
      - In my case I download the file: `por.traineddata` and my language is portuguese `language = "por"`.
      - If you put a language that you haven't the trained data the execution will generate an error.
   - Insert the path of your Terrresact in the code:
      - In the line 15 of the file `fishfilter.py` put the path of the installed Terresact:
      - In my case: `pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'`
      - I believe this is the default path in case you just press next every step in the installation.
      - If you put the wrong path will generate an error.
   - Open the chat in the game:
      - Put your chat of your game to the top and left as possible.
      - Decrease the size of your chat as minimum you can:
      - And filter only info messages
      
      <img src="/images/textdetect.png" width="400">

   - Put the fishs you want.
      - The file `fishs.txt` have all fish that the bot will filter.
      - You need to erase the content of this file and put all fish you want to fish.
      - The bot will see if the name of the fish is in inside of the text. So if put the name `Carpa` the bot will accept any fish that has this name so will accept `Carpa` or `Carpa Grande`, because this two fish contains `Carpa` in their names.
   
- You can run the bot and see the log of the execution, you will see the fishs you put in the files and the text detected.

<img src="/images/log.png" width="400">

## Check list


- [x] Detect the fish.
- [x] Make a macro to fish (Bait and throw).
- [x] Detect the fish only during the minigame.
- [x] Skip fish using text detection.
- [ ] Detect the daily bonus and select any option.
- [ ] Use the fish bait item.
- [ ] Use fish item from the inventory to save space.
- [ ] Throw away the fish item from the inventory.
- [ ] Detect bait quantity.

