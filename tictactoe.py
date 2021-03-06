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
    #Variables for X's and O's
    X_number = 0
    O_number = 0

    for x in board:
    #Checks each space on board for X's and O's
    	for y in x:
    		if y == "X":
    			X_number += 1
    		if y == "O":
    			O_number += 1
    #Has to be X's turn if X's and O's are equal
    if X_number == O_number:
        return X
    else:
        return O



def actions(board):
 #Initializing set
    moves = {(3,3)}
    i = -1
 #Checking for empty spaces
    for x in board:
    	i += 1
    	j = -1
    	for y in x:
    		j += 1
    		if board[i][j] == EMPTY:
    			moves.add((i,j))
    #Removing dummy tuple
    moves.remove((3,3))
    return moves


def result(board, action):
 #Returns board with proper moves
 #Creating a deep copy of board
    b = copy.deepcopy(board)
 #Checking if move is valid
    if action == None:
    	print("Error")
    elif board[action[0]][action[1]] == EMPTY:
        b[action[0]][action[1]] = player(board)
    else:
        print("Move is not valid")
    return b



def winner(board):
#Check if there's a winner
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
#Stops game if winner or no spaces
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
#Returns utility
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
    return utility



def minimax(board):
#Makes sure AI returns most optimal move
    optimal = {(3,3)}
    turn = player(board)
    if turn == X:
        opponent = O
    else:
        opponent = X
    move_int = 0
    move = ""

#Check if this is first or second move
    i = -1
    for x in board:
    	i += 1
    	j = -1
    	for y in x:
    		j += 1
    		if board[i][j] != EMPTY:
    			move_int += 1
    if move_int == 0:
    	move = "First"
    elif move_int == 1:
        move = "Second"
    elif move_int > 1:
        move = "Other"


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
    else:
        #If you can make 3 in a row, complete it
        #(0,0)
        if board[0][0] == None and ((board[0][1] == board[0][2] == turn) or (board[1][0] == board[2][0] == turn) or (board[1][1] == board[2][2] == turn)):
            print("Returning (0,0) to match 3 in a row")
            return (0,0)
        #(0,1)
        if board[0][1] == None and ((board[0][0] == board[0][2] == turn) or (board[1][1] == board[2][1] == turn)):
            print("Returning (0,1) to match 3 in a row")
            return (0,1)
      #(0,2)
        if board[0][2] == None and ((board[0][0] == board[0][1] == turn) or (board[1][1] == board[2][0] == turn) or (board[1][2] == board[2][2] == turn)):
            print("Returning (0,2) to match 3 in a row")
            return (0,2)
        #(1,0)
        if board[1][0] == None and ((board[0][0] == board[2][0] == turn) or (board[1][1] == board[1][2] == turn)):
            print("Returning (1,0) to match 3 in a row")
            return (1,0)
        #(1,1)
        if board[1][1] == None and ((board[0][0] == board[2][2] == turn) or (board[0][2] == board[2][0] == turn) or (board[1][0] == board[1][2] == turn) or (board[0][1] == board[2][1] == turn)):
            print("Returning (1,1) to match 3 in a row")
            return (1,1)
        #(1,2)
        if board[1][2] == None and ((board[1][0] == board[1][1] == turn) or (board[0][2] == board[2][2] == turn)):
            print("Returning (1,2) to match 3 in a row")
            return (1,2)
        #(2,0)
        if board[2][0] == None and ((board[2][1] == board[2][2] == turn) or (board[1][0] == board[0][0] == turn) or (board[1][1] == board[0][2] == turn)):
            print("Returning (2,0) to match 3 in a row")
            return (2,0)
        #(2,1)
        if board[2][1] == None and ((board[2][0] == board[2][2] == turn) or (board[1][1] == board[0][1] == turn)):
            print("Returning (2,1) to match 3 in a row")
            return (2,1)
        #(2,2)
        if board[2][2] == None and ((board[2][0] == board[2][1] == turn) or (board[1][1] == board[0][0] == turn) or (board[1][2] == board[0][2] == turn)):
            print("Returning (2,2) to match 3 in a row")
            return (2,2)


        #If the opponent can make 3 in a row, stop them
        #(0,0)
        if board[0][0] == None and ((board[0][1] == board[0][2] == opponent) or (board[1][0] == board[2][0] == opponent) or (board[1][1] == board[2][2] == opponent)):
            print("Returning (0,0) to block opponent")
            return (0,0)
        #(0,1)
        if board[0][1] == None and ((board[0][0] == board[0][2] == opponent) or (board[1][1] == board[2][1] == opponent)):
            print("Returning (0,1) to block opponent")
            return (0,1)
      #(0,2)
        if board[0][2] == None and ((board[0][0] == board[0][1] == opponent) or (board[1][1] == board[2][0] == opponent) or (board[1][2] == board[2][2] == opponent)):
            print("Returning (0,2) to block opponent")
            return (0,2)
        #(1,0)
        if board[1][0] == None and ((board[0][0] == board[2][0] == opponent) or (board[1][1] == board[1][2] == opponent)):
            print("Returning (1,0) to block opponent")
            return (1,0)
        #(1,1)
        if board[1][1] == None and ((board[0][0] == board[2][2] == opponent) or (board[0][2] == board[2][0] == opponent) or (board[1][0] == board[1][2] == opponent) or (board[0][1] == board[2][1] == opponent)):
            print("Returning (1,1) to block opponent")
            return (1,1)
        #(1,2)
        if board[1][2] == None and ((board[1][0] == board[1][1] == opponent) or (board[0][2] == board[2][2] == opponent)):
            print("Returning (1,2) to block opponent")
            return (1,2)
        #(2,0)
        if board[2][0] == None and ((board[2][1] == board[2][2] == opponent) or (board[1][0] == board[0][0] == opponent) or (board[1][1] == board[0][2] == opponent)):
            print("Returning (2,0) to block opponent")
            return (2,0)
        #(2,1)
        if board[2][1] == None and ((board[2][0] == board[2][2] == opponent) or (board[1][1] == board[0][1] == opponent)):
            print("Returning (2,1) to block opponent")
            return (2,1)
        #(2,2)
        if board[2][2] == None and ((board[2][0] == board[2][1] == opponent) or (board[1][1] == board[0][0] == opponent) or (board[1][2] == board[0][2] == opponent)):
            print("Returning (2,2) to block opponent")
            return (2,2)


#If you can make 2 in a row, do it
        #(0,0)
        if board[0][0] == None and ((board[0][1] == turn and board[0][2] == EMPTY) or (board[0][1] == EMPTY and board[0][2] == turn) or (board[1][0] == turn and board[2][0] == EMPTY) or (board[1][0] == EMPTY and board[2][0] == turn) or (board[1][1] == turn and board[2][2] == EMPTY) or (board[1][1] == EMPTY and board[2][2] == turn)):
            print("Returning (0,0) to get 2 in a row")
            return (0,0)
        #(0,1)
        if board[0][1] == None and ((board[0][0] == turn and board[0][2] == EMPTY) or (board[0][0] == EMPTY and board[0][2] == turn) or (board[1][1] == turn and board[2][1] == EMPTY) or (board[1][1] == EMPTY and board[2][1] == turn)):
            print("Returning (0,1) to get 2 in a row")
            return (0,1)
        #(0,2)
        if board[0][2] == None and ((board[0][0] == turn and board[0][1] == EMPTY) or (board[0][0] == EMPTY and board[0][1] == turn) or (board[1][2] == turn and board[2][2] == EMPTY) or (board[1][2] == EMPTY and board[2][2] == turn) or (board[1][1] == turn and board[2][0] == EMPTY) or (board[1][1] == EMPTY and board[2][0] == turn)):
            print("Returning (0,2) to get 2 in a row")
            return (0,2)
        #(1,0)
        if board[1][0] == None and ((board[0][0] == turn and board[2][0] == EMPTY) or (board[0][0] == EMPTY and board[2][0] == turn) or (board[1][1] == turn and board[1][2] == EMPTY) or (board[1][1] == EMPTY and board[1][2] == turn)):
            print("Returning (1,0) to get 2 in a row")
            return (1,0)
        #(1,1)
        if board[1][1] == None and ((board[0][0] == turn and board[2][2] == EMPTY) or (board[0][0] == EMPTY and board[2][2] == turn) or (board[0][2] == turn and board[2][0] == EMPTY) or (board[0][2] == EMPTY and board[2][0] == turn) or (board[1][0] == turn and board[1][2] == EMPTY) or (board[1][0] == EMPTY and board[1][2] == turn) or (board[0][1] == turn and board[2][1] == EMPTY) or (board[0][1] == EMPTY and board[2][1] == turn)):
            print("Returning (1,1) to get 2 in a row")
            return (1,1)
        #(1,2)
        if board[1][2] == None and ((board[0][2] == turn and board[2][2] == EMPTY) or (board[0][2] == EMPTY and board[2][2] == turn) or (board[1][1] == turn and board[1][0] == EMPTY) or (board[1][1] == EMPTY and board[1][0] == turn)):
            print("Returning (1,2) to get 2 in a row")
            return (1,2)
        #(2,0)
        if board[2][0] == None and ((board[2][1] == turn and board[2][2] == EMPTY) or (board[0][1] == EMPTY and board[0][0] == turn) or (board[1][0] == turn and board[0][0] == EMPTY) or (board[1][0] == EMPTY and board[0][0] == turn) or (board[1][1] == turn and board[0][2] == EMPTY) or (board[1][1] == EMPTY and board[0][2] == turn)):
            print("Returning (2,0) to get 2 in a row")
            return (2,0)
        #(2,1)
        if board[2][1] == None and ((board[2][0] == turn and board[2][2] == EMPTY) or (board[2][0] == EMPTY and board[2][2] == turn) or (board[0][1] == turn and board[1][1] == EMPTY) or (board[0][1] == EMPTY and board[1][1] == turn)):
            print("Returning (2,1) to get 2 in a row")
            return (2,1)
        #(0,2)
        if board[2][2] == None and ((board[2][0] == turn and board[2][1] == EMPTY) or (board[2][0] == EMPTY and board[2][1] == turn) or (board[1][2] == turn and board[0][2] == EMPTY) or (board[1][2] == EMPTY and board[0][2] == turn) or (board[1][1] == turn and board[0][0] == EMPTY) or (board[1][1] == EMPTY and board[0][0] == turn)):
            print("Returning (2,2) to get 2 in a row")
            return (0,2)
        i = -1
        for x in board:
         i += 1
         j = -1
         for y in x:
         	j += 1
         	if board[i][j] == EMPTY:
         		optimal.add((i,j))

    #If you can make 3 in a row, complete it
    #If the opponent can make 3 in a row, stop them
    #If you can make 2 in a row, do it

    optimal.remove((3,3))
    return random.choice(tuple(optimal))
    #print(optimal)
    #print(random.choice(tuple(optimal)))
