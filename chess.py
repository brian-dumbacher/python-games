#Name:     chess.py
#Purpose:  Given a legal chess position, determine all possible moves

def printBoard(board):
    print("")
    for i in [7,6,5,4,3,2,1,0]:
        print(" " + str(i+1) + " |", end="")
        for j in [0,1,2,3,4,5,6,7]:
            square = "."
            if len(board[i][j]) == 2:
                if board[i][j][0] == "w":
                    square = board[i][j][1]
                if board[i][j][0] == "b":
                    square = "\033[94m" + board[i][j][1] + "\033[0m"
            print(" " + square, end="")
        print("")
    print("     ---------------")
    print("     a b c d e f g h")
    print("")
    return

def makeNotation(move, piece):
    i = move[0]
    j = move[1]
    row = str(i+1)
    col = ""
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
    pid = piece
    if piece == "p":
        pid = ""
    notation = pid + col + row
    return notation

def findPawnMoves(board, colorMove, enPassant, posit):
    d = 1
    if colorMove == "b":
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
        if board[i+d][j-1][0] == "b":
            candsQual.append([i+d,j-1])
    if j <= 6:
        if board[i+d][j+1][0] == "b":
            candsQual.append([i+d,j+1])
    #en passant
    if enPassant != []:
        iEP = enPassant[0]
        jEP = enPassant[1]
        if i == iEP:
            if abs(j - jEP) == 1:
                candsQual.append([iEP+d,jEP])
    return candsQual

def findBishopMoves(board, colorMove, posit):
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

def findKnightMoves(board, colorMove, posit):
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

def findRookMoves(board, colorMove, posit):
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

def findQueenMoves(board, colorMove, posit):
    candsQual = findBishopMoves(board, colorMove, posit)
    candsQual.extend(findRookMoves(board, colorMove, posit))
    return candsQual

def findKingMoves(board, colorMove, canCastleKingside, canCastleQueenside, posit):
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
        movesPawn.extend(findPawnMoves(board, colorMove, enPassant, posit))
    notationsPawn = [makeNotation(move, "") for move in movesPawn]
    notationsPawn.sort()
    
    movesBishop = []
    for posit in positsBishop:
        movesBishop.extend(findBishopMoves(board, colorMove, posit))
    notationsBishop = [makeNotation(move, "B") for move in movesBishop]
    notationsBishop.sort()
    
    movesKnight = []
    for posit in positsKnight:
        movesKnight.extend(findKnightMoves(board, colorMove, posit))
    notationsKnight = [makeNotation(move, "N") for move in movesKnight]
    notationsKnight.sort()
    
    movesRook = []
    for posit in positsRook:
        movesRook.extend(findRookMoves(board, colorMove, posit))
    notationsRook = [makeNotation(move, "R") for move in movesRook]
    notationsRook.sort()
    
    movesQueen = []
    for posit in positsQueen:
        movesQueen.extend(findQueenMoves(board, colorMove, posit))
    notationsQueen = [makeNotation(move, "Q") for move in movesQueen]
    notationsQueen.sort()
    
    movesKing = []
    for posit in positsKing:
        movesKing.extend(findKingMoves(board, colorMove, canCastleKingside, canCastleQueenside, posit))
    notationsKing = [makeNotation(move, "K") for move in movesKing]
    notationsKing.sort()
    
    #Print moves
    print(notationsBishop)
    print(notationsKnight)
    print(notationsRook)
    print(notationsQueen)
    print(notationsKing)
    return

if __name__ == "__main__":
    main()
