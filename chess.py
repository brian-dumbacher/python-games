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

def findPositsEndPawn(board, colorMove, enPassant, posit):
    if colorMove == "w":
        d = 1
    elif colorMove == "b":
        d = -1
    i = posit[0]
    j = posit[1]
    candsQual = []
    #One square ahead
    if board[i+d][j] == "":
        candsQual.append([i+d,j])
    #Two squares ahead
    if i == 1:
        if board[i+2*d][j] == "":
            candsQual.append([i+2*d,j])
    #Capture
    if j >= 1:
        if board[i+d][j-1] != "":
            if board[i+d][j-1][0] != colorMove:
                candsQual.append([i+d,j-1])
    if j <= 6:
        if board[i+d][j+1] != "":
            if board[i+d][j+1][0] != colorMove:
                candsQual.append([i+d,j+1])
    #en passant
    if enPassant != []:
        iEP = enPassant[0]
        jEP = enPassant[1]
        if i == iEP and abs(j - jEP) == 1:
            candsQual.append([iEP+d,jEP])
    return candsQual

def findPositsEndBishop(board, colorMove, posit):
    i = posit[0]
    j = posit[1]
    candsQual = []
    #Up-Right
    blocked = False
    numSquares = min([7-i,7-j])
    for d in range(1, numSquares + 1):
        if not blocked:
            cand = [i+d,j+d]
            if board[i+d][j+d] == "":
                candsQual.append(cand)
            else:
                blocked = True
                if board[i+d][j+d][0] != colorMove:
                    candsQual.append(cand)
    #Down-Right
    blocked = False
    numSquares = min([i,7-j])
    for d in range(1, numSquares + 1):
        if not blocked:
            cand = [i-d,j+d]
            if board[i-d][j+d] == "":
                candsQual.append(cand)
            else:
                blocked = True
                if board[i-d][j+d][0] != colorMove:
                    candsQual.append(cand)
    #Down-Left
    blocked = False
    numSquares = min([i,j])
    for d in range(1, numSquares + 1):
        if not blocked:
            cand = [i-d,j-d]
            if board[i-d][j-d] == "":
                candsQual.append(cand)
            else:
                blocked = True
                if board[i-d][j-d][0] != colorMove:
                    candsQual.append(cand)
    #Up-Left
    blocked = False
    numSquares = min([7-i,j])
    for d in range(1, numSquares + 1):
        if not blocked:
            cand = [i+d,j-d]
            if board[i+d][j-d] == "":
                candsQual.append(cand)
            else:
                blocked = True
                if board[i+d][j-d][0] != colorMove:
                    candsQual.append(cand)
    return candsQual

def findPositsEndKnight(board, colorMove, posit):
    i = posit[0]
    j = posit[1]
    cands = [[i+2,j+1],[i+1,j+2],[i-1,j+2],[i-2,j+1],[i-2,j-1],[i-1,j-2],[i+1,j-2],[i+2,j-1]]
    candsQual = []
    for cand in cands:
        if cand[0] in [0,1,2,3,4,5,6,7] and cand[1] in [0,1,2,3,4,5,6,7]:
            if board[cand[0]][cand[1]] == "":
                candsQual.append(cand)
            elif board[cand[0]][cand[1]][0] != colorMove:
                candsQual.append(cand)
    return candsQual

def findPositsEndRook(board, colorMove, posit):
    i = posit[0]
    j = posit[1]
    candsQual = []
    #Up
    blocked = False
    for z in [ii for ii in [1,2,3,4,5,6,7] if ii > i]:
        if not blocked:
            cand = [z,j]
            if board[z][j] == "":
                candsQual.append(cand)
            else:
                blocked = True
                if board[z][j][0] != colorMove:
                    candsQual.append(cand)
    #Down
    blocked = False
    for z in [ii for ii in [6,5,4,3,2,1,0] if ii < i]:
        if not blocked:
            cand = [z,j]
            if board[z][j] == "":
                candsQual.append(cand)
            else:
                blocked = True
                if board[z][j][0] != colorMove:
                    candsQual.append(cand)
    #Right
    blocked = False
    for z in [jj for jj in [1,2,3,4,5,6,7] if jj > j]:
        if not blocked:
            cand = [i,z]
            if board[i][z] == "":
                candsQual.append(cand)
            else:
                blocked = True
                if board[i][z][0] != colorMove:
                    candsQual.append(cand)
    #Left
    blocked = False
    for z in [jj for jj in [6,5,4,3,2,1,0] if jj < j]:
        if not blocked:
            cand = [i,z]
            if board[i][z] == "":
                candsQual.append(cand)
            else:
                blocked = True
                if board[i][z][0] != colorMove:
                    candsQual.append(cand)
    return candsQual

def findPositsEndQueen(board, colorMove, posit):
    candsQual = findPositsEndBishop(board, colorMove, posit)
    candsQual.extend(findPositsEndRook(board, colorMove, posit))
    return candsQual

def findPositsEndKing(board, colorMove, canCastleKingside, canCastleQueenside, posit):
    i = posit[0]
    j = posit[1]
    cands = [[i+1,j],[i+1,j+1],[i,j+1],[i-1,j+1],[i-1,j],[i-1,j-1],[i,j-1],[i+1,j-1]]
    candsQual = []
    for cand in cands:
        if cand[0] in [0,1,2,3,4,5,6,7] and cand[1] in [0,1,2,3,4,5,6,7]:
            if board[cand[0]][cand[1]] == "":
                candsQual.append(cand)
            elif board[cand[0]][cand[1]][0] != colorMove:
                candsQual.append(cand)
    #Castling
    if canCastleKingside:
        if board[i][j+1] == "" and board[i][j+2] == "" and board[i][j+3] == (colorMove + "R"):
            candsQual.append([i, j+2])
    if canCastleQueenside:
        if board[i][j-1] == "" and board[i][j-2] == "" and board[i][j-3] == "" and board[i][j-4] == (colorMove + "R"):
            candsQual.append([i, j-2])
    return candsQual

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
        movesPawn.extend([[posit, positEnd] for positEnd in findPositsEndPawn(board, colorMove, enPassant, posit)])
    movesCoordPawn = [convertMoveCoord(move) for move in movesPawn]
    movesCoordPawn.sort()
    
    movesBishop = []
    for posit in positsBishop:
        movesBishop.extend([[posit, positEnd] for positEnd in findPositsEndBishop(board, colorMove, posit)])
    movesCoordBishop = [convertMoveCoord(move) for move in movesBishop]
    movesCoordBishop.sort()
    
    movesKnight = []
    for posit in positsKnight:
        movesKnight.extend([[posit, positEnd] for positEnd in findPositsEndKnight(board, colorMove, posit)])
    movesCoordKnight = [convertMoveCoord(move) for move in movesKnight]
    movesCoordKnight.sort()
    
    movesRook = []
    for posit in positsRook:
        movesRook.extend([[posit, positEnd] for positEnd in findPositsEndRook(board, colorMove, posit)])
    movesCoordRook = [convertMoveCoord(move) for move in movesRook]
    movesCoordRook.sort()
    
    movesQueen = []
    for posit in positsQueen:
        movesQueen.extend([[posit, positEnd] for positEnd in findPositsEndQueen(board, colorMove, posit)])
    movesCoordQueen = [convertMoveCoord(move) for move in movesQueen]
    movesCoordQueen.sort()
    
    movesKing = []
    for posit in positsKing:
        movesKing.extend([[posit, positEnd] for positEnd in findPositsEndKing(board, colorMove, canCastleKingside, canCastleQueenside, posit)])
    movesCoordKing = [convertMoveCoord(move) for move in movesKing]
    movesCoordKing.sort()
    
    #Print status
    print("Status")
    print("")
    
    #Print moves
    print("Possible Moves")
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
