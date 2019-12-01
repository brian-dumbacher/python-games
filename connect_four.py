#Name:     connect_four.py
#Purpose:  Play connect four
#Author:   Brian Dumbacher

import random

def printBoard(board):
    ansiGREY = "\x1b[90m"
    ansiBLUE = "\x1b[94m"
    ansiTEAL = "\x1b[96m"
    ansiEND  = "\x1b[0m"
    print("")
    for i in [5,4,3,2,1,0]:
        print(ansiTEAL + "   |" + ansiEND, end="")
        for j in [0,1,2,3,4,5,6]:
            if board[i][j] == " ":
                square = ansiGREY + "." + ansiEND
            elif board[i][j] == "h":
                square = "o"
            elif board[i][j] == "c":
                square = ansiBLUE + "o" + ansiEND
            print(" " + square, end="")
        print("")
    print(ansiTEAL + "     -------------" + ansiEND)
    print(ansiTEAL + "     1 2 3 4 5 6 7" + ansiEND)
    print("")
    return

def validMove(board, move):
    return True if move in ["1","2","3","4","5","6","7"] and board[5][int(move) - 1] == " " else False

def updateBoard(board, move, player):
    j = int(move) - 1
    if board[0][j] == " ":
        board[0][j] = player
    elif board[1][j] == " ":
        board[1][j] = player
    elif board[2][j] == " ":
        board[2][j] = player
    elif board[3][j] == " ":
        board[3][j] = player
    elif board[4][j] == " ":
        board[4][j] = player
    elif board[5][j] == " ":
        board[5][j] = player
    return board

def checkWin(board, player):
    #Rows
    for i in [0,1,2,3,4,5]:
        for j in [0,1,2,3]:
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                return True
    #Columns
    for j in [0,1,2,3,4,5,6]:
        for i in [0,1,2]:
            if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
                return True
    #SW-NE Diagonals
    for j in [0,1,2,3]:
        for i in [0,1,2]:
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                return True
    #SE-NW Diagonals
    for j in [3,4,5,6]:
        for i in [0,1,2]:
            if board[i][j] == player and board[i+1][j-1] == player and board[i+2][j-2] == player and board[i+3][j-3] == player:
                return True
    return False

def winMove(board, move, player):
    row6Win = [" "," "," "," "," "," "," "]
    row5Win = [" "," "," "," "," "," "," "]
    row4Win = [" "," "," "," "," "," "," "]
    row3Win = [" "," "," "," "," "," "," "]
    row2Win = [" "," "," "," "," "," "," "]
    row1Win = [" "," "," "," "," "," "," "]
    boardWin = [row1Win,row2Win,row3Win,row4Win,row5Win,row6Win]
    for i in [0,1,2,3,4,5]:
        for j in [0,1,2,3,4,5,6]:
            boardWin[i][j] = board[i][j]
    boardWin = updateBoard(boardWin, move, player)
    return checkWin(boardWin, player)

def loseMove(board, move, player):
    if player == "c":
        playerOpp = "h"
    elif player == "h":
        playerOpp = "c"
    
    row6New = [" "," "," "," "," "," "," "]
    row5New = [" "," "," "," "," "," "," "]
    row4New = [" "," "," "," "," "," "," "]
    row3New = [" "," "," "," "," "," "," "]
    row2New = [" "," "," "," "," "," "," "]
    row1New = [" "," "," "," "," "," "," "]
    boardNew = [row1New,row2New,row3New,row4New,row5New,row6New]
    for i in [0,1,2,3,4,5]:
        for j in [0,1,2,3,4,5,6]:
            boardNew[i][j] = board[i][j]
    boardNew = updateBoard(boardNew, move, player)
    
    columns = ["1","2","3","4","5","6","7"]
    validMovesNew = [move for move in columns if validMove(boardNew, move)]
    for move in validMovesNew:
        if winMove(boardNew, move, playerOpp):
            return True
    return False

def getMoveComputer(board, moveHuman):
    #Classify valid moves
    columns = ["1","2","3","4","5","6","7"]
    validMoves = [move for move in columns if validMove(board, move)]
    winMoves = []
    otherMoves = []
    loseMoves = []
    for move in validMoves:
        if winMove(board, move, "c"):
            winMoves.append(move)
        elif loseMove(board, move, "c"):
            loseMoves.append(move)
        else:
            otherMoves.append(move)
    #Randomly choose move
    random.seed()
    if len(winMoves) > 0:
        random.shuffle(winMoves)
        computerMove = winMoves[0]
    elif len(otherMoves) > 0:
        random.shuffle(otherMoves)
        computerMove = otherMoves[0]
    else:
        random.shuffle(loseMoves)
        computerMove = loseMoves[0]
    return computerMove

def checkBoardFull(board):
    for j in [0,1,2,3,4,5,6]:
        if board[5][j] == " ":
            return False
    return True

def printEndGame(winHuman, winComputer):
    print("==================================================")
    if winHuman:
        print("You win!")
    elif winComputer:
        print("You lose.")
    else:
        print("Tie game.")
    print("==================================================")
    print("")
    return

def playConnectFour():
    #Board setup
    row6 = [" "," "," "," "," "," "," "]
    row5 = [" "," "," "," "," "," "," "]
    row4 = [" "," "," "," "," "," "," "]
    row3 = [" "," "," "," "," "," "," "]
    row2 = [" "," "," "," "," "," "," "]
    row1 = [" "," "," "," "," "," "," "]
    board = [row1,row2,row3,row4,row5,row6]
    winHuman = False
    winComputer = False
    boardFull = False
        
    #Move loop
    while (not winHuman) and (not winComputer) and (not boardFull):
        printBoard(board)
        #Human move
        moveHuman = ""
        while not validMove(board, moveHuman):
            moveHuman = input("Column: ")
        board = updateBoard(board, moveHuman, "h")
        winHuman = checkWin(board, "h")
        #Computer move
        if not winHuman:
            moveComputer = getMoveComputer(board, moveHuman)        
            board = updateBoard(board, moveComputer, "c")
            winComputer = checkWin(board, "c")
            boardFull = checkBoardFull(board)
    
    printBoard(board)
    printEndGame(winHuman, winComputer)
    return

def main():
    #Parameters
    loopFlag = True
    
    #Game loop
    while loopFlag:
        playConnectFour()
        newGame = ""
        while newGame not in ["n", "no", "y", "yes"]:
            newGame = input("Another game? Y/N: ")
            newGame = newGame.lower()
        if newGame in ["n", "no"]:
            loopFlag = False
    print("")
    return

if __name__ == "__main__":
    main()
