import numpy as np
import pydirectinput
import cv2 as cv
import math
from time import time
from windowcapture import WindowCapture
from tetris import Tetris
from piece import Piece
import json
import constants

class PuzzleBot:

    #properties
    
    botting = False

    PUZZLE_WINDOW_SIZE = (260, 170)
    PUZZLE_WINDOW_POSITION = (270, 227)

    PUZZLE_GET_NEW_PIECE = (230, 85)
    PUZZLE_COMFIRM = (100, 90)
    PUZZLE_GET_NEW_PIECE_COLOR = (110, 150)

    wincap = None

    tetris = Tetris()

    timer_action = time()

    get_piece_time = 2

    new_piece = None

    state = 0

    end = False
    dictdump = None

    def set_to_begin(self, values):
        self.wincap = WindowCapture(constants.GAME_NAME)
        self.state = 0
        with open('pieces_second.json') as handle:
            self.dictdump = json.loads(handle.read())

    def set_puzzle_state(self, crop_img):

        paint_c = 32

        board = [[0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0]]

        for i in range(0, 4):
            for j in range(0, 6):
                if crop_img[15 + paint_c*i, 15 + paint_c*j, 0] < 50 and crop_img[15 + paint_c*i, 15 + paint_c*j, 1] < 50 and crop_img[15 + paint_c*i, 15 + paint_c*j, 2] < 50:
                    board[i][j] = 0
                else:
                    board[i][j] = 1

                cv.rectangle(crop_img, (15 + paint_c*j, 15 + paint_c*i), (15 + paint_c*j, 15 + paint_c*i),
                            color=(0, 255, 255), thickness=4, lineType=cv.LINE_4)

        self.tetris.board = board
        if self.tetris.count_zeros == 0:
            self.tetris.first = 0
            self.tetris.second = 0
        else:
            self.tetris.first = 1
            self.tetris.second = 1

    def get_image(self):

        screenshot = self.wincap.get_screenshot()

        crop_img = screenshot[self.PUZZLE_WINDOW_POSITION[1]:self.PUZZLE_WINDOW_POSITION[1]+self.PUZZLE_WINDOW_SIZE[1],
                            self.PUZZLE_WINDOW_POSITION[0]:self.PUZZLE_WINDOW_POSITION[0]+self.PUZZLE_WINDOW_SIZE[0]]

        return crop_img

    def press_comfirm(self):

        mouse_x = int(self.PUZZLE_COMFIRM[0] + self.PUZZLE_WINDOW_POSITION[0] + self.wincap.offset_x)
        mouse_y = int(self.PUZZLE_COMFIRM[1] + self.PUZZLE_WINDOW_POSITION[1] + self.wincap.offset_y)

        pydirectinput.click(x=mouse_x, y=mouse_y, button='left')
    
    def press_comfirm_cake(self):

        mouse_x = int(self.PUZZLE_COMFIRM[0] + 20 + self.PUZZLE_WINDOW_POSITION[0] + self.wincap.offset_x)
        mouse_y = int(self.PUZZLE_COMFIRM[1] + self.PUZZLE_WINDOW_POSITION[1] + self.wincap.offset_y)

        pydirectinput.click(x=mouse_x, y=mouse_y, button='left')

    def throw_pice(self):

        mouse_x = int(self.PUZZLE_COMFIRM[0] + self.PUZZLE_WINDOW_POSITION[0] + self.wincap.offset_x)
        mouse_y = int(self.PUZZLE_COMFIRM[1] + self.PUZZLE_WINDOW_POSITION[1] + self.wincap.offset_y)

        pydirectinput.click(x=mouse_x, y=mouse_y, button='right')

    def get_new_piece_color(self, crop_image):

        x = int(self.PUZZLE_GET_NEW_PIECE_COLOR[0])
        y = int(self.PUZZLE_GET_NEW_PIECE_COLOR[1])

        if (crop_image[y, x, 0] > 35 and crop_image[y, x, 0] < 40 and 
           crop_image[y, x, 1] > 60 and crop_image[y, x, 1] < 70 and 
           crop_image[y, x, 2] > 240 and crop_image[y, x, 2] < 260):
            return 4
        elif (crop_image[y, x, 0] > 20 and crop_image[y, x, 0] < 30 and 
           crop_image[y, x, 1] > 150 and crop_image[y, x, 1] < 170 and 
           crop_image[y, x, 2] > 240 and crop_image[y, x, 2] < 260):
            return 1
        elif (crop_image[y, x, 0] > 35 and crop_image[y, x, 0] < 50 and 
           crop_image[y, x, 1] > 240 and crop_image[y, x, 1] < 260 and 
           crop_image[y, x, 2] > 35 and crop_image[y, x, 2] < 50):
            return 5
        elif (crop_image[y, x, 0] > 240 and crop_image[y, x, 0] < 260 and 
           crop_image[y, x, 1] > 240 and crop_image[y, x, 1] < 260 and 
           crop_image[y, x, 2] > 20 and crop_image[y, x, 2] < 30):
            return 3
        elif (crop_image[y, x, 0] > 240 and crop_image[y, x, 0] < 260 and 
           crop_image[y, x, 1] > 100 and crop_image[y, x, 1] < 115 and 
           crop_image[y, x, 2] > -10 and crop_image[y, x, 2] < 10):
            return 2
        elif (crop_image[y, x, 0] > 50 and crop_image[y, x, 0] < 60 and 
           crop_image[y, x, 1] > 235 and crop_image[y, x, 1] < 255 and 
           crop_image[y, x, 2] > 250 and crop_image[y, x, 2] < 260):
            return 6

    def detect_end_game(self, crop_img):

        x = int(self.PUZZLE_GET_NEW_PIECE[0])
        y = int(self.PUZZLE_GET_NEW_PIECE[1])


        if crop_img[y, x, 0] > 100 and crop_img[y, x, 1] > 150 and crop_img[y, x, 2] > 150:
            return False
        else:
            return True

    def play_game(self):
        
        piece = Piece(self.new_piece)

        decision, pos = self.tetris.find_first(piece, self.dictdump)
        paint_c = 32
        if decision == 1:

            self.tetris.insert_piece(pos[0], pos[1], piece)
            if self.tetris.verify_end():
                self.end = True
            mouse_x = 15 + paint_c*pos[1] + self.PUZZLE_WINDOW_POSITION[0] + self.wincap.offset_x
            mouse_y = 15 + paint_c*pos[0] + self.PUZZLE_WINDOW_POSITION[1] + self.wincap.offset_y
            pydirectinput.click(mouse_x, mouse_y)

            return None

        if decision == 2:
            return None

        possibilites = self.tetris.find_possibles(piece)

        pices_count = 0

        for i in range(1,7):
            if i != piece.piece_type:
                possis = self.tetris.find_possibles(Piece(i))
                if len(possis):
                    pices_count += 1

        if piece.piece_type == 1 and pices_count != 0:
            possibilites = [i for i in possibilites if self.tetris.verify_isolated(i[0], i[1])]

        if len(possibilites):

            a = self.tetris.choose_better(piece, possibilites)

            self.tetris.insert_piece(a[0], a[1], piece)
            if self.tetris.verify_end():
                self.end = True
            mouse_x = 15 + paint_c*a[1] + self.PUZZLE_WINDOW_POSITION[0] + self.wincap.offset_x
            mouse_y = 15 + paint_c*a[0] + self.PUZZLE_WINDOW_POSITION[1] + self.wincap.offset_y
            pydirectinput.click(mouse_x, mouse_y)

            return True

        return None

    def runHack(self):
        
        crop_image = self.get_image()

        timep = 0.2

        if self.state == 0:
            mouse_x = int(self.PUZZLE_GET_NEW_PIECE[0] + self.PUZZLE_WINDOW_POSITION[0] + self.wincap.offset_x)
            mouse_y = int(self.PUZZLE_GET_NEW_PIECE[1] + self.PUZZLE_WINDOW_POSITION[1] + self.wincap.offset_y)

            if time() - self.timer_action > timep:

                if self.detect_end_game(crop_image):
                    self.botting = False
                    return None

                pydirectinput.click(x=mouse_x, y=mouse_y, button='left')
                self.state = 1
                self.timer_action = time()

        if self.state == 1:

            if time() - self.timer_action > timep:
                self.press_comfirm()
                self.state = 2
                self.timer_action = time()

        if self.state == 2:

            mouse_x = int(self.PUZZLE_GET_NEW_PIECE_COLOR[0] + self.PUZZLE_WINDOW_POSITION[0] + self.wincap.offset_x)
            mouse_y = int(self.PUZZLE_GET_NEW_PIECE_COLOR[1] + self.PUZZLE_WINDOW_POSITION[1] + self.wincap.offset_y)

            if time() - self.timer_action > timep:
                self.state = 4
                self.timer_action = time()
                pydirectinput.moveTo(mouse_x, mouse_y)

        if self.state == 4:

            if time() - self.timer_action > timep:
                self.state = 5
                self.timer_action = time()
                self.new_piece = self.get_new_piece_color(crop_image)

        if self.state == 5:
            if time() - self.timer_action > timep:
                self.timer_action = time()
                self.set_puzzle_state(crop_image)
                if self.play_game():
                    self.state = 6
                else:
                    self.state = 7
                
        if self.state == 6:
            if time() - self.timer_action > timep:
                self.press_comfirm()
                self.timer_action = time()
                if self.end:
                    self.state = 9
                else: 
                    self.state = 0

        if self.state == 7:
            if time() - self.timer_action > timep:
                self.throw_pice()
                self.timer_action = time()
                self.state = 8

        if self.state == 8:
            if time() - self.timer_action > timep:
                self.press_comfirm()
                self.timer_action = time()
                self.state = 0

        if self.state == 9:
            if time() - self.timer_action > 2:
                self.end = False
                self.press_comfirm_cake()
                self.timer_action = time()
                self.state = 0

        return None
