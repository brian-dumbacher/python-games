# Name:     chess.py
# Purpose:  Given a legal chess position, determine all possible moves
# Author:   Brian Dumbacher
# Date:     June 20, 2025

import copy

# ANSI escape codes
ANSI_BLACK     = "\x1b[30m"
ANSI_RED_BOLD  = "\x1b[1;31m"
ANSI_BLUE_BOLD = "\x1b[1;34m"
ANSI_GREY      = "\x1b[90m"
ANSI_END       = "\x1b[0m"

# Name:        printBoard
# Purpose:     Print board in current state
# Parameters:  board (2D list)
# Returns:

def printBoard(board):
    print("")
    for i in [7, 6, 5, 4, 3, 2, 1, 0]:
        if i == 7:
            print("{}    -------------------------------{}".format(ANSI_GREY, ANSI_END))
        else:
            print("{}   |---+---+---+---+---+---+---+---|{}".format(ANSI_GREY, ANSI_END))
        print(" {}{}{} {}|{}".format(ANSI_BLACK, i+1, ANSI_END, ANSI_GREY, ANSI_END), end="")
        for j in [0, 1, 2, 3, 4, 5, 6, 7]:
            if board[i][j] == "  ":
                square = " ".format(ANSI_GREY, ANSI_END)
            elif board[i][j][0] == "w":
                square = "{}{}{}".format(ANSI_RED_BOLD, board[i][j][1], ANSI_END)
            elif board[i][j][0] == "b":
                square = "{}{}{}".format(ANSI_BLUE_BOLD, board[i][j][1], ANSI_END)
            print(" {} {}|{}".format(square, ANSI_GREY, ANSI_END), end="")
        print("")
    print("{}    -------------------------------{}".format(ANSI_GREY, ANSI_END))
    print("{}     a   b   c   d   e   f   g   h {}".format(ANSI_BLACK, ANSI_END))
    print("")
    return

# Name:        findMovesCandPawn
# Purpose:     Determine candidate pawn moves
# Parameters:  board (2D list)
#              player ("w" or "b")
#              enPassant (iEP, jEP)
#              startSquare (i, j)
# Returns:     List of candidate pawn moves

def findMovesCandPawn(board, player, enPassant, startSquare):
    # Opponent
    if player == "w":
        playerOpp = "b"
        d = 1
        promotionRow = 7
    elif player == "b":
        playerOpp = "w"
        d = -1
        promotionRow = 0

    # Start square
    i = startSquare[0]
    j = startSquare[1]

    # End squares and move types
    endSquares = []
    moveTypes = []

    # One square ahead
    if board[i+d][j] == "  ":
        endSquares.append((i+d, j))
        moveTypes.append("normal")

    # Two squares ahead
    if (player == "w" and i == 1) or (player == "b" and i == 6):
        if board[i+d][j] == "  " and board[i+2*d][j] == "  ":
            endSquares.append((i+2*d, j))
            moveTypes.append("normal")

    # Capture
    if j >= 1:
        if board[i+d][j-1][0] == playerOpp:
            endSquares.append((i+d, j-1))
            moveTypes.append("capture")
    if j <= 6:
        if board[i+d][j+1][0] == playerOpp:
            endSquares.append((i+d, j+1))
            moveTypes.append("capture")

    # Capture en passant
    if enPassant != ():
        iEP = enPassant[0]
        jEP = enPassant[1]
        if (i == iEP) and (abs(j - jEP) == 1):
            endSquares.append((iEP+d, jEP))
            moveTypes.append("enpassant")

    # List of candidate pawn moves
    movesCandInit = [{"piece": "pawn", "startSquare": startSquare, "endSquare": endSquares[i], "type": moveTypes[i]} for i in range(len(endSquares))]
    movesCandFinal = []
    for d in movesCandInit:
        if d["endSquare"][0] == promotionRow:
            movesCandFinal.append({"piece": d["piece"], "startSquare": d["startSquare"], "endSquare": d["endSquare"], "type": d["type"], "promotion": "=B"})
            movesCandFinal.append({"piece": d["piece"], "startSquare": d["startSquare"], "endSquare": d["endSquare"], "type": d["type"], "promotion": "=N"})
            movesCandFinal.append({"piece": d["piece"], "startSquare": d["startSquare"], "endSquare": d["endSquare"], "type": d["type"], "promotion": "=R"})
            movesCandFinal.append({"piece": d["piece"], "startSquare": d["startSquare"], "endSquare": d["endSquare"], "type": d["type"], "promotion": "=Q"})
        else:
            movesCandFinal.append({"piece": d["piece"], "startSquare": d["startSquare"], "endSquare": d["endSquare"], "type": d["type"], "promotion": ""})

    return movesCandFinal

# Name:        findMovesCandBishop
# Purpose:     Determine candidate bishop moves
# Parameters:  board (2D list)
#              player ("w" or "b")
#              startSquare (i, j)
# Returns:     List of candidate bishop moves

def findMovesCandBishop(board, player, startSquare):
    # Opponent
    if player == "w":
        playerOpp = "b"
    elif player == "b":
        playerOpp = "w"

    # Start square
    i = startSquare[0]
    j = startSquare[1]

    # End squares and move types
    endSquares = []
    moveTypes = []

    # Up-right
    blocked = False
    numSquares = min([7-i, 7-j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i+d][j+d] == "  ":
                endSquares.append((i+d, j+d))
                moveTypes.append("normal")
            else:
                blocked = True
                if board[i+d][j+d][0] == playerOpp:
                    endSquares.append((i+d, j+d))
                    moveTypes.append("capture")

    # Down-right
    blocked = False
    numSquares = min([i, 7-j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i-d][j+d] == "  ":
                endSquares.append((i-d, j+d))
                moveTypes.append("normal")
            else:
                blocked = True
                if board[i-d][j+d][0] == playerOpp:
                    endSquares.append((i-d, j+d))
                    moveTypes.append("capture")

    # Down-left
    blocked = False
    numSquares = min([i, j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i-d][j-d] == "  ":
                endSquares.append((i-d, j-d))
                moveTypes.append("normal")
            else:
                blocked = True
                if board[i-d][j-d][0] == playerOpp:
                    endSquares.append((i-d, j-d))
                    moveTypes.append("capture")

    # Up-left
    blocked = False
    numSquares = min([7-i, j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i+d][j-d] == "  ":
                endSquares.append((i+d, j-d))
                moveTypes.append("normal")
            else:
                blocked = True
                if board[i+d][j-d][0] == playerOpp:
                    endSquares.append((i+d, j-d))
                    moveTypes.append("capture")

    # List of candidate bishop moves
    movesCandFinal = [{"piece": "bishop", "startSquare": startSquare, "endSquare": endSquares[i], "type": moveTypes[i], "promotion": ""} for i in range(len(endSquares))]

    return movesCandFinal

# Name:        findMovesCandKnight
# Purpose:     Determine candidate knight moves
# Parameters:  board (2D list)
#              player ("w" or "b")
#              startSquare (i, j)
# Returns:     List of candidate knight moves

def findMovesCandKnight(board, player, startSquare):
    # Opponent
    if player == "w":
        playerOpp = "b"
    elif player == "b":
        playerOpp = "w"

    # Start square
    i = startSquare[0]
    j = startSquare[1]

    # End squares and move types
    endSquares = []
    moveTypes = []

    # Normal moves and captures
    endSquaresEight = [(i+2, j+1), (i+1, j+2), (i-1, j+2), (i-2, j+1), (i-2, j-1), (i-1, j-2), (i+1, j-2), (i+2, j-1)]
    for endSquare in endSquaresEight:
        if endSquare[0] in [0, 1, 2, 3, 4, 5, 6, 7] and endSquare[1] in [0, 1, 2, 3, 4, 5, 6, 7]:
            if board[endSquare[0]][endSquare[1]] == "  ":
                endSquares.append(endSquare)
                moveTypes.append("normal")
            elif board[endSquare[0]][endSquare[1]][0] == playerOpp:
                endSquares.append(endSquare)
                moveTypes.append("capture")

    # List of candidate knight moves
    movesCandFinal = [{"piece": "knight", "startSquare": startSquare, "endSquare": endSquares[i], "type": moveTypes[i], "promotion": ""} for i in range(len(endSquares))]

    return movesCandFinal

# Name:        findMovesCandRook
# Purpose:     Determine candidate rook moves
# Parameters:  board (2D list)
#              player ("w" or "b")
#              startSquare (i, j)
# Returns:     List of candidate rook moves

def findMovesCandRook(board, player, startSquare):
    # Opponent
    if player == "w":
        playerOpp = "b"
    elif player == "b":
        playerOpp = "w"

    # Start square
    i = startSquare[0]
    j = startSquare[1]

    # End squares and move types
    endSquares = []
    moveTypes = []

    # Up
    blocked = False
    for z in [ii for ii in [1, 2, 3, 4, 5, 6, 7] if ii > i]:
        if not blocked:
            if board[z][j] == "  ":
                endSquares.append((z, j))
                moveTypes.append("normal")
            else:
                blocked = True
                if board[z][j][0] == playerOpp:
                    endSquares.append((z, j))
                    moveTypes.append("capture")

    # Down
    blocked = False
    for z in [ii for ii in [6, 5, 4, 3, 2, 1, 0] if ii < i]:
        if not blocked:
            if board[z][j] == "  ":
                endSquares.append((z, j))
                moveTypes.append("normal")
            else:
                blocked = True
                if board[z][j][0] == playerOpp:
                    endSquares.append((z, j))
                    moveTypes.append("capture")

    # Right
    blocked = False
    for z in [jj for jj in [1, 2, 3, 4, 5, 6, 7] if jj > j]:
        if not blocked:
            if board[i][z] == "  ":
                endSquares.append((i, z))
                moveTypes.append("normal")
            else:
                blocked = True
                if board[i][z][0] == playerOpp:
                    endSquares.append((i, z))
                    moveTypes.append("capture")

    # Left
    blocked = False
    for z in [jj for jj in [6, 5, 4, 3, 2, 1, 0] if jj < j]:
        if not blocked:
            if board[i][z] == "  ":
                endSquares.append((i, z))
                moveTypes.append("normal")
            else:
                blocked = True
                if board[i][z][0] == playerOpp:
                    endSquares.append((i, z))
                    moveTypes.append("capture")

    # List of candidate rook moves
    movesCandFinal = [{"piece": "rook", "startSquare": startSquare, "endSquare": endSquares[i], "type": moveTypes[i], "promotion": ""} for i in range(len(endSquares))]

    return movesCandFinal

# Name:        findMovesCandQueen
# Purpose:     Determine candidate queen moves
# Parameters:  board (2D list)
#              player ("w" or "b")
#              startSquare (i, j)
# Returns:     List of candidate queen moves

def findMovesCandQueen(board, player, startSquare):
    # List of candidate queen moves
    movesCandFinal = findMovesCandBishop(board, player, startSquare) + findMovesCandRook(board, player, startSquare)
    for i in range(len(movesCandFinal)):
        movesCandFinal[i]["piece"] = "queen"

    return movesCandFinal

# Name:        findMovesCandKing
# Purpose:     Determine candidate king moves
# Parameters:  board (2D list)
#              player ("w" or "b")
#              canCastleKingside (boolean)
#              canCastleQueenside (boolean)
#              startSquare (i, j)
# Returns:     List of candidate king moves

def findMovesCandKing(board, player, canCastleKingside, canCastleQueenside, startSquare):
    # Opponent
    if player == "w":
        playerOpp = "b"
    elif player == "b":
        playerOpp = "w"

    # Start square
    i = startSquare[0]
    j = startSquare[1]

    # End squares and move types
    endSquares = []
    moveTypes = []

    # Normal moves and captures
    moveSquaresEight = [(i+1, j), (i+1, j+1), (i, j+1), (i-1, j+1), (i-1, j), (i-1, j-1), (i, j-1), (i+1, j-1)]
    for moveSquare in moveSquaresEight:
        if moveSquare[0] in [0, 1, 2, 3, 4, 5, 6, 7] and moveSquare[1] in [0, 1, 2, 3, 4, 5, 6, 7]:
            if board[moveSquare[0]][moveSquare[1]] == "  ":
                endSquares.append(moveSquare)
                moveTypes.append("normal")
            elif board[moveSquare[0]][moveSquare[1]][0] == playerOpp:
                endSquares.append(moveSquare)
                moveTypes.append("capture")

    # Castling
    if canCastleKingside:
        if ((player == "w") and (i == 0) and (j == 4)) or ((player == "b") and (i == 7) and (j == 4)):
            if (board[i][j+1] == "  ") and (board[i][j+2] == "  ") and (board[i][j+3] == ("{}R".format(player))):
                endSquares.append((i, j+2))
                moveTypes.append("0-0")
    if canCastleQueenside:
        if ((player == "w") and (i == 0) and (j == 4)) or ((player == "b") and (i == 7) and (j == 4)):
            if (board[i][j-1] == "  ") and (board[i][j-2] == "  ") and (board[i][j-3] == "  ") and (board[i][j-4] == ("{}R".format(player))):
                endSquares.append((i, j-2))
                moveTypes.append("0-0-0")

    # List of candidate king moves
    movesCandFinal = [{"piece": "king", "startSquare": startSquare, "endSquare": endSquares[i], "type": moveTypes[i], "promotion": ""} for i in range(len(endSquares))]

    return movesCandFinal

# Name:        findAttackSquaresPawn
# Purpose:     Determine squares that a pawn can attack
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of pawn attack squares

def findAttackSquaresPawn(board, player, square):
    # Opponent
    if player == "w":
        playerOpp = "b"
        d = 1
    elif player == "b":
        playerOpp = "w"
        d = -1

    # Pawn square
    i = square[0]
    j = square[1]

    # Attack squares
    attackSquares = []
    if j >= 1:
        if board[i+d][j-1] == "  " or board[i+d][j-1][0] == playerOpp:
            attackSquares.append((i+d, j-1))
    if j <= 6:
        if board[i+d][j+1] == "  " or board[i+d][j+1][0] == playerOpp:
            attackSquares.append((i+d, j+1))

    return attackSquares

# Name:        findAttackSquaresBishop
# Purpose:     Determine squares that a bishop can attack
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of bishop attack squares

def findAttackSquaresBishop(board, player, square):
    return [moveCand["endSquare"] for moveCand in findMovesCandBishop(board, player, square)]

# Name:        findAttackSquaresKnight
# Purpose:     Determine squares that a knight can attack
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of knight attack squares

def findAttackSquaresKnight(board, player, square):
    return [moveCand["endSquare"] for moveCand in findMovesCandKnight(board, player, square)]

# Name:        findAttackSquaresRook
# Purpose:     Determine squares that a rook can attack
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of rook attack squares

def findAttackSquaresRook(board, player, square):
    return [moveCand["endSquare"] for moveCand in findMovesCandRook(board, player, square)]

# Name:        findAttackSquaresQueen
# Purpose:     Determine squares that a queen can attack
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of queen attack squares

def findAttackSquaresQueen(board, player, square):
    return [moveCand["endSquare"] for moveCand in findMovesCandQueen(board, player, square)]

# Name:        findAttackSquaresKing
# Purpose:     Determine squares that a king can attack
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of king attack squares

def findAttackSquaresKing(board, player, square):
    # Opponent
    if player == "w":
        playerOpp = "b"
    elif player == "b":
        playerOpp = "w"

    # King square
    i = square[0]
    j = square[1]

    # Attack squares
    attackSquares = []
    attackSquaresEight = [(i+1, j), (i+1, j+1), (i, j+1), (i-1, j+1), (i-1, j), (i-1, j-1), (i, j-1), (i+1, j-1)]
    for attackSquare in attackSquaresEight:
        if attackSquare[0] in [0, 1, 2, 3, 4, 5, 6, 7] and attackSquare[1] in [0, 1, 2, 3, 4, 5, 6, 7]:
            if board[attackSquare[0]][attackSquare[1]] == "  " or board[attackSquare[0]][attackSquare[1]][0] == playerOpp:
                attackSquares.append(attackSquare)

    return attackSquares

# Name:        inCheck
# Purpose:     Determine whether player is in check
# Parameters:  board (2D list)
#              player ("w" or "b")
# Returns:     True (player in check) or False (player NOT in check)

def inCheck(board, player):
    # Opponent
    if player == "w":
        playerOpp = "b"
    elif player == "b":
        playerOpp = "w"

    # Piece positions
    squaresPawnOpp   = []
    squaresBishopOpp = []
    squaresKnightOpp = []
    squaresRookOpp   = []
    squaresQueenOpp  = []
    squaresKingOpp   = []
    for i in [0, 1, 2, 3, 4, 5, 6, 7]:
        for j in [0, 1, 2, 3, 4, 5, 6, 7]:
            if board[i][j][0] == playerOpp:
                if board[i][j][1] == "p":
                    squaresPawnOpp.append((i, j))
                elif board[i][j][1] == "B":
                    squaresBishopOpp.append((i, j))
                elif board[i][j][1] == "N":
                    squaresKnightOpp.append((i, j))
                elif board[i][j][1] == "R":
                    squaresRookOpp.append((i, j))
                elif board[i][j][1] == "Q":
                    squaresQueenOpp.append((i, j))
                elif board[i][j][1] == "K":
                    squaresKingOpp.append((i, j))
            elif board[i][j] == "{}K".format(player):
                squareKing = (i, j)

    # Determine whether player's king occupies a square under attack by the opponent
    for square in squaresPawnOpp:
        if squareKing in findAttackSquaresPawn(board, playerOpp, square):
            return True
    for square in squaresBishopOpp:
        if squareKing in findAttackSquaresBishop(board, playerOpp, square):
            return True
    for square in squaresKnightOpp:
        if squareKing in findAttackSquaresKnight(board, playerOpp, square):
            return True
    for square in squaresRookOpp:
        if squareKing in findAttackSquaresRook(board, playerOpp, square):
            return True
    for square in squaresQueenOpp:
        if squareKing in findAttackSquaresQueen(board, playerOpp, square):
            return True
    for square in squaresKingOpp:
        if squareKing in findAttackSquaresKing(board, playerOpp, square):
            return True

    return False

# Name:        isMoveLegal
# Purpose:     Determine whether candidate move is legal
# Parameters:  board (2D list)
#              player ("w" or "b")
#              checkFlag (boolean)
#              moveCand (candidate move)
# Returns:

def isMoveLegal(board, player, checkFlag, moveCand):
    # Start square and end square
    i0 = moveCand["startSquare"][0]
    j0 = moveCand["startSquare"][1]
    i1 = moveCand["endSquare"][0]
    j1 = moveCand["endSquare"][1]

    # Special moves
    isMoveCastle    = moveCand["type"] in ["0-0", "0-0-0"]
    isMoveEnPassant = moveCand["type"] == "enpassant"
    isMovePromotion = moveCand["promotion"] in ["=B", "=N", "=R", "=Q"]

    # Check castling transit square legality
    canCastleFlag = False
    legalTransitFlag = False
    if isMoveCastle and not checkFlag:
        canCastleFlag = True
        jTransit = int((j0 + j1)/2)
        boardNew = copy.deepcopy(board)
        boardNew[i1][jTransit] = "{}K".format(player)
        boardNew[i0][j0] = "  "
        legalTransitFlag = not inCheck(boardNew, player)

    # Check end square legality
    boardNew = copy.deepcopy(board)
    if isMoveCastle:
        boardNew[i1][j1] = boardNew[i0][j0]
        boardNew[i0][j0] = "  "
        if (j1 < j0):
            boardNew[i1][0]    = "  "
            boardNew[i1][j1+1] = "{}R".format(player)
        elif (j1 > j0):
            boardNew[i1][7]    = "  "
            boardNew[i1][j1-1] = "{}R".format(player)
    elif isMoveEnPassant:
        boardNew[i1][j1] = boardNew[i0][j0]
        boardNew[i0][j0] = "  "
        boardNew[i0][j1] = "  "
    elif isMovePromotion:
        boardNew[i1][j1] = "{}{}".format(player, moveCand["promotion"][1])
        boardNew[i0][j0] = "  "
    else:
        boardNew[i1][j1] = boardNew[i0][j0]
        boardNew[i0][j0] = "  "
    
    legalEndFlag = not inCheck(boardNew, player)

    return (isMoveCastle and canCastleFlag and legalTransitFlag and legalEndFlag) or (not isMoveCastle and legalEndFlag)

# Name:        convertSquareNotation
# Purpose:     Convert square to chess notation
# Parameters:  square (i, j)
# Returns:     square in chess notation (e.g., "e4")

def convertSquareNotation(square):
    #Setup
    i = square[0]
    j = square[1]

    # Row
    row = i + 1

    # Column
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

    return "{}{}".format(col, row)

# Name:        convertMoveNotation
# Purpose:     Convert legal move to chess notation
# Parameters:  board (2D list)
#              player ("w" or "b")
#              moveLegal (legal move)
# Returns:     legal move in chess notation

def convertMoveNotation(board, player, moveLegal):
    # Opponent
    if player == "w":
        playerOpp = "b"
    elif player == "b":
        playerOpp = "w"

    # End square chess notation
    endSquareNotation = convertSquareNotation(moveLegal["endSquare"])

    # Chess notation
    moveLegalNotation = ""

    # Pawn
    if moveLegal["piece"] == "pawn":
        if moveLegal["type"] in ["capture", "enpassant"]:
            startSquareNotation = convertSquareNotation(moveLegal["startSquare"])
            moveLegalNotation += startSquareNotation[0]
            moveLegalNotation += "x"
        moveLegalNotation += endSquareNotation
        if moveLegal["promotion"] != "":
            moveLegalNotation += moveLegal["promotion"]

    # Bishop
    elif moveLegal["piece"] == "bishop":
        moveLegalNotation += "B"
        if moveLegal["type"] == "capture":
            moveLegalNotation += "x"
        moveLegalNotation += endSquareNotation

    # Knight
    elif moveLegal["piece"] == "knight":
        moveLegalNotation = "N"
        if moveLegal["type"] == "capture":
            moveLegalNotation += "x"
        moveLegalNotation += endSquareNotation

    # Rook
    elif moveLegal["piece"] == "rook":
        moveLegalNotation = "R"
        if moveLegal["type"] == "capture":
            moveLegalNotation += "x"
        moveLegalNotation += endSquareNotation

    # Queen
    elif moveLegal["piece"] == "queen":
        moveLegalNotation = "Q"
        if moveLegal["type"] == "capture":
            moveLegalNotation += "x"
        moveLegalNotation += endSquareNotation

    # King
    elif moveLegal["piece"] == "king":
        if moveLegal["type"] in ["0-0", "0-0-0"]:
            moveLegalNotation = moveLegal["type"]
        else:
            moveLegalNotation = "K"
            if moveLegal["type"] == "capture":
                moveLegalNotation += "x"
            moveLegalNotation += endSquareNotation

    # Check whether opponent is now in check
    # Start square and end square
    i0 = moveLegal["startSquare"][0]
    j0 = moveLegal["startSquare"][1]
    i1 = moveLegal["endSquare"][0]
    j1 = moveLegal["endSquare"][1]

    # Special moves
    isMoveCastle    = moveLegal["type"] in ["0-0", "0-0-0"]
    isMoveEnPassant = moveLegal["type"] == "enpassant"
    isMovePromotion = moveLegal["promotion"] in ["=B", "=N", "=R", "=Q"]

    boardNew = copy.deepcopy(board)
    if isMoveCastle:
        boardNew[i1][j1] = boardNew[i0][j0]
        boardNew[i0][j0] = "  "
        if (j1 < j0):
            boardNew[i1][0]    = "  "
            boardNew[i1][j1+1] = "{}R".format(player)
        elif (j1 > j0):
            boardNew[i1][7]    = "  "
            boardNew[i1][j1-1] = "{}R".format(player)
    elif isMoveEnPassant:
        boardNew[i1][j1] = boardNew[i0][j0]
        boardNew[i0][j0] = "  "
        boardNew[i0][j1] = "  "
    elif isMovePromotion:
        boardNew[i1][j1] = "{}{}".format(player, moveLegal["promotion"][1])
        boardNew[i0][j0] = "  "
    else:
        boardNew[i1][j1] = boardNew[i0][j0]
        boardNew[i0][j0] = "  "

    if inCheck(boardNew, playerOpp):
        moveLegalNotation += "+"

    return moveLegalNotation

# Name:        printStatus
# Purpose:     Print status
# Parameters:  playerTurn ("w" or "b"; player whose turn it is)
#              checkFlag (boolean)
#              checkmateFlag (boolean)
#              stalemateFlag (boolean)
# Returns:

def printStatus(playerTurn, checkFlag, checkmateFlag, stalemateFlag):
    # Whose turn is it?
    if playerTurn == "w":
        print("Whose turn?    {}White{}".format(ANSI_RED_BOLD, ANSI_END))
    elif playerTurn == "b":
        print("Whose turn?    {}Black{}".format(ANSI_BLUE_BOLD, ANSI_END))

    # Is player in check?
    if checkFlag:
        print("In check?      Yes")
    else:
        print("In check?      No")

    # Is player in checkmate?
    if checkmateFlag:
        print("In checkmate?  Yes")
    else:
        print("In checkmate?  No")

    # Is player in stalemate?
    if stalemateFlag:
        print("In stalemate?  Yes")
    else:
        print("In stalemate?  No")

    print("")
    return

# Name:        printMovesLegalNotation
# Purpose:     Given a piece, print legal moves
# Parameters:  text
#              movesLegalNotation (list of legal moves)
# Returns:

def printMovesLegalNotation(text, movesLegalNotation):
    print("  {:<6}  |  {:<10}  |  {}".format(text, len(movesLegalNotation), ", ".join(sorted(movesLegalNotation))))
    return

# Name:        main
# Purpose:     Given a legal chess position, determine all possible moves for player
# Parameters:
# Returns:

def main():
    # Position setup
    row8 = ["bR", "  ", "bB", "bQ", "bK", "bB", "bN", "bR"]
    row7 = ["  ", "bp", "bp", "  ", "  ", "bp", "bp", "bp"]
    row6 = ["bp", "  ", "bN", "bp", "  ", "  ", "  ", "  "]
    row5 = ["  ", "  ", "  ", "  ", "bp", "  ", "  ", "  "]
    row4 = ["wB", "  ", "  ", "  ", "wp", "  ", "  ", "  "]
    row3 = ["  ", "  ", "  ", "  ", "  ", "wN", "  ", "  "]
    row2 = ["wp", "wp", "wp", "wp", "  ", "wp", "wp", "wp"]
    row1 = ["wR", "wN", "wB", "wQ", "wK", "  ", "  ", "wR"]
    board = [row1, row2, row3, row4, row5, row6, row7, row8]

    playerTurn            = "w"
    canCastleKingside     = True
    canCastleQueenside    = True
    canCastleKingsideOpp  = True
    canCastleQueensideOpp = True
    enPassant             = ()

    # Set check flag
    checkFlag = inCheck(board, playerTurn)

    # Print board
    printBoard(board)

    # Piece positions
    squaresPawn   = []
    squaresBishop = []
    squaresKnight = []
    squaresRook   = []
    squaresQueen  = []
    squaresKing   = []
    for i in [0, 1, 2, 3, 4, 5, 6, 7]:
        for j in [0, 1, 2, 3, 4, 5, 6, 7]:
            if board[i][j][0] == playerTurn:
                if board[i][j][1] == "p":
                    squaresPawn.append((i, j))
                elif board[i][j][1] == "B":
                    squaresBishop.append((i, j))
                elif board[i][j][1] == "N":
                    squaresKnight.append((i, j))
                elif board[i][j][1] == "R":
                    squaresRook.append((i, j))
                elif board[i][j][1] == "Q":
                    squaresQueen.append((i, j))
                elif board[i][j][1] == "K":
                    squaresKing.append((i, j))

    # Determine candidate moves
    movesCand = []
    for square in squaresPawn:
        movesCand += findMovesCandPawn(board, playerTurn, enPassant, square)
    for square in squaresBishop:
        movesCand += findMovesCandBishop(board, playerTurn, square)
    for square in squaresKnight:
        movesCand += findMovesCandKnight(board, playerTurn, square)
    for square in squaresRook:
        movesCand += findMovesCandRook(board, playerTurn, square)
    for square in squaresQueen:
        movesCand += findMovesCandQueen(board, playerTurn, square)
    for square in squaresKing:
        movesCand += findMovesCandKing(board, playerTurn, canCastleKingside, canCastleQueenside, square)

    # Determine legal moves
    movesLegal = [moveCand for moveCand in movesCand if isMoveLegal(board, playerTurn, checkFlag, moveCand)]

    # Set checkmate and stalemate flags
    checkmateFlag = (len(movesLegal) == 0) and checkFlag
    stalemateFlag = (len(movesLegal) == 0) and not checkFlag

    # Print status
    printStatus(playerTurn, checkFlag, checkmateFlag, stalemateFlag)

    # Convert legal moves to chess notation, by piece
    movesLegalNotationPawn   = [convertMoveNotation(board, playerTurn, moveLegal) for moveLegal in movesLegal if moveLegal["piece"] == "pawn"]
    movesLegalNotationBishop = [convertMoveNotation(board, playerTurn, moveLegal) for moveLegal in movesLegal if moveLegal["piece"] == "bishop"]
    movesLegalNotationKnight = [convertMoveNotation(board, playerTurn, moveLegal) for moveLegal in movesLegal if moveLegal["piece"] == "knight"]
    movesLegalNotationRook   = [convertMoveNotation(board, playerTurn, moveLegal) for moveLegal in movesLegal if moveLegal["piece"] == "rook"]
    movesLegalNotationQueen  = [convertMoveNotation(board, playerTurn, moveLegal) for moveLegal in movesLegal if moveLegal["piece"] == "queen"]
    movesLegalNotationKing   = [convertMoveNotation(board, playerTurn, moveLegal) for moveLegal in movesLegal if moveLegal["piece"] == "king"]

    # Print summary of legal moves
    print("")
    print("  {:<6}  |  {:<10}  |  {}".format("Piece", "# of Moves", "Moves"))
    print("----------+--------------+----------------------------------------------------------")
    printMovesLegalNotation("Pawn",   movesLegalNotationPawn)
    printMovesLegalNotation("Bishop", movesLegalNotationBishop)
    printMovesLegalNotation("Knight", movesLegalNotationKnight)
    printMovesLegalNotation("Rook",   movesLegalNotationRook)
    printMovesLegalNotation("Queen",  movesLegalNotationQueen)
    printMovesLegalNotation("King",   movesLegalNotationKing)
    print("----------+--------------+----------------------------------------------------------")
    print("  {:<6}  |  {:<10}  |".format("Total", len(movesLegal)))
    print("")

    return

if __name__ == "__main__":
    main()
