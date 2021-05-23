from piece import Piece
from copy import deepcopy
class Tetris:

    board = None

    first = 0
    second = 0

    def __init__(self):
        self.board = [[0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0],
                      [0,0,0,0,0,0]]


    def find_first(self, piece, dictdump):
        if not self.first:
            pos = dictdump['first'][str(piece.piece_type)]['pos']
            if pos:
                self.first = piece.piece_type
                # self.insert_piece(pos[0], pos[1], piece)
                return 1, pos
            else:
                return 2, None
        if not self.second:
            pos = dictdump['first'][str(self.first)]['second'][str(piece.piece_type)]['pos']
            if pos:
                self.second = piece.piece_type
                # self.insert_piece(pos[0], pos[1], piece)
                return 1, pos
            else:
                return 2, None

        return 3, None

    def count_zeros(self):
        total = 0
        for i in self.board:
            for l in self.board:
                total += 1

        return 24 - total

    def verify_end(self):

        for i in self.board:
            if 0 in i:
                return False
            
        return True

    def insert_piece(self, position_x, position_y, piece):

        if (piece.height - 1 + position_x) > 3:
            return False
        elif (piece.width - 1 + position_y) > 5:
            return False

        pos_row = position_x
        pos_column = position_y

        for row in piece.form:
            for cel in row:
                if cel and self.board[pos_row][pos_column]:
                    return False
                self.board[pos_row][pos_column] += cel
                pos_column += 1
            pos_row += 1
            pos_column = position_y

        return True

    def verify_insert_piece(self, position_x, position_y, piece, board):

        if (piece.height - 1 + position_x) > 3:
            return False
        elif (piece.width - 1 + position_y) > 5:
            return False

        pos_row = position_x
        pos_column = position_y

        for row in piece.form:
            for cel in row:
                if cel and board[pos_row][pos_column]:
                    return False
                pos_column += 1
            pos_row += 1
            pos_column = position_y

        return True 

    def verify_isolated(self, x, y):

        if (x == 0 and y == 0) or (x == 2 and y == 0):
            if self.board[x][y+1] == 1 and self.board[x+1][y] == 1:
                return True
            return False

        if (x == 0 and y == 5) or (x == 2 and y == 5):
            if self.board[x][y-1] == 1 and self.board[x+1][y] == 1:
                return True
            return False

        if (x == 1 and y == 0) or (x == 3 and y == 0):
            if self.board[x-1][y] == 1 and self.board[x][y+1] == 1:
                return True
            return False

        if (x == 1 and y == 5) or (x == 3 and y == 5):
            if self.board[x-1][y] == 1 and self.board[x][y-1] == 1:
                return True
            return False

        if (x == 0 or x == 2) and (y > 0 and y < 5):
            if self.board[x][y-1] == 1 and self.board[x][y+1] == 1 and self.board[x+1][y] == 1:
                return True
            return False

        if (x == 1 or x == 3) and (y > 0 and y < 5):
            if self.board[x][y-1] == 1 and self.board[x][y+1] == 1 and self.board[x-1][y] == 1:
                return True
            return False

    def choose_better(self, piece, possibilites):
        
        better_one = None
        better_total = -1

        for p in possibilites:
            tetris = Tetris()
            a = self.board
            tetris.board = [[a[x][y] for y in range(len(a[0]))] for x in range(len(a))]
            tetris.insert_piece(p[0], p[1], piece)

            pices_count = 0

            for i in range(1,7):
                if i != piece.piece_type:
                    possis = tetris.find_possibles(Piece(i))

                    pices_count += len(possis)

            if pices_count > better_total:
                better_total = pices_count
                better_one = p

        return better_one
    
    def find_possibles(self, piece):

        new_list = self.board.copy()
        possibilites = []

        for i in range(0,4):
            for l in range(0,6):
                if self.verify_insert_piece(i, l, piece, new_list):
                    possibilites.append([i,l])

        ## Some strategies

        if piece.piece_type == 2:
            aux = [[0,5],[1,0]]
            return [i for i in possibilites if i in aux]
        if piece.piece_type == 6:
            aux = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],
                   [2,1],[2,2],[2,3],[2,4],[2,5]]
            return [i for i in possibilites if i in aux]
        if piece.piece_type in [3,4,5]:
            aux = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],
                   [2,0],[2,1],[2,2],[2,3],[2,4],[2,5]]
            return [i for i in possibilites if i in aux]

        return possibilites

    def __str__(self):
        text = '------------------\n'
        for i in self.board:
            text += str(i) + '\n'
        text += '------------------'
        return text
    

