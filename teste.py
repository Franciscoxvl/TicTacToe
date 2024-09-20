from tictactoe import minimax

EMPTY = None

board = [[EMPTY,"X","O"],
        [EMPTY,"X","O"],
        [EMPTY,EMPTY,EMPTY]]

print(minimax(board))
