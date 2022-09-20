"""
Tic Tac Toe Player
"""
import copy
import math
from sys import float_info

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
    x_count=0
    o_count=0
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j]==X:
                x_count+=1
            elif board[i][j]==O:
                o_count+=1
    if x_count>o_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions=set()

    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            if board[i][j]==EMPTY:
                possible_actions.add((i,j))

    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result=copy.deepcopy(board)
    result[action[0]][action[1]]=player(board)
    return result

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    if all(i==board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i==board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i==board[2][0] for i in board[2]):
        return board[2][0]
    #check columns
    elif board[0][0]==board[1][0] and board[1][0]==board[2][0]:
        return board[0][0]
    elif board[0][1]==board[1][1] and board[1][1]==board[2][1]:
        return board[0][1]
    elif board[0][2]==board[1][2] and board[1][2]==board[2][2]:
        return board[0][2]
        
    #diagonals
    elif board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        return board[0][0]
    elif board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        return board[0][2]

    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)==X or winner(board)==O or (not any (EMPTY in x for x in board)):
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board)==X:
            return 1
        elif winner(board)==O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board)==X:
            val,move=maximum(board)
            return move
        else:
            val,move=minimum(board)
            return move


def maximum(board):
    if terminal(board):
        return utility(board),None
    a=float('-inf')
    move=None
    for action in actions(board):
        tempval,act=minimum(result(board,action))
        if tempval>a:
            a=tempval
            move=action
            if a==1:
                return a,move

    return a,move

def minimum(board):
    if terminal(board):
        return utility(board),None
    a=float('inf')
    move=None
    for action in actions(board):
        tempval,act=maximum(result(board,action))
        if tempval<a:
            a=tempval
            move=action
            if a==-1:
                return a,move
    return a,move