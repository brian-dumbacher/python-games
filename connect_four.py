#Name:     connect_four.py
#Purpose:  Play connect four
#Author:   Brian Dumbacher

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
            elif board[i][j] == "w":
                square = "x"
            elif board[i][j] == "b":
                square = ansiBLUE + "x" + ansiEND
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

def isLegalMove(board, color, checkFlag, move):
    i0 = move[0][0]
    j0 = move[0][1]
    i1 = move[1][0]
    j1 = move[1][1]
    isKing = (board[i0][j0][1] == "K")
    
    #Castling
    legalCastleFlag = True
    if isKing and abs(j1 - j0) == 2:
        if j1 > j0:
            jMiddle = j0 + 1
        elif j1 < j0:
            jMiddle = j0 - 1
        if checkFlag:
            legalCastleFlag = False
        else:
            row1New = ["  ","  ","  ","  ","  ","  ","  ","  "]
            row2New = ["  ","  ","  ","  ","  ","  ","  ","  "]
            row3New = ["  ","  ","  ","  ","  ","  ","  ","  "]
            row4New = ["  ","  ","  ","  ","  ","  ","  ","  "]
            row5New = ["  ","  ","  ","  ","  ","  ","  ","  "]
            row6New = ["  ","  ","  ","  ","  ","  ","  ","  "]
            row7New = ["  ","  ","  ","  ","  ","  ","  ","  "]
            row8New = ["  ","  ","  ","  ","  ","  ","  ","  "]
            boardNew = [row1New,row2New,row3New,row4New,row5New,row6New,row7New,row8New]
            for i in [0,1,2,3,4,5,6,7]:
                for j in [0,1,2,3,4,5,6,7]:
                    boardNew[i][j] = board[i][j]
            boardNew[i1][jMiddle] = boardNew[i0][j0]
            boardNew[i0][j0] = "  "
            legalCastleFlag = not inCheck(boardNew, color)
    
    #Everything other than castling
    row1New = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row2New = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row3New = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row4New = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row5New = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row6New = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row7New = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row8New = ["  ","  ","  ","  ","  ","  ","  ","  "]
    boardNew = [row1New,row2New,row3New,row4New,row5New,row6New,row7New,row8New]
    for i in [0,1,2,3,4,5,6,7]:
        for j in [0,1,2,3,4,5,6,7]:
            boardNew[i][j] = board[i][j]
    boardNew[i1][j1] = boardNew[i0][j0]
    boardNew[i0][j0] = "  "
    legalFlag = not inCheck(boardNew, color)
    
    return legalCastleFlag and legalFlag

def printStatus(colorMove, checkFlag, checkmateFlag):
    if colorMove == "w":
        print("Turn to move: WHITE")
    elif colorMove == "b":
        print("Turn to move: BLACK")
    if checkFlag:
        print("In check?     YES")
    else:
        print("In check?     NO")
    if checkmateFlag:
        print("Checkmated?   YES")
    else:
        print("Checkmated?   NO")
    print("")
    return

def main():
    #Position setup
    row6 = [" "," "," "," "," "," "," "]
    row5 = [" "," "," "," "," "," "," "]
    row4 = [" "," "," "," "," "," "," "]
    row3 = [" "," "," "," "," "," "," "]
    row2 = [" "," "," "," "," "," "," "]
    row1 = [" "," "," "," "," "," "," "]
    board = [row1,row2,row3,row4,row5,row6]
    
    #Print board
    printBoard(board)
    
    #Piece positions
    squaresPawn   = []
    squaresBishop = []
    squaresKnight = []
    squaresRook   = []
    squaresQueen  = []
    squaresKing   = []
    for i in [0,1,2,3,4,5,6,7]:
        for j in [0,1,2,3,4,5,6,7]:
            if board[i][j][0] == colorMove:
                if board[i][j][1] == "p":
                    squaresPawn.append([i,j])
                elif board[i][j][1] == "B":
                    squaresBishop.append([i,j])
                elif board[i][j][1] == "N":
                    squaresKnight.append([i,j])
                elif board[i][j][1] == "R":
                    squaresRook.append([i,j])
                elif board[i][j][1] == "Q":
                    squaresQueen.append([i,j])
                elif board[i][j][1] == "K":
                    squaresKing.append([i,j])
    
    #Possible moves
    movesPawn = []
    for square in squaresPawn:
        movesPawn.extend([[square, moveSquare] for moveSquare in findMoveSquaresPawn(board, colorMove, enPassant, square)])
    movesLegalPawn = [move for move in movesPawn if isLegalMove(board, colorMove, checkFlag, move)]
    movesCoordPawn = [convertMoveCoord(move) for move in movesLegalPawn]
    movesCoordPawn.sort()
    
    #Print status
    checkmateFlag = (len(movesCoord) == 0)
    printStatus(colorMove, checkFlag, checkmateFlag)
    
    #Print moves
    print("Possible Moves:")
    printMovesCoord("Pawn   | ", movesCoordPawn)
    print("")
    return

if __name__ == "__main__":
    main()
