class Game:
    """
    """

    PLAYER_ONE = 0
    PLAYER_TWO = 1
    DRAW = 2
    EMPTY = 0
    BOARD_WIDTH = 7
    BOARD_HEIGHT = 6

    def __init__(self):
        self.board = [[Game.EMPTY] * Game.BOARD_WIDTH for i in range(Game.BOARD_HEIGHT)]
        self.columns = [0] * Game.BOARD_WIDTH
        number_of_moves = 0

    def make_move(self, column):
        self.board[column][self.columns[column]] = self.get_player()
        self.heights[column] += 1
        self.number_of_moves += 1
        assert self.heights[column] < Game.BOARD_HEIGHT, "To many disks"

    def get_player(self):
        if self.number_of_moves % 2 == 0:
            return Game.PLAYER_ONE
        return Game.PLAYER_TWO

    def play(self, seq):
        for index, move in enumerate(seq):
            col = int(move) - 1
            if col < 0 or col >= Game.BOARD_WIDTH or not self.can_make_move(col) or self.is_winning_move(col):
                return index
            self.make_move(col)

        return len(seq)

    def can_make_move(self, column):
        return self.columns[column] < Game.BOARD_HEIGHT

    def get_winner(self):
        pass

    def get_player_at(self, row, col):
        pass

    def get_current_player(self):
        pass
