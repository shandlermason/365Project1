"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
board = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]
print(board)

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    X_number = 0
    O_number = 0

    for x in board:
    	for y in x:
    		print(y)
    		if y == "X":
    			X_number += 1
    		if y == "O":
    			O_number += 1
    print(X_number,"Xs")
    print(O_number,"Os")
    if X_number == O_number:
        return X
    else:
        return O



def actions(board):
    moves = {(3,3)}
    i = -1
    for x in board:
    	i += 1
    	j = -1
    	for y in x:
    		j += 1
    		if board[i][j] == EMPTY:
    			moves.add((i,j))
    moves.remove((3,3))
    return moves


def result(board, action):
    b = copy.deepcopy(board)
    if action == None:
    	print("Error")
    elif board[action[0]][action[1]] == EMPTY:
        b[action[0]][action[1]] = player(board)
    else:
        print("Move is not valid")
    return b



def winner(board):
    a = (board[0][0] == board[0][1] == board[0][2] == ("X" or "O"))
    b = (board[1][0] == board[1][1] == board[1][2] == ("X" or "O"))
    c = (board[2][0] == board[2][1] == board[2][2] == ("X" or "O"))
    d = (board[0][0] == board[1][0] == board[2][0] == ("X" or "O"))
    e = (board[0][1] == board[1][1] == board[2][1] == ("X" or "O"))
    f = (board[0][2] == board[1][2] == board[2][2] == ("X" or "O"))
    g = (board[0][0] == board[1][1] == board[2][2] == ("X" or "O"))
    h = (board[2][0] == board[1][1] == board[0][2] == ("X" or "O"))

    return a or b or c or d or e or f or g or h



def terminal(board):
    game = ""
    i = -1
    for x in board:
        i += 1
        j = -1
        for y in x:
            j += 1
            if board[i][j] != EMPTY:
                game = "over"
            else:
                game = "not over"
    if game == "over" or winner:
    	return True
    else:
    	return False

def utility(board):
    utility = 0

    if board[0][0] == board[0][1] == board[0][2] == ("X"):
    	utility = 1
    if board[1][0] == board[1][1] == board[1][2] == ("X"):
    	utility = 1
    if board[2][0] == board[2][1] == board[2][2] == ("X"):
    	utility = 1
    if board[0][0] == board[1][0] == board[2][0] == ("X"):
    	utility = 1
    if board[0][1] == board[1][1] == board[2][1] == ("X"):
    	utility = 1
    if board[0][2] == board[1][2] == board[2][2] == ("X"):
    	utility = 1
    if board[0][0] == board[1][1] == board[2][2] == ("X"):
    	utility = 1
    if board[2][0] == board[1][1] == board[0][2] == ("X"):
    	utility = 1
    if board[0][0] == board[0][1] == board[0][2] == ("O"):
    	utility = -1
    if board[1][0] == board[1][1] == board[1][2] == ("O"):
    	utility = -1
    if board[2][0] == board[2][1] == board[2][2] == ("O"):
    	utility = -1
    if board[0][0] == board[1][0] == board[2][0] == ("O"):
    	utility = -1
    if board[0][1] == board[1][1] == board[2][1] == ("O"):
    	utility = -1
    if board[0][2] == board[1][2] == board[2][2] == ("O"):
    	utility = -1
    if board[0][0] == board[1][1] == board[2][2] == ("O"):
    	utility = -1
    if board[2][0] == board[1][1] == board[0][2] == ("O"):
    	utility = -1




def minimax(board):
    EMPTY = None
    X = "X"
    O = "O"
    board = [[EMPTY, EMPTY, EMPTY], [X, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

    optimal = {(3,3)}
    move = ""

    #Check if this is first or second move
    i = -1
    for x in board:
    	i += 1
    	j = -1
    	for y in x:
    		j += 1
    		if board[i][j] != EMPTY:
    			if move == "Second":
    				move = "Other"
    			else:
    				move = "Second"
    if move == "":
    	move = "First"

    if move == "First":
    	optimal.add((0,0))
    	optimal.add((0,2))
    	optimal.add((2,0))
    	optimal.add((2,2))
    elif move == "Second":
    	if board[1][1] == EMPTY:
    		optimal.add((1,1))
    	else:
    		optimal.add((0,0))
    		optimal.add((0,2))
    		optimal.add((2,0))
    		optimal.add((2,2))
    #If you can make 3 in a row, complete it
    #If the opponent can make 3 in a row, stop them
    #If you can make 2 in a row, do it

    optimal.remove((3,3))
    #print(optimal)
    #print(random.choice(tuple(optimal)))
