import cv2 as cv
import numpy as np
import pydirectinput
import math
from time import time
from windowcapture import WindowCapture
from hsvfilter import HsvFilter


fish_pos_x = None
fish_pos_y = None

fish_direction = None
fish_last_time = None
fish_velocity = None

FISH_RANGE = 74
FISH_VELO_PREDICT = 30

BAIT_POSITION = (473, 750)
FISH_POSITION = (440, 750)

FILTER_CONFIG = [49, 0, 58, 134, 189, 189, 0, 0, 0, 0]

# set position of the fish windows
# this value can be diferent by the sizes of the game window

FISH_WINDOW_SIZE = (280, 226)
FISH_WINDOW_POSITION = (163, 125)


def shift_channel(c, amount):
    if amount > 0:
        lim = 255 - amount
        c[c >= lim] = 255
        c[c < lim] += amount
    elif amount < 0:
        amount = -amount
        lim = amount
        c[c <= lim] = 0
        c[c > lim] -= amount
    return c


def apply_hsv_filter(original_image, hsv_filter=None):
    # convert image to HSV
    hsv = cv.cvtColor(original_image, cv.COLOR_BGR2HSV)

    # add/subtract saturation and value
    h, s, v = cv.split(hsv)
    s = shift_channel(s, hsv_filter.sAdd)
    s = shift_channel(s, -hsv_filter.sSub)
    v = shift_channel(v, hsv_filter.vAdd)
    v = shift_channel(v, -hsv_filter.vSub)
    hsv = cv.merge([h, s, v])

    # Set minimum and maximum HSV values to display
    lower = np.array([hsv_filter.hMin, hsv_filter.sMin, hsv_filter.vMin])
    upper = np.array([hsv_filter.hMax, hsv_filter.sMax, hsv_filter.vMax])
    # Apply the thresholds
    mask = cv.inRange(hsv, lower, upper)
    result = cv.bitwise_and(hsv, hsv, mask=mask)

    # convert back to BGR for imshow() to display it properly
    img = cv.cvtColor(result, cv.COLOR_HSV2BGR)

    return img


def detect(haystack_img, needle_img):

    # match the needle_image with the hasytack image
    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # needle_image's dimensions
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    # get the position of the match image
    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    # Draw the circle of the fish limits
    cv.circle(haystack_img,
              (int(haystack_img.shape[1] / 2), int(haystack_img.shape[0] / 2)),
              FISH_RANGE, color=(0, 0, 255), thickness=1)

    # Only the max level of match is greater than 0.5
    if max_val > 0.5:
        pos_x = (top_left[0] + bottom_right[0])/2
        pos_y = (top_left[1] + bottom_right[1])/2

        global fish_pos_x
        global fish_pos_y
        global fish_last_time

        if fish_last_time:
            dist = math.sqrt((pos_x - fish_pos_x)**2 + (fish_pos_y - pos_y)**2)
            cv.rectangle(haystack_img, top_left, bottom_right,
                         color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

            # Calculate the fish velocity
            velo = dist/(time() - fish_last_time)

            if velo == 0.0:
                return (pos_x, pos_y, True)
            elif velo >= 150:

                # With this velocity the fish position will be predict

                pro = FISH_VELO_PREDICT / dist
                destiny_x = int(pos_x + (pos_x - fish_pos_x) * pro)
                destiny_y = int(pos_y + (pos_y - fish_pos_y) * pro)

                # Draw the predict line

                cv.line(haystack_img, (int(pos_x), int(pos_y)),
                        (destiny_x, destiny_y), (0, 255, 0),  thickness=3)

                return (destiny_x, destiny_y, False)

        # get the fish position and the time

        fish_pos_x = pos_x
        fish_pos_y = pos_y
        fish_last_time = time()
    return None


# Capture the game screen

wincap = WindowCapture('METIN2')

# Load the needle image

needle_img = cv.imread('fiss.jpg', cv.IMREAD_UNCHANGED)

# Some time cooldowns

# for fps

loop_time = time()

# The mouse click cooldown

timer_mouse = time()

# The timer beteween the states

timer_action = time()

# This is the filter parameters, this help to find the right image
hsv_filter = HsvFilter(*FILTER_CONFIG)

state = 0

# 0 -> not fishing
# 1 -> put food
# 2 -> fish
# 3 -> detecting



while(True):

    screenshot = wincap.get_screenshot()

    # crop and aply hsv filter
    crop_img = screenshot[FISH_WINDOW_POSITION[1]:FISH_WINDOW_POSITION[1]+FISH_WINDOW_SIZE[1],
                          FISH_WINDOW_POSITION[0]:FISH_WINDOW_POSITION[0]+FISH_WINDOW_SIZE[0]]
    crop_img = apply_hsv_filter(crop_img, hsv_filter=hsv_filter)

    # Print some information

    cv.putText(crop_img, 'FPS: ' + str(1/(time() - loop_time))[:2],
               (10, 200), cv.FONT_HERSHEY_SIMPLEX,  0.5, (0, 255, 0), 2)
    cv.putText(crop_img, 'State: ' + str(state) + ' ' + str(time() - timer_action)[:5],
               (10, 160), cv.FONT_HERSHEY_SIMPLEX,  0.5, (0, 255, 0), 2)
    loop_time = time()

    # State to click put the bait in the rod

    if state == 0:
        mouse_x = int(BAIT_POSITION[0] + wincap.offset_x)
        mouse_y = int(BAIT_POSITION[1] + wincap.offset_y)

        if time() - timer_action > 2:
            pydirectinput.click(x=mouse_x, y=mouse_y, button='right')
            state = 1
            timer_action = time()

    # State to throw the bait

    if state == 1:
        if time() - timer_action > 1:
            mouse_x = int(FISH_POSITION[0] + wincap.offset_x)
            mouse_y = int(FISH_POSITION[1] + wincap.offset_y)
            pydirectinput.click(x=mouse_x, y=mouse_y, button='right')
            state = 2
            timer_action = time()

    # Delay to start the clicks

    if state == 2:
        if time() - timer_action > 1.5:
            state = 3
            timer_action = time()

    # Countdown to finish the state

    if state == 3:
        if time() - timer_action > 15:
            timer_action = time()
            state = 0

    # Detect the fish
    square_pos = detect(crop_img, needle_img)

    # make the click

    if (time() - timer_mouse) > 0.3 and square_pos and state == 3:

        # Recalculate the mouse position with the fish position

        pos_x = square_pos[0]
        pos_y = square_pos[1]

        center_x = FISH_WINDOW_SIZE[0]/2
        center_y = FISH_WINDOW_SIZE[1]/2

        mouse_x = int(pos_x)
        mouse_y = int(pos_y)

        # Verify if the fish is in range

        d = FISH_RANGE**2 - ((center_x-mouse_x)**2 + (center_y-mouse_y)**2)

        # Make the click

        if (d > 0):
            timer_mouse = time()

            mouse_x = int(pos_x + FISH_WINDOW_POSITION[0] + wincap.offset_x)
            mouse_y = int(pos_y + FISH_WINDOW_POSITION[1] + wincap.offset_y)

            pydirectinput.click(x=mouse_x, y=mouse_y)

    cv.imshow('Minha Janela', crop_img)

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
