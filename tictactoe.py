"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None
board = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]]

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
    a = (board[0][0] == board[0][1] == board[0][2] == X)
    b = (board[1][0] == board[1][1] == board[1][2] == X)
    c = (board[2][0] == board[2][1] == board[2][2] == X)
    d = (board[0][0] == board[1][0] == board[2][0] == X)
    e = (board[0][1] == board[1][1] == board[2][1] == X)
    f = (board[0][2] == board[1][2] == board[2][2] == X)
    g = (board[0][0] == board[1][1] == board[2][2] == X)
    h = (board[2][0] == board[1][1] == board[0][2] == X)
    i = (board[0][0] == board[0][1] == board[0][2] == O)
    j = (board[1][0] == board[1][1] == board[1][2] == O)
    k = (board[2][0] == board[2][1] == board[2][2] == O)
    l = (board[0][0] == board[1][0] == board[2][0] == O)
    m = (board[0][1] == board[1][1] == board[2][1] == O)
    n = (board[0][2] == board[1][2] == board[2][2] == O)
    o = (board[0][0] == board[1][1] == board[2][2] == O)
    p = (board[2][0] == board[1][1] == board[0][2] == O)

    if a or b or c or d or e or f or g or h:
    	return X
    elif i or j or k or l or m or n or o or p:
    	return O
    else:
    	return None



def terminal(board):
    spaces = 0
    i = -1
    for x in board:
    	i += 1
    	j = -1
    	for y in x:
    		j += 1
    		if board[i][j] != EMPTY:
    			spaces += 1
    return spaces == 9 or winner(board) != None


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
    return random.choice(tuple(optimal))
    #print(optimal)
    #print(random.choice(tuple(optimal)))
