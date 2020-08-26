# Metin2FishBot

A Metin2 fish bot. The bot will play the minigame and automatically put the bait in the rod and throw the bait.
The code was build from scrap from the repository: [https://github.com/learncodebygaming/opencv_tutorials](https://github.com/learncodebygaming/opencv_tutorials)

## Requirements:
`python 3.+` and `pip`

## Install:

`pip install -r requirements`

## How to use:

- First open the game in `1024x768` resolution and `not fullscreen`. If the game is not in that resolution you need to change the values of some variables in the code (BAIT_POSITION, FISH_POSITION, FISH_WINDOW_POSITION), otherwise the bot will detect and click the wrong place in the screen.
- The code will look for a window that has the name: `Metin2`. If you have another window that also have this same name is possible the script will capture this other window instead. But if you want to run the bot and keep this windows you need to move the window of the game to the first (You can just grab the window to begin). If you only have a game open you dont need to worry about.
- Put the fish skill in the `1` hotkey and the bait in `2` hotkey. Equip your fishing rod.

   <img src="/images/actionbar.png" width="300">

- The game window must to be all visible and not minimized.
- Open the Windows CMD as admin. If you open without that way the script will not be able to click inside the game.
- Activate the virtualenv if you have and install all requirements: `pip install -r requirements.txt`. Pip will install these follow libraries:

```
numpy==1.19.1
opencv-python==4.3.0.36
PyDirectInput==1.0.2
pywin32==228
```

- Try to look at the water for not confuse the fish detection (This will be fix soon).

   <img src="/images/look.jpg" width="300">

- Execute the hack: `python hack.py`
- When the bot is executing, the game window must be visible all time and your mouse will used by the bot. This is a visual bot, so is kind impossible to you use your pc in the same time the bot is running because the bot you click with your mouse.
- Sometimes you find a daily bonus, the bot is not yet prepared for his. You need to click in any option. (This will be fix soon).

   <img src="/images/atum.png" width="300">

- For you to quit the bot you need select the new window created and press `q`. Or kill the execution in the command prompt.

## Check list


- [x] Detect fish
- [x] Make macro to fish (Bait and throw)
- [ ] Detect fish only in the minigame
- [ ] Detect daily bonus
- [ ] Use item fish bait
- [ ] Use item fish from inventory to save space
- [ ] Thow away item fish from inventory
- [ ] Detect bait quantity

