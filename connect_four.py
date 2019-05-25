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
            elif board[i][j] == "p":
                square = "o"
            elif board[i][j] == "c":
                square = ansiBLUE + "o" + ansiEND
            print(" " + square, end="")
        print("")
    print(ansiTEAL + "     -------------" + ansiEND)
    print(ansiTEAL + "     1 2 3 4 5 6 7" + ansiEND)
    print("")
    return

def findMoveSquaresPawn(board, color, enPassant, square):
    if color == "w":
        colorOpp = "b"
        d = 1
    elif color == "b":
        colorOpp = "w"
        d = -1
    i = square[0]
    j = square[1]
    moveSquares = []
    #One square ahead
    if board[i+d][j] == "  ":
        moveSquares.append([i+d,j])
    #Two squares ahead
    if (color == "w" and i == 1) or (color == "b" and i == 6):
        if board[i+d][j] == "  " and board[i+2*d][j] == "  ":
            moveSquares.append([i+2*d,j])
    #Capture
    if j >= 1:
        if board[i+d][j-1][0] == colorOpp:
            moveSquares.append([i+d,j-1])
    if j <= 6:
        if board[i+d][j+1][0] == colorOpp:
            moveSquares.append([i+d,j+1])
    #en passant
    if enPassant != []:
        iEP = enPassant[0]
        jEP = enPassant[1]
        if i == iEP and abs(j - jEP) == 1:
            moveSquares.append([iEP+d,jEP])
    return moveSquares

def findAttackSquaresPawn(board, color, square):
    if color == "w":
        colorOpp = "b"
        d = 1
    elif color == "b":
        colorOpp = "w"
        d = -1
    i = square[0]
    j = square[1]
    attackSquares = []
    #Capture
    if j >= 1:
        if board[i+d][j-1][0] in [" ",colorOpp]:
            attackSquares.append([i+d,j-1])
    if j <= 6:
        if board[i+d][j+1][0] in [" ",colorOpp]:
            attackSquares.append([i+d,j+1])
    return attackSquares

def inCheck(board, color):
    if color == "w":
        colorOpp = "b"
    elif color == "b":
        colorOpp = "w"
    
    #Piece positions
    squaresPawnOpp   = []
    squaresBishopOpp = []
    squaresKnightOpp = []
    squaresRookOpp   = []
    squaresQueenOpp  = []
    squaresKingOpp   = []
    for i in [0,1,2,3,4,5,6,7]:
        for j in [0,1,2,3,4,5,6,7]:
            if board[i][j][0] == colorOpp:
                if board[i][j][1] == "p":
                    squaresPawnOpp.append([i,j])
                elif board[i][j][1] == "B":
                    squaresBishopOpp.append([i,j])
                elif board[i][j][1] == "N":
                    squaresKnightOpp.append([i,j])
                elif board[i][j][1] == "R":
                    squaresRookOpp.append([i,j])
                elif board[i][j][1] == "Q":
                    squaresQueenOpp.append([i,j])
                elif board[i][j][1] == "K":
                    squaresKingOpp.append([i,j])
            elif board[i][j] == color + "K":
                squareKing = [i,j]
    
    #Possible moves
    attackSquares = []
    for square in squaresPawnOpp:
        attackSquares.extend(findAttackSquaresPawn(board, colorOpp, square))
    for square in squaresBishopOpp:
        attackSquares.extend(findAttackSquaresBishop(board, colorOpp, square))
    for square in squaresKnightOpp:
        attackSquares.extend(findAttackSquaresKnight(board, colorOpp, square))
    for square in squaresRookOpp:
        attackSquares.extend(findAttackSquaresRook(board, colorOpp, square))
    for square in squaresQueenOpp:
        attackSquares.extend(findAttackSquaresQueen(board, colorOpp, square))
    for square in squaresKingOpp:
        attackSquares.extend(findAttackSquaresKing(board, colorOpp, square))
    
    #Determine whether king is in check
    checkFlag = False
    for attackSquare in attackSquares:
        if attackSquare == squareKing:
            checkFlag = True
    return checkFlag

def validColumn(board, column):
    validFlag = False
    if column in ["1","2","3","4","5","6","7"]:
        j = int(column) - 1
        if board[5][j] == " ":
            validFlag = True
    return validFlag

def updateBoard(board, column, player):
    j = int(column) - 1
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
    return

def checkBoardFull(board):
    fullFlag = True
    for j in [0,1,2,3,4,5,6]:
        if board[5][j] == " ":
            fullFlag = False
    return fullFlag

def main():
    #Parameters
    row6 = [" "," "," "," "," "," "," "]
    row5 = [" "," "," "," "," "," "," "]
    row4 = [" "," "," "," "," "," "," "]
    row3 = [" "," "," "," "," "," "," "]
    row2 = [" "," "," "," "," "," "," "]
    row1 = [" "," "," "," "," "," "," "]
    board = [row1,row2,row3,row4,row5,row6]
    columns = ["1","2","3","4","5","6","7"]
    playerWin = False
    computerWin = False
    boardFull = False
        
    #Move loop
    while (not playerWin) and (not computerWin) and (not boardFull):
        printBoard(board)
        column = ""
        while not validColumn(board, column):
            column = input("Column: ")
        board = updateBoard(board, column, "p")
        playerWin = checkWin(board, "p")
        validColumns = [column for column in columns if validColumn(board, column)]
        random.seed()
        random.shuffle(validColumns)
        board = updateBoard(board, validColumns[0], "c")
        computerWin = checkWin(board, "c")
        boardFull = checkBoardFull(board)
    
    printBoard(board)
    printEndGame(playerWin, computerWin, boardFull)
    
    return

if __name__ == "__main__":
    main()
