#Name:     chess.py
#Purpose:  Given a legal chess position, determine all possible moves

def printBoard(board):
    ansiGREY = "\x1b[90m"
    ansiBLUE = "\x1b[94m"
    ansiTEAL = "\x1b[96m"
    ansiEND  = "\x1b[0m"
    print("")
    for i in [7,6,5,4,3,2,1,0]:
        print(ansiTEAL + " " + str(i+1) + " |" + ansiEND, end="")
        for j in [0,1,2,3,4,5,6,7]:
            if board[i][j] == "":
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

def findMoveSquaresPawn(board, color, enPassant, posit):
    if color == "w":
        d = 1
    elif color == "b":
        d = -1
    i = posit[0]
    j = posit[1]
    moveSquares = []
    #One square ahead
    if board[i+d][j] == "":
        moveSquares.append([i+d,j])
    #Two squares ahead
    if i == 1:
        if board[i+2*d][j] == "":
            moveSquares.append([i+2*d,j])
    #Capture
    if j >= 1:
        if board[i+d][j-1] != "":
            if board[i+d][j-1][0] != color:
                moveSquares.append([i+d,j-1])
    if j <= 6:
        if board[i+d][j+1] != "":
            if board[i+d][j+1][0] != color:
                moveSquares.append([i+d,j+1])
    #en passant
    if enPassant != []:
        iEP = enPassant[0]
        jEP = enPassant[1]
        if i == iEP and abs(j - jEP) == 1:
            moveSquares.append([iEP+d,jEP])
    return moveSquares

def findMoveSquaresBishop(board, color, posit):
    i = posit[0]
    j = posit[1]
    moveSquares = []
    #Up-Right
    blocked = False
    numSquares = min([7-i,7-j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i+d][j+d] == "":
                moveSquares.append([i+d,j+d])
            else:
                blocked = True
                if board[i+d][j+d][0] != color:
                    moveSquares.append([i+d,j+d])
    #Down-Right
    blocked = False
    numSquares = min([i,7-j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i-d][j+d] == "":
                moveSquares.append([i-d,j+d])
            else:
                blocked = True
                if board[i-d][j+d][0] != color:
                    moveSquares.append([i-d,j+d])
    #Down-Left
    blocked = False
    numSquares = min([i,j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i-d][j-d] == "":
                moveSquares.append([i-d,j-d])
            else:
                blocked = True
                if board[i-d][j-d][0] != color:
                    moveSquares.append([i-d,j-d])
    #Up-Left
    blocked = False
    numSquares = min([7-i,j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i+d][j-d] == "":
                moveSquares.append([i+d,j-d])
            else:
                blocked = True
                if board[i+d][j-d][0] != color:
                    moveSquares.append([i+d,j-d])
    return moveSquares

def findMoveSquaresKnight(board, color, posit):
    i = posit[0]
    j = posit[1]
    moveSquaresEight = [[i+2,j+1],[i+1,j+2],[i-1,j+2],[i-2,j+1],[i-2,j-1],[i-1,j-2],[i+1,j-2],[i+2,j-1]]
    moveSquares = []
    for moveSquare in moveSquareEight:
        if moveSquare[0] in [0,1,2,3,4,5,6,7] and moveSquare[1] in [0,1,2,3,4,5,6,7]:
            if board[moveSquare[0]][moveSquare[1]] == "":
                moveSquares.append(moveSquare)
            elif board[moveSquare[0]][moveSquare[1]][0] != color:
                moveSquares.append(moveSquare)
    return moveSquares

def findMoveSquaresRook(board, color, posit):
    i = posit[0]
    j = posit[1]
    moveSquares = []
    #Up
    blocked = False
    for z in [ii for ii in [1,2,3,4,5,6,7] if ii > i]:
        if not blocked:
            if board[z][j] == "":
                moveSquares.append([z,j])
            else:
                blocked = True
                if board[z][j][0] != color:
                    moveSquares.append([z,j])
    #Down
    blocked = False
    for z in [ii for ii in [6,5,4,3,2,1,0] if ii < i]:
        if not blocked:
            if board[z][j] == "":
                moveSquares.append([z,j])
            else:
                blocked = True
                if board[z][j][0] != color:
                    moveSquares.append([z,j])
    #Right
    blocked = False
    for z in [jj for jj in [1,2,3,4,5,6,7] if jj > j]:
        if not blocked:
            if board[i][z] == "":
                moveSquares.append([i,z])
            else:
                blocked = True
                if board[i][z][0] != color:
                    moveSquares.append([i,z])
    #Left
    blocked = False
    for z in [jj for jj in [6,5,4,3,2,1,0] if jj < j]:
        if not blocked:
            if board[i][z] == "":
                moveSquares.append([i,z])
            else:
                blocked = True
                if board[i][z][0] != color:
                    moveSquares.append([i,z])
    return moveSquares

def findMoveSquaresQueen(board, color, posit):
    moveSquares = findMoveSquaresBishop(board, color, posit)
    moveSquares.extend(findMoveSquaresRook(board, color, posit))
    return moveSquares

def findMoveSquaresKing(board, color, canCastleKingside, canCastleQueenside, posit):
    i = posit[0]
    j = posit[1]
    moveSquaresEight = [[i+1,j],[i+1,j+1],[i,j+1],[i-1,j+1],[i-1,j],[i-1,j-1],[i,j-1],[i+1,j-1]]
    moveSquares = []
    for moveSquare in moveSquaresEight:
        if moveSquare[0] in [0,1,2,3,4,5,6,7] and moveSquare[1] in [0,1,2,3,4,5,6,7]:
            if board[moveSquare[0]][moveSquare[1]] == "":
                moveSquares.append(moveSquare)
            elif board[moveSquare[0]][moveSquare[1]][0] != color:
                moveSquares.append(moveSquare)
    #Castling
    if canCastleKingside:
        if board[i][j+1] == "" and board[i][j+2] == "" and board[i][j+3] == (color + "R"):
            moveSquares.append([i, j+2])
    if canCastleQueenside:
        if board[i][j-1] == "" and board[i][j-2] == "" and board[i][j-3] == "" and board[i][j-4] == (color + "R"):
            moveSquares.append([i, j-2])
    return moveSquares

def findAttackSquaresPawn(board, color, posit):
    if color == "w":
        d = 1
    elif color == "b":
        d = -1
    i = posit[0]
    j = posit[1]
    attackSquares = []
    #Capture
    if j >= 1:
        if board[i+d][j-1] != "":
            if board[i+d][j-1][0] != color:
                attackSquares.append([i+d,j-1])
    if j <= 6:
        if board[i+d][j+1] != "":
            if board[i+d][j+1][0] != color:
                attackSquares.append([i+d,j+1])
    return attackSquares

def findAttackSquaresBishop(board, color, posit):
    return findMoveSquaresBishop(board, color, posit)

def findAttackSquaresKnight(board, color, posit):
    return findMoveSquaresKnight(board, color, posit)

def findAttackSquaresRook(board, color, posit):
    return findMoveSquaresRook(board, color, posit)

def findAttackSquaresQueen(board, color, posit):
    return findMoveSquaresQueen(board, color, posit)

def findAttackSquaresKing(board, color, posit):
    i = posit[0]
    j = posit[1]
    attackSquaresEight = [[i+1,j],[i+1,j+1],[i,j+1],[i-1,j+1],[i-1,j],[i-1,j-1],[i,j-1],[i+1,j-1]]
    attackSquares = []
    for attackSquare in attackSquaresEight:
        if attackSquare[0] in [0,1,2,3,4,5,6,7] and attackSquare[1] in [0,1,2,3,4,5,6,7]:
            if board[attackSquare[0]][attackSquare[1]] == "":
                attackSquares.append(attackSquare)
            elif board[attackSquare[0]][attackSquare[1]][0] != color:
                attackSquares.append(attackSquare)
    return attackSquares

def inCheck(board, color):
    #Determine color of opponent
    if color == "w":
        colorOpp = "b"
    elif color == "b":
        colorOpp = "w"
    
    #Piece positions
    positsPawnOpp   = []
    positsBishopOpp = []
    positsKnightOpp = []
    positsRookOpp   = []
    positsQueenOpp  = []
    positsKingOpp   = []
    for i in [0,1,2,3,4,5,6,7]:
        for j in [0,1,2,3,4,5,6,7]:
            if board[i][j] != "":
                if board[i][j][0] == colorOpp:
                    if board[i][j][1] == "p":
                        positsPawnOpp.append([i,j])
                    elif board[i][j][1] == "B":
                        positsBishopOpp.append([i,j])
                    elif board[i][j][1] == "N":
                        positsKnightOpp.append([i,j])
                    elif board[i][j][1] == "R":
                        positsRookOpp.append([i,j])
                    elif board[i][j][1] == "Q":
                        positsQueenOpp.append([i,j])
                    elif board[i][j][1] == "K":
                        positsKingOpp.append([i,j])
                elif board[i][j][0] == color:
                    if board[i][j][1] == "K":
                        positKing = [i,j]
    
    #Possible moves
    attackSquares = []
    for posit in positsPawnOpp:
        attackSquares.extend(findAttackSquaresPawn(board, colorOpp, posit))
    for posit in positsBishopOpp:
        attackSquares.extend(findAttackSquaresBishop(board, colorOpp, posit))
    for posit in positsKnightOpp:
        attackSquares.extend(findAttackSquaresKnight(board, colorOpp, posit))
    for posit in positsRookOpp:
        attackSquares.extend(findAttackSquaresRook(board, colorOpp, posit))
    for posit in positsQueenOpp:
        attackSquares.extend(findAttackSquaresQueen(board, colorOpp, posit))
    for posit in positsKingOpp:
        attackSquares.extend(findAttackSquaresKing(board, colorOpp, posit))
    
    #Determine whether king is in check
    checkFlag = False
    for attackSquare in attackSquares:
        if attackSquare == positKing:
            checkFlag = True
    return checkFlag

def convertPositCoord(posit):
    i = posit[0]
    j = posit[1]
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
    return convertPositCoord(move[0]) + "-" + convertPositCoord(move[1])

def printMovesCoord(text, movesCoord):
    print(text, end="")
    print(", ".join(movesCoord))
    return

def isLegalMove(board, color, move):
    i0 = move[0][0]
    j0 = move[0][1]
    i1 = move[1][0]
    j1 = move[1][1]
    boardNew = board
    boardNew[i1,j1] = boardNew[i0,j0]
    boardNew[i0,j0] = ""
    return not inCheck(boardNew, color)

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
    row8 = ["bR","bN","bB","bQ","bK","bB","bN","bR"]
    row7 = ["bp","bp","bp","bp","bp","bp","bp","bp"]
    row6 = ["","","","","","","",""]
    row5 = ["","","","","","","",""]
    row4 = ["","","","","","","",""]
    row3 = ["","","","","","","",""]
    row2 = ["wp","wp","wp","wp","wp","wp","wp","wp"]
    row1 = ["wR","wN","wB","wQ","wK","wB","wN","wR"]
    board = [row1, row2, row3, row4, row5, row6, row7, row8]
    colorMove = "w"
    canCastleKingside = True
    canCastleQueenside = True
    enPassant = []
    
    #Print board
    printBoard(board)
    
    #Piece positions
    positsPawn   = []
    positsBishop = []
    positsKnight = []
    positsRook   = []
    positsQueen  = []
    positsKing   = []
    for i in [0,1,2,3,4,5,6,7]:
        for j in [0,1,2,3,4,5,6,7]:
            if board[i][j] != "":
                if board[i][j][0] == colorMove:
                    if board[i][j][1] == "p":
                        positsPawn.append([i,j])
                    elif board[i][j][1] == "B":
                        positsBishop.append([i,j])
                    elif board[i][j][1] == "N":
                        positsKnight.append([i,j])
                    elif board[i][j][1] == "R":
                        positsRook.append([i,j])
                    elif board[i][j][1] == "Q":
                        positsQueen.append([i,j])
                    elif board[i][j][1] == "K":
                        positsKing.append([i,j])
    
    #Possible moves
    movesPawn = []
    for posit in positsPawn:
        movesPawn.extend([[posit, moveSquare] for moveSquare in findMoveSquaresPawn(board, colorMove, enPassant, posit)])
    movesLegalPawn = [move for move in movesPawn if isLegalMove(board, colorMove, move)]
    movesCoordPawn = [convertMoveCoord(move) for move in movesLegalPawn]
    movesCoordPawn.sort()
    
    movesBishop = []
    for posit in positsBishop:
        movesBishop.extend([[posit, moveSquare] for moveSquare in findMoveSquaresBishop(board, colorMove, posit)])
    movesLegalBishop = [move for move in movesBishop if isLegalMove(board, colorMove, move)]
    movesCoordBishop = [convertMoveCoord(move) for move in movesLegalBishop]
    movesCoordBishop.sort()
    
    movesKnight = []
    for posit in positsKnight:
        movesKnight.extend([[posit, moveSquare] for moveSquare in findMoveSquaresKnight(board, colorMove, posit)])
    movesLegalKnight = [move for move in movesKnight if isLegalMove(board, colorMove, move)]
    movesCoordKnight = [convertMoveCoord(move) for move in movesLegalKnight]
    movesCoordKnight.sort()
    
    movesRook = []
    for posit in positsRook:
        movesRook.extend([[posit, moveSquare] for moveSquare in findMoveSquaresRook(board, colorMove, posit)])
    movesLegalRook = [move for move in movesRook if isLegalMove(board, colorMove, move)]
    movesCoordRook = [convertMoveCoord(move) for move in movesLegalRook]
    movesCoordRook.sort()
    
    movesQueen = []
    for posit in positsQueen:
        movesQueen.extend([[posit, moveSquare] for moveSquare in findMoveSquaresQueen(board, colorMove, posit)])
    movesLegalQueen = [move for move in movesQueen if isLegalMove(board, colorMove, move)]
    movesCoordQueen = [convertMoveCoord(move) for move in movesLegalQueen]
    movesCoordQueen.sort()
    
    movesKing = []
    for posit in positsKing:
        movesKing.extend([[posit, moveSquare] for moveSquare in findMoveSquaresKing(board, colorMove, canCastleKingside, canCastleQueenside, posit)])
    movesLegalKing = [move for move in movesKing if isLegalMove(board, colorMove, move)]
    movesCoordKing = [convertMoveCoord(move) for move in movesLegalKing]
    movesCoordKing.sort()
    
    movesCoord = movesCoordPawn + movesCoordBishop + movesCoordKnight + movesCoordRook + movesCoordQueen + movesCoordKing
    
    #Print status
    checkFlag = inCheck(board, colorMove)
    checkmateFlag = (len(movesCoord) == 0)
    printStatus(colorMove, checkFlag, checkmateFlag)
    
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
