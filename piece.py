class Piece:

    form = None
    height = 0
    width = 0
    piece_type = 0

    def __init__(self, type):

        if type == 1:
            self.form = [[1]]
            self.height = 1
            self.width = 1
            self.piece_type = type
        if type == 2:
            self.form = [[1],[1],[1]]
            self.height = 3
            self.width = 1
            self.piece_type = type
        if type == 3:
            self.form = [[1,1],[1,1]]
            self.height = 2
            self.width = 2
            self.piece_type = type
        if type == 4:
            self.form = [[1,1,0],[0,1,1]]
            self.height = 2
            self.width = 3
            self.piece_type = type
        if type == 5:
            self.form = [[1,0],[1,1]]
            self.height = 2
            self.width = 2
            self.piece_type = type
        if type == 6:
            self.form = [[1,1],[0,1]]
            self.height = 2
            self.width = 2
            self.piece_type = type

    def __str__(self):
        text = '------------------\n'
        for i in self.form:
            text += str(i) + '\n'
        text += '------------------'
        return text
