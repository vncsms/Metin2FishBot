import numpy as np
import cv2 as cv

class HsvFilter:

    def __init__(self, hMin=None, sMin=None, vMin=None, hMax=None, sMax=None, vMax=None, 
                    sAdd=None, sSub=None, vAdd=None, vSub=None):
        self.hMin = hMin
        self.sMin = sMin
        self.vMin = vMin
        self.hMax = hMax
        self.sMax = sMax
        self.vMax = vMax
        self.sAdd = sAdd
        self.sSub = sSub
        self.vAdd = vAdd
        self.vSub = vSub

    def shift_channel(self, c, amount):
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


    def apply_hsv_filter(self, original_image):
        # convert image to HSV
        hsv = cv.cvtColor(original_image, cv.COLOR_BGR2HSV)

        # add/subtract saturation and value
        h, s, v = cv.split(hsv)
        s = self.shift_channel(s, self.sAdd)
        s = self.shift_channel(s, -1*self.sSub)
        v = self.shift_channel(v, self.vAdd)
        v = self.shift_channel(v, -1*self.vSub)
        hsv = cv.merge([h, s, v])

        # Set minimum and maximum HSV values to display
        lower = np.array([self.hMin, self.sMin, self.vMin])
        upper = np.array([self.hMax, self.sMax, self.vMax])
        # Apply the thresholds
        mask = cv.inRange(hsv, lower, upper)
        result = cv.bitwise_and(hsv, hsv, mask=mask)

        # convert back to BGR for imshow() to display it properly
        img = cv.cvtColor(result, cv.COLOR_HSV2BGR)

        return img