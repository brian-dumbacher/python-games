#Name:     chess.py
#Purpose:  Determine the possible moves a player can make in a given legal position

def printBoard(board):
    print("")
    for i in [7,6,5,4,3,2,1,0]:
        print(" " + str(i+1) + " | ", end="")
        for j in [0,1,2,3,4,5,6,7]:
            square = "."
            if len(board[i][j]) == 2:
                if board[i][j][0] == "w":
                    square = board[i][j][1]
                if board[i][j][0] == "b":
                    square = "\033[94m" + board[i][j][1] + "\033[0m"
            print(square, end="")
        print("")
    print("     --------")
    print("     abcdefgh")
    print("")
    return

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

"""
def convertMove(move):
    i = int(move[1]) - 1
    j = 0
    if move[0] == "a":
        j = 0
    elif move[0] == "b":
        j = 1
    elif move[0] == "c":
        j = 2
    elif move[0] == "d":
        j = 3
    elif move[0] == "e":
        j = 4
    elif move[0] == "f":
        j = 5
    elif move[0] == "g":
        j = 6
    elif move[0] == "h":
        j = 7
    return [i,j]

def validMoveStart(board, moveStart, color):
    validFlag = False
    if len(moveStart) == 2:
        if moveStart[0] in ["a","b","c","d","e","f","g","h"] and moveStart[1] in ["1","2","3","4","5","6","7","8"]:
            moveStartConvert = convertMove(moveStart)
            i = moveStartConvert[0]
            j = moveStartConvert[1]
            if board[i][j] != "":
                validFlag = (board[i][j][0] == color)
    return validFlag

def validMoveEnd(board, moveStart, moveEnd, color):
    validFlag = False
    if len(moveEnd) == 2:
        if moveEnd[0] in ["a","b","c","d","e","f","g","h"] and moveEnd[1] in ["1","2","3","4","5","6","7","8"]:
            moveEndConvert = convertMove(moveEnd)
            i = moveEndConvert[0]
            j = moveEndConvert[1]
            validFlag = (board[i][j] == "")
    return validFlag

def updateBoard(board, moveStart, moveEnd):
    moveStartConvert = convertMove(moveStart)
    iStart = moveStartConvert[0]
    jStart = moveStartConvert[1]
    moveEndConvert = convertMove(moveEnd)
    iEnd = moveEndConvert[0]
    jEnd = moveEndConvert[1]
    board[iEnd][jEnd] = board[iStart][jStart]
    board[iStart][jStart] = ""
    return board
"""

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
    enPassant = ""
    
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
    movesPawn   = []
    movesBishop = []
    for posit in positsBishop:
        movesBishop.extend(findBishopMoves(board, colorMove, posit))
    movesKnight = []
    for posit in positsKnight:
        movesKnight.extend(findKnightMoves(board, colorMove, posit))
    movesRook   = []
    for posit in positsRook:
        movesRook.extend(findRookMoves(board, colorMove, posit))
    movesQueen  = []
    for posit in positsQueen:
        movesQueen.extend(findQueenMoves(board, colorMove, posit))
    movesKing   = []
    for posit in positsKing:
        movesKing.extend(findKingMoves(board, colorMove, canCastleKingside, canCastleQueenside, posit))
    
    print(movesBishop)
    print(movesKnight)
    print(movesRook)
    print(movesQueen)
    print(movesKing)

    return

if __name__ == "__main__":
    main()
