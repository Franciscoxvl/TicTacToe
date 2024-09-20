"""
Tic Tac Toe Player
"""
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    N_X = 0
    N_O = 0

    for row in board:
        for column in row:
            if column == "X":
                N_X += 1
            elif column == "O":
                N_O += 1
    
    if (N_X == 0 and N_O == 0) or (N_X == N_O):
        return "X"
    else:
        return "O"
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for row in range(0, 3):
        for column in range(0, 3):
            if board[row][column] == None:
                actions.add((row, column))

    return actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    actual_player = player(board)
    new_board = copy.deepcopy(board)

    valid_actions = actions(board)

    if action in valid_actions:
        new_board[action[0]][action[1]] = actual_player
        return new_board
    else:
        raise NameError("Action is not valid!")

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win_positions = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],[(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],[(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]

    for wp in win_positions:
        resultado_X = all(board[x][y] == 'X' for x, y in wp)
        resultado_O = all(board[x][y] == 'O' for x, y in wp)
        if resultado_X:
            return "X"
        elif resultado_O:
            return "O"

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # parcial_result = winner()
    if winner(board):
        return True
    else:
        for row in board:
            for column in row:
                if column == None:
                    return False

    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == False:
        return None
    else:
        win_player = winner(board)

    if win_player == "X":
        return 1
    elif win_player == "O":
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    moves_values = ()
    new_board = copy.deepcopy(board)

    if terminal(board):
        return None
    else:
        current_player = player(board)

        if current_player == "X":
            for a in actions(board):
                if winner(result(board, a)) == "X":
                    return a
            
            for a in actions(new_board):
                new_board[a[0]][a[1]] = "O"
                if winner(new_board) == "O":
                    return a
                else:
                    new_board[a[0]][a[1]] = EMPTY

            moves_values = Max_Value(board)
        else:
            for a in actions(board):
                if winner(result(board, a)) == "O":
                    return a
            
            for a in actions(new_board):
                new_board[a[0]][a[1]] = "X"
                if winner(new_board) == "X":
                    return a
                else:
                    new_board[a[0]][a[1]] = EMPTY

            moves_values = Min_Value(board)
        
        if len(moves_values[1]) > 1:
            aleatorio = random.randint(0, len(moves_values[1])-1)
            return moves_values[1][aleatorio]
        else:
            return moves_values[1][0]
        
    raise NotImplementedError

def Max_Value(board):
    possible_states = []
    
    if terminal(board):
        return utility(board)
    
    v = float('-inf')
    aux = 0
    var = 0
    for action in actions(board):

        next_board = result(board, action)
        min_value = Min_Value(next_board)

        if type(min_value) != int:
            aux = v
            var = min_value[0]
            v = max(v, min_value[0] )
        else:
            aux = v
            var = min_value
            v = max(v, min_value)

        if len(possible_states) == 0 or v == var:          
            possible_states.append(action)
        elif v > aux:
            possible_states[0] = action
    return v, possible_states


def Min_Value(board):
    possible_states = []

    if terminal(board):
        return utility(board) 
    
    v = float('inf')
    aux = 0     
    for action in actions(board):
        max_value = Max_Value(result(board, action))

        if type(max_value) != int :
            aux = v
            v = min(v, max_value[0])
        else:
            aux = v
            v = min(v, max_value)

        if len(possible_states) == 0 or v == aux:          
            possible_states.append(action)
        elif v < aux:
            possible_states[0] = action

    return v, possible_states

