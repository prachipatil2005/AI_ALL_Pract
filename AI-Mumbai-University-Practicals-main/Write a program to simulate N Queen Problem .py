import numpy as np

global N
N = 4

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],'\t',end=' ')
        print()
def isSafe(board,row,col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i , j in zip(range(row , -1 , -1),range(col, -1 , -1)):
        if board[i][j] == 1:
            return False
    for i , j in zip(range(row , N , 1),range(col, -1 , -1)):
        if board[i][j] == 1:
            return False
    return True
def solveNQUtil(board, col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board , i , col):
            board[i][col] = 1
            if solveNQUtil(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False
def solveNQ():
    board = np.zeros((4 , 4))
    print('Initial Board : \n',board)
    if solveNQUtil(board , 0) == False:
        print('Solution doesn\'t exist')
        return False
    print('\nBoard after the N Queen Solution : \n')
    printSolution(board)
    return True
#Driver program to test above function
solveNQ()