#Name:     chess.py
#Purpose:  Given a legal chess position, determine all possible moves
#Author:   Brian Dumbacher

def printBoard(board):
    ansiGREY = "\x1b[90m"
    ansiBLUE = "\x1b[94m"
    ansiTEAL = "\x1b[96m"
    ansiEND  = "\x1b[0m"
    print("")
    for i in [7,6,5,4,3,2,1,0]:
        print(ansiTEAL + " " + str(i+1) + " |" + ansiEND, end="")
        for j in [0,1,2,3,4,5,6,7]:
            if board[i][j] == "  ":
                square = ansiGREY + "." + ansiEND
            elif board[i][j][0] == "w":
                square = board[i][j][1]
            elif board[i][j][0] == "b":
                square = ansiBLUE + board[i][j][1] + ansiEND
            print(" " + square, end="")
        print("")
    print(ansiTEAL + "     ---------------" + ansiEND)
    print(ansiTEAL + "     a b c d e f g h" + ansiEND)
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

def findMoveSquaresBishop(board, color, square):
    if color == "w":
        colorOpp = "b"
    elif color == "b":
        colorOpp = "w"
    i = square[0]
    j = square[1]
    moveSquares = []
    #Up-Right
    blocked = False
    numSquares = min([7-i,7-j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i+d][j+d] == "  ":
                moveSquares.append([i+d,j+d])
            else:
                blocked = True
                if board[i+d][j+d][0] == colorOpp:
                    moveSquares.append([i+d,j+d])
    #Down-Right
    blocked = False
    numSquares = min([i,7-j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i-d][j+d] == "  ":
                moveSquares.append([i-d,j+d])
            else:
                blocked = True
                if board[i-d][j+d][0] == colorOpp:
                    moveSquares.append([i-d,j+d])
    #Down-Left
    blocked = False
    numSquares = min([i,j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i-d][j-d] == "  ":
                moveSquares.append([i-d,j-d])
            else:
                blocked = True
                if board[i-d][j-d][0] == colorOpp:
                    moveSquares.append([i-d,j-d])
    #Up-Left
    blocked = False
    numSquares = min([7-i,j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i+d][j-d] == "  ":
                moveSquares.append([i+d,j-d])
            else:
                blocked = True
                if board[i+d][j-d][0] == colorOpp:
                    moveSquares.append([i+d,j-d])
    return moveSquares

def findMoveSquaresKnight(board, color, square):
    if color == "w":
        colorOpp = "b"
    elif color == "b":
        colorOpp = "w"
    i = square[0]
    j = square[1]
    moveSquaresEight = [[i+2,j+1],[i+1,j+2],[i-1,j+2],[i-2,j+1],[i-2,j-1],[i-1,j-2],[i+1,j-2],[i+2,j-1]]
    moveSquares = []
    for moveSquare in moveSquaresEight:
        if moveSquare[0] in [0,1,2,3,4,5,6,7] and moveSquare[1] in [0,1,2,3,4,5,6,7]:
            if board[moveSquare[0]][moveSquare[1]][0] in [" ", colorOpp]:
                moveSquares.append(moveSquare)
    return moveSquares

def findMoveSquaresRook(board, color, square):
    if color == "w":
        colorOpp = "b"
    elif color == "b":
        colorOpp = "w"
    i = square[0]
    j = square[1]
    moveSquares = []
    #Up
    blocked = False
    for z in [ii for ii in [1,2,3,4,5,6,7] if ii > i]:
        if not blocked:
            if board[z][j] == "  ":
                moveSquares.append([z,j])
            else:
                blocked = True
                if board[z][j][0] == colorOpp:
                    moveSquares.append([z,j])
    #Down
    blocked = False
    for z in [ii for ii in [6,5,4,3,2,1,0] if ii < i]:
        if not blocked:
            if board[z][j] == "  ":
                moveSquares.append([z,j])
            else:
                blocked = True
                if board[z][j][0] == colorOpp:
                    moveSquares.append([z,j])
    #Right
    blocked = False
    for z in [jj for jj in [1,2,3,4,5,6,7] if jj > j]:
        if not blocked:
            if board[i][z] == "  ":
                moveSquares.append([i,z])
            else:
                blocked = True
                if board[i][z][0] == colorOpp:
                    moveSquares.append([i,z])
    #Left
    blocked = False
    for z in [jj for jj in [6,5,4,3,2,1,0] if jj < j]:
        if not blocked:
            if board[i][z] == "  ":
                moveSquares.append([i,z])
            else:
                blocked = True
                if board[i][z][0] == colorOpp:
                    moveSquares.append([i,z])
    return moveSquares

def findMoveSquaresQueen(board, color, square):
    return findMoveSquaresBishop(board, color, square) + findMoveSquaresRook(board, color, square)

def findMoveSquaresKing(board, color, canCastleKingside, canCastleQueenside, square):
    if color == "w":
        colorOpp = "b"
    elif color == "b":
        colorOpp = "w"
    i = square[0]
    j = square[1]
    moveSquaresEight = [[i+1,j],[i+1,j+1],[i,j+1],[i-1,j+1],[i-1,j],[i-1,j-1],[i,j-1],[i+1,j-1]]
    moveSquares = []
    for moveSquare in moveSquaresEight:
        if moveSquare[0] in [0,1,2,3,4,5,6,7] and moveSquare[1] in [0,1,2,3,4,5,6,7]:
            if board[moveSquare[0]][moveSquare[1]][0] in [" ", colorOpp]:
                moveSquares.append(moveSquare)
    #Castling
    if canCastleKingside:
        if board[i][j+1] == "  " and board[i][j+2] == "  " and board[i][j+3] == (color + "R"):
            moveSquares.append([i, j+2])
    if canCastleQueenside:
        if board[i][j-1] == "  " and board[i][j-2] == "  " and board[i][j-3] == "  " and board[i][j-4] == (color + "R"):
            moveSquares.append([i, j-2])
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
        if board[i+d][j-1][0] in [" ", colorOpp]:
            attackSquares.append([i+d,j-1])
    if j <= 6:
        if board[i+d][j+1][0] in [" ", colorOpp]:
            attackSquares.append([i+d,j+1])
    return attackSquares

def findAttackSquaresBishop(board, color, square):
    return findMoveSquaresBishop(board, color, square)

def findAttackSquaresKnight(board, color, square):
    return findMoveSquaresKnight(board, color, square)

def findAttackSquaresRook(board, color, square):
    return findMoveSquaresRook(board, color, square)

def findAttackSquaresQueen(board, color, square):
    return findMoveSquaresQueen(board, color, square)

def findAttackSquaresKing(board, color, square):
    if color == "w":
        colorOpp = "b"
    elif color == "b":
        colorOpp = "w"
    i = square[0]
    j = square[1]
    attackSquaresEight = [[i+1,j],[i+1,j+1],[i,j+1],[i-1,j+1],[i-1,j],[i-1,j-1],[i,j-1],[i+1,j-1]]
    attackSquares = []
    for attackSquare in attackSquaresEight:
        if attackSquare[0] in [0,1,2,3,4,5,6,7] and attackSquare[1] in [0,1,2,3,4,5,6,7]:
            if board[attackSquare[0]][attackSquare[1]][0] in [" ", colorOpp]:
                attackSquares.append(attackSquare)
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
    for attackSquare in attackSquares:
        if attackSquare == squareKing:
            return True
    return False

def isLegalMove(board, color, checkFlag, move):
    i0 = move[0][0]
    j0 = move[0][1]
    i1 = move[1][0]
    j1 = move[1][1]
    
    #Castling transit square
    legalCastleFlag = True
    if (board[i0][j0][1] == "K") and (abs(j1 - j0) == 2):
        jTransit = int((j0 + j1)/2)
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
            boardNew[i1][jTransit] = boardNew[i0][j0]
            boardNew[i0][j0] = "  "
            legalCastleFlag = not inCheck(boardNew, color)
    
    #Final square
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

def convertSquareCoord(square):
    i = square[0]
    j = square[1]
    row = str(i+1)
    if j == 0:
        col = "a"
    elif j == 1:
        col = "b"
    elif j == 2:
        col = "c"
    elif j == 3:
        col = "d"
    elif j == 4:
        col = "e"
    elif j == 5:
        col = "f"
    elif j == 6:
        col = "g"
    elif j == 7:
        col = "h"
    return col + row

def convertMoveCoord(move):
    return convertSquareCoord(move[0]) + "-" + convertSquareCoord(move[1])

def printStatus(colorMove, checkFlag, checkmateFlag, stalemateFlag):
    if colorMove == "w":
        print("Turn to move: WHITE")
    elif colorMove == "b":
        print("Turn to move: BLACK")
    
    if checkFlag:
        print("In check?     YES")
    else:
        print("In check?     NO")
    
    if checkmateFlag:
        print("Checkmate?    YES")
    else:
        print("Checkmate?    NO")
    
    if stalemateFlag:
        print("Stalemate?    YES")
    else:
        print("Stalemate?    NO")
    
    print("")
    return

def printMovesCoord(text, movesCoord):
    print(text, end="")
    print(", ".join(movesCoord))
    return

def main():
    #Position setup
    row8 = ["bR","bN","bB","bQ","bK","bB","bN","bR"]
    row7 = ["bp","bp","bp","bp","bp","bp","bp","bp"]
    row6 = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row5 = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row4 = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row3 = ["  ","  ","  ","  ","  ","  ","  ","  "]
    row2 = ["wp","wp","wp","wp","wp","wp","wp","wp"]
    row1 = ["wR","wN","wB","wQ","wK","wB","wN","wR"]
    board = [row1,row2,row3,row4,row5,row6,row7,row8]
    colorMove = "w"
    checkFlag = inCheck(board, colorMove)
    canCastleKingside = True
    canCastleQueenside = True
    enPassant = []
    
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
    
    movesBishop = []
    for square in squaresBishop:
        movesBishop.extend([[square, moveSquare] for moveSquare in findMoveSquaresBishop(board, colorMove, square)])
    movesLegalBishop = [move for move in movesBishop if isLegalMove(board, colorMove, checkFlag, move)]
    movesCoordBishop = [convertMoveCoord(move) for move in movesLegalBishop]
    movesCoordBishop.sort()
    
    movesKnight = []
    for square in squaresKnight:
        movesKnight.extend([[square, moveSquare] for moveSquare in findMoveSquaresKnight(board, colorMove, square)])
    movesLegalKnight = [move for move in movesKnight if isLegalMove(board, colorMove, checkFlag, move)]
    movesCoordKnight = [convertMoveCoord(move) for move in movesLegalKnight]
    movesCoordKnight.sort()
    
    movesRook = []
    for square in squaresRook:
        movesRook.extend([[square, moveSquare] for moveSquare in findMoveSquaresRook(board, colorMove, square)])
    movesLegalRook = [move for move in movesRook if isLegalMove(board, colorMove, checkFlag, move)]
    movesCoordRook = [convertMoveCoord(move) for move in movesLegalRook]
    movesCoordRook.sort()
    
    movesQueen = []
    for square in squaresQueen:
        movesQueen.extend([[square, moveSquare] for moveSquare in findMoveSquaresQueen(board, colorMove, square)])
    movesLegalQueen = [move for move in movesQueen if isLegalMove(board, colorMove, checkFlag, move)]
    movesCoordQueen = [convertMoveCoord(move) for move in movesLegalQueen]
    movesCoordQueen.sort()
    
    movesKing = []
    for square in squaresKing:
        movesKing.extend([[square, moveSquare] for moveSquare in findMoveSquaresKing(board, colorMove, canCastleKingside, canCastleQueenside, square)])
    movesLegalKing = [move for move in movesKing if isLegalMove(board, colorMove, checkFlag, move)]
    movesCoordKing = [convertMoveCoord(move) for move in movesLegalKing]
    movesCoordKing.sort()
    
    movesCoord = movesCoordPawn + movesCoordBishop + movesCoordKnight + movesCoordRook + movesCoordQueen + movesCoordKing
    
    #Print status
    checkmateFlag = checkFlag and len(movesCoord) == 0
    stalemateFlag = not checkFlag and len(movesCoord) == 0
    printStatus(colorMove, checkFlag, checkmateFlag, stalemateFlag)
    
    #Print moves
    print("Possible Moves:")
    printMovesCoord("Pawn   | ", movesCoordPawn)
    printMovesCoord("Bishop | ", movesCoordBishop)
    printMovesCoord("Knight | ", movesCoordKnight)
    printMovesCoord("Rook   | ", movesCoordRook)
    printMovesCoord("Queen  | ", movesCoordQueen)
    printMovesCoord("King   | ", movesCoordKing)
    print("")
    return

if __name__ == "__main__":
    main()
