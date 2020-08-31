
# Metin2 Fishing Bot

A Metin2 fishing bot. The bot will play the minigame and automatically put the bait in the rod and throw the bait.
The code was build from scrap from the repository: [https://github.com/learncodebygaming/opencv_tutorials](https://github.com/learncodebygaming/opencv_tutorials)

## Requirements:
`python 3.+` and `pip`

## Install:

`pip install -r requirements`

## How to use:

- First open the game in `1024x768` resolution and `not fullscreen`. If the game is not in that resolution you need to change the values of some variables in the code (BAIT_POSITION, FISH_POSITION, FISH_WINDOW_POSITION), otherwise the bot will detect and click the wrong place in the screen.
- The code will look for a window that has the name: `Metin2`. If you have another window that also has this same name it is possible that the script will capture this other window instead. But if you want to run the bot and keep all windows open you need to grab the metin2 icon from taskbar and move it to the beginning. If you only have a game open you don't need to worry about this.
- Put the fish skill in the `1` hotkey and the bait in `2` hotkey. Equip your fishing rod.

   <img src="/images/actionbar.png" width="300">

- The game window must to be totally visible and not minimized.
- Open the Windows CMD as admin. If you open without doing that the script will not be able to click inside the game.
- Activate the virtualenv if you have it and install all requirements: `pip install -r requirements.txt`. Pip will install these following libraries:

```
numpy==1.19.1
opencv-python==4.3.0.36
PyDirectInput==1.0.2
pywin32==228
```

- Try to look at the water to not confuse the fish detection (This will be fixed soon).

   <img src="/images/look.jpg" width="300">

- Execute the hack: `python hack.py`
- When the bot is executing, the game window must be visible at all times and your mouse will be used by the bot. This is a visual bot, so it's kind of impossible for you to use your pc at the same time the bot is running because the bot needs to click with your mouse.
- Sometimes you'll find a daily bonus, the bot is not prepared for this yet. You need to click on any option. (This will be fixed soon).

   <img src="/images/atum.png" width="300">

- To quit the bot you need to select the newly created window and press `q` or kill its execution in the command prompt.

## Check list


- [x] Detect the fish.
- [x] Make a macro to fish (Bait and throw).
- [ ] Detect the fish only during the minigame.
- [ ] Detect the daily bonus and select any option.
- [ ] Use the fish bait item.
- [ ] Use fish item from the inventory to save space.
- [ ] Throw away the fish item from the inventory.
- [ ] Detect bait quantity.

