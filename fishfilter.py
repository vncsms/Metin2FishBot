import pytesseract
import numpy as np
import cv2 as cv

class Filter:

    match_words = []
    language = "eng"

    TEXT_POSITION = (75,0)
    TEXT_SIZE = (15,300)

    def __init__(self):

        pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

        file = open('fishs.txt')
        for fish in file:
            self.match_words.append(fish.replace('\n', ''))

        print("Fishs: ")
        print(self.match_words)


    def change_image(self, crop_img):
        crop_img = cv.cvtColor(crop_img, cv.COLOR_BGR2GRAY)
        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        crop_img = cv.filter2D(crop_img, -1, sharpen_kernel)
        crop_img = cv.threshold(crop_img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

        return crop_img

    def get_text_image(self, crop_img):
        return pytesseract.image_to_string(crop_img, lang=self.language)

    def match_with_text(self, screenshot):

        crop_img = screenshot[self.TEXT_POSITION[0]:self.TEXT_POSITION[0] + self.TEXT_SIZE[0],
                              self.TEXT_POSITION[1]:self.TEXT_POSITION[1] + self.TEXT_SIZE[1]]
        crop_img = self.change_image(crop_img)

        text = self.get_text_image(crop_img)
        print("Detect text:")
        print(text)
        for fish in self.match_words:
            if fish.lower() in text.lower():
                return True
        
        return False
