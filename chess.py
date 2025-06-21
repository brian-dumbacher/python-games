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
        print("{} {} |{}".format(ANSI_BLACK, i+1, ANSI_END), end="")
        for j in [0, 1, 2, 3, 4, 5, 6, 7]:
            if board[i][j] == "  ":
                square = "{}.{}".format(ANSI_GREY, ANSI_END)
            elif board[i][j][0] == "w":
                square = "{}{}{}".format(ANSI_RED_BOLD, board[i][j][1], ANSI_END)
            elif board[i][j][0] == "b":
                square = "{}{}{}".format(ANSI_BLUE_BOLD, board[i][j][1], ANSI_END)
            print(" {}".format(square), end="")
        print("")
    print("{}     ---------------{}".format(ANSI_BLACK, ANSI_END))
    print("{}     a b c d e f g h{}".format(ANSI_BLACK, ANSI_END))
    print("")
    return

# Name:        findMoveSquaresPawn
# Purpose:     Determine squares that a pawn can move to
# Parameters:  board (2D list)
#              player ("w" or "b")
#              enPassant
#              square (i, j)
# Returns:     List of move squares

def findMoveSquaresPawn(board, player, enPassant, square):
    # Opponent
    if player == "w":
        playerOpp = "b"
        d = 1
    elif player == "b":
        playerOpp = "w"
        d = -1

    i = square[0]
    j = square[1]
    moveSquares = []

    # One square ahead
    if board[i+d][j] == "  ":
        moveSquares.append([i+d, j])

    # Two squares ahead
    if (player == "w" and i == 1) or (player == "b" and i == 6):
        if (board[i+d][j] == "  ") and (board[i+2*d][j] == "  "):
            moveSquares.append([i+2*d, j])

    # Capture
    if j >= 1:
        if board[i+d][j-1][0] == playerOpp:
            moveSquares.append([i+d, j-1])
    if j <= 6:
        if board[i+d][j+1][0] == playerOpp:
            moveSquares.append([i+d, j+1])

    # en passant
    if enPassant != []:
        iEP = enPassant[0]
        jEP = enPassant[1]
        if (i == iEP) and (abs(j - jEP) == 1):
            moveSquares.append([iEP+d, jEP])

    return moveSquares

# Name:        findMoveSquaresBishop
# Purpose:     Determine squares that a bishop can move to
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of move squares

def findMoveSquaresBishop(board, player, square):
    # Opponent
    if player == "w":
        playerOpp = "b"
    elif player == "b":
        playerOpp = "w"

    i = square[0]
    j = square[1]
    moveSquares = []

    # Up-Right
    blocked = False
    numSquares = min([7-i, 7-j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i+d][j+d] == "  ":
                moveSquares.append((i+d, j+d))
            else:
                blocked = True
                if board[i+d][j+d][0] == playerOpp:
                    moveSquares.append((i+d, j+d))

    # Down-Right
    blocked = False
    numSquares = min([i, 7-j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i-d][j+d] == "  ":
                moveSquares.append((i-d, j+d))
            else:
                blocked = True
                if board[i-d][j+d][0] == playerOpp:
                    moveSquares.append((i-d, j+d))

    # Down-Left
    blocked = False
    numSquares = min([i, j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i-d][j-d] == "  ":
                moveSquares.append((i-d, j-d))
            else:
                blocked = True
                if board[i-d][j-d][0] == playerOpp:
                    moveSquares.append((i-d, j-d))

    # Up-Left
    blocked = False
    numSquares = min([7-i, j])
    for d in range(1, numSquares + 1):
        if not blocked:
            if board[i+d][j-d] == "  ":
                moveSquares.append((i+d, j-d))
            else:
                blocked = True
                if board[i+d][j-d][0] == playerOpp:
                    moveSquares.append((i+d, j-d))

    return moveSquares

# Name:        findMoveSquaresKnight
# Purpose:     Determine squares that a knight can move to
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of move squares

def findMoveSquaresKnight(board, player, square):
    # Opponent
    if player == "w":
        playerOpp = "b"
    elif player == "b":
        playerOpp = "w"

    i = square[0]
    j = square[1]

    moveSquaresEight = [(i+2, j+1), (i+1, j+2), (i-1, j+2), (i-2, j+1), (i-2, j-1), (i-1, j-2), (i+1, j-2), (i+2, j-1)]
    moveSquares = []
    for moveSquare in moveSquaresEight:
        if moveSquare[0] in [0, 1, 2, 3, 4, 5, 6, 7] and moveSquare[1] in [0, 1, 2, 3, 4, 5, 6, 7]:
            if board[moveSquare[0]][moveSquare[1]][0] in [" ", playerOpp]:
                moveSquares.append(moveSquare)

    return moveSquares

# Name:        findMoveSquaresRook
# Purpose:     Determine squares that a rook can move to
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of move squares

def findMoveSquaresRook(board, player, square):
    # Opponent
    if player == "w":
        playerOpp = "b"
    elif player == "b":
        playerOpp = "w"

    i = square[0]
    j = square[1]
    moveSquares = []

    # Up
    blocked = False
    for z in [ii for ii in [1, 2, 3, 4, 5, 6, 7] if ii > i]:
        if not blocked:
            if board[z][j] == "  ":
                moveSquares.append((z, j))
            else:
                blocked = True
                if board[z][j][0] == playerOpp:
                    moveSquares.append((z, j))

    # Down
    blocked = False
    for z in [ii for ii in [6, 5, 4, 3, 2, 1, 0] if ii < i]:
        if not blocked:
            if board[z][j] == "  ":
                moveSquares.append((z, j))
            else:
                blocked = True
                if board[z][j][0] == playerOpp:
                    moveSquares.append((z, j))

    # Right
    blocked = False
    for z in [jj for jj in [1, 2, 3, 4, 5, 6, 7] if jj > j]:
        if not blocked:
            if board[i][z] == "  ":
                moveSquares.append((i, z))
            else:
                blocked = True
                if board[i][z][0] == playerOpp:
                    moveSquares.append((i, z))

    # Left
    blocked = False
    for z in [jj for jj in [6, 5, 4, 3, 2, 1, 0] if jj < j]:
        if not blocked:
            if board[i][z] == "  ":
                moveSquares.append((i, z))
            else:
                blocked = True
                if board[i][z][0] == playerOpp:
                    moveSquares.append((i, z))

    return moveSquares

# Name:        findMoveSquaresQueen
# Purpose:     Determine squares that a queen can move to
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of move squares

def findMoveSquaresQueen(board, player, square):
    return findMoveSquaresBishop(board, player, square) + findMoveSquaresRook(board, player, square)

# Name:        findMoveSquaresKing
# Purpose:     Determine squares that a king can move to
# Parameters:  board (2D list)
#              player ("w" or "b")
#              canCastleKingside (boolean)
#              canCastleQueenside (boolean)
#              square (i, j)
# Returns:     List of move squares

def findMoveSquaresKing(board, player, canCastleKingside, canCastleQueenside, square):
    # Opponent
    if player == "w":
        playerOpp = "b"
    elif player == "b":
        playerOpp = "w"

    i = square[0]
    j = square[1]

    moveSquaresEight = [(i+1, j), (i+1, j+1), (i, j+1), (i-1, j+1), (i-1, j), (i-1, j-1), (i, j-1), (i+1, j-1)]
    moveSquares = []
    for moveSquare in moveSquaresEight:
        if moveSquare[0] in [0, 1, 2, 3, 4, 5, 6, 7] and moveSquare[1] in [0, 1, 2, 3, 4, 5, 6, 7]:
            if board[moveSquare[0]][moveSquare[1]][0] in [" ", playerOpp]:
                moveSquares.append(moveSquare)

    # Castling
    if canCastleKingside:
        if ((player == "w") and (i == 0) and (j == 4)) or ((player == "b") and (i == 7) and (j == 4)):
            if (board[i][j+1] == "  ") and (board[i][j+2] == "  ") and (board[i][j+3] == (player + "R")):
                moveSquares.append((i, j+2))
    if canCastleQueenside:
        if ((player == "w") and (i == 0) and (j == 4)) or ((player == "b") and (i == 7) and (j == 4)):
            if (board[i][j-1] == "  ") and (board[i][j-2] == "  ") and (board[i][j-3] == "  ") and (board[i][j-4] == (player + "R")):
                moveSquares.append((i, j-2))

    return moveSquares

# Name:        findAttackSquaresPawn
# Purpose:     Determine squares that a pawn can attack
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of attack squares

def findAttackSquaresPawn(board, player, square):
    # Opponent
    if player == "w":
        playerOpp = "b"
        d = 1
    elif player == "b":
        playerOpp = "w"
        d = -1

    i = square[0]
    j = square[1]
    attackSquares = []

    # Capture
    if j >= 1:
        if board[i+d][j-1][0] in [" ", playerOpp]:
            attackSquares.append((i+d, j-1))
    if j <= 6:
        if board[i+d][j+1][0] in [" ", playerOpp]:
            attackSquares.append((i+d, j+1))

    return attackSquares

# Name:        findAttackSquaresBishop
# Purpose:     Determine squares that a bishop can attack
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of attack squares

def findAttackSquaresBishop(board, player, square):
    return findMoveSquaresBishop(board, player, square)

# Name:        findAttackSquaresKnight
# Purpose:     Determine squares that a knight can attack
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of attack squares

def findAttackSquaresKnight(board, player, square):
    return findMoveSquaresKnight(board, player, square)

# Name:        findAttackSquaresRook
# Purpose:     Determine squares that a rook can attack
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of attack squares

def findAttackSquaresRook(board, player, square):
    return findMoveSquaresRook(board, player, square)

# Name:        findAttackSquaresQueen
# Purpose:     Determine squares that a queen can attack
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of attack squares

def findAttackSquaresQueen(board, player, square):
    return findMoveSquaresQueen(board, player, square)

# Name:        findAttackSquaresKing
# Purpose:     Determine squares that a king can attack
# Parameters:  board (2D list)
#              player ("w" or "b")
#              square (i, j)
# Returns:     List of attack squares

def findAttackSquaresKing(board, player, square):
    # Opponent
    if player == "w":
        playerOpp = "b"
    elif player == "b":
        playerOpp = "w"

    i = square[0]
    j = square[1]

    attackSquaresEight = [(i+1, j), (i+1, j+1), (i, j+1), (i-1, j+1), (i-1, j), (i-1, j-1), (i, j-1), (i+1, j-1)]
    attackSquares = []
    for attackSquare in attackSquaresEight:
        if attackSquare[0] in [0, 1, 2, 3, 4, 5, 6, 7] and attackSquare[1] in [0, 1, 2, 3, 4, 5, 6, 7]:
            if board[attackSquare[0]][attackSquare[1]][0] in [" ", playerOpp]:
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
            elif board[i][j] == player + "K":
                squareKing = (i, j)
    
    # Possible moves
    attackSquares = []
    for square in squaresPawnOpp:
        attackSquares.extend(findAttackSquaresPawn(board, playerOpp, square))
    for square in squaresBishopOpp:
        attackSquares.extend(findAttackSquaresBishop(board, playerOpp, square))
    for square in squaresKnightOpp:
        attackSquares.extend(findAttackSquaresKnight(board, playerOpp, square))
    for square in squaresRookOpp:
        attackSquares.extend(findAttackSquaresRook(board, playerOpp, square))
    for square in squaresQueenOpp:
        attackSquares.extend(findAttackSquaresQueen(board, playerOpp, square))
    for square in squaresKingOpp:
        attackSquares.extend(findAttackSquaresKing(board, playerOpp, square))
    
    # Determine whether king is in check
    for attackSquare in attackSquares:
        if attackSquare == squareKing:
            return True

    return False

# Name:        isLegalMove
# Purpose:     Determine whether candidate move is legal
# Parameters:  board (2D list)
#              player ("w" or "b")
#              checkFlag (boolean)
#              move (candidate move)
# Returns:

def isLegalMove(board, player, checkFlag, move):
    # Move components
    i0 = move[0][0]
    j0 = move[0][1]
    i1 = move[1][0]
    j1 = move[1][1]

    # Castling flags
    isMoveCastle = (board[i0][j0][1] == "K") and (abs(j1 - j0) == 2)
    canCastleFlag = False
    legalTransitFlag = False
    if isMoveCastle and not checkFlag:
        canCastleFlag = True
        jTransit = int((j0 + j1)/2)
        boardNew = copy.deepcopy(board)
        boardNew[i1][jTransit] = boardNew[i0][j0]
        boardNew[i0][j0] = "  "
        legalTransitFlag = not inCheck(boardNew, player)

    # End square
    boardNew = copy.deepcopy(board)
    boardNew[i1][j1] = boardNew[i0][j0]
    boardNew[i0][j0] = "  "
    legalEndFlag = not inCheck(boardNew, player)

    return (isMoveCastle and canCastleFlag and legalTransitFlag and legalEndFlag) or (not isMoveCastle and legalEndFlag)

# Name:        convertSquareCoord
# Purpose:     Convert square to board coordinates
# Parameters:  square (i, j)
# Returns:     square in board coordinates (e.g., "e4")

def convertSquareCoord(square):
    i = square[0]
    j = square[1]
    row = i + 1
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

# Name:        convertMoveCoord
# Purpose:     Convert move to board coordinates
# Parameters:  move ((i0, j0), (i1, j1))
# Returns:     move in board coordinates (e.g., "e4-e5")

def convertMoveCoord(move):
    return "{}-{}".format(convertSquareCoord(move[0]), convertSquareCoord(move[1]))

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

# Name:        printMovesLegalCoord
# Purpose:     Print legal moves
# Parameters:  text (beginning text)
#              movesLegalCoord (list of legal moves)
# Returns:

def printMovesLegalCoord(text, movesLegalCoord):
    print(text, end="")
    print(", ".join(movesLegalCoord))
    return

# Name:        main
# Purpose:     Given a legal chess position, determine all possible moves for player
# Parameters:
# Returns:

def main():
    # Position setup
    row8 = ["bR", "  ", "bB", "bQ", "bK", "bB", "bN", "bR"]
    row7 = ["  ", "bp", "bp", "bp", "  ", "bp", "bp", "bp"]
    row6 = ["bp", "  ", "bN", "  ", "  ", "  ", "  ", "  "]
    row5 = ["  ", "wB", "  ", "  ", "bp", "  ", "  ", "  "]
    row4 = ["  ", "  ", "  ", "  ", "wp", "  ", "  ", "  "]
    row3 = ["  ", "  ", "  ", "  ", "  ", "wN", "  ", "  "]
    row2 = ["wp", "wp", "wp", "wp", "  ", "wp", "wp", "wp"]
    row1 = ["wR", "wN", "wB", "wQ", "wK", "  ", "  ", "wR"]
    board = [row1, row2, row3, row4, row5, row6, row7, row8]
    playerTurn = "w"
    canCastleKingside = True
    canCastleQueenside = True
    enPassant = []

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

    # Possible moves
    # Pawns
    movesPawnCand = []
    for square in squaresPawn:
        movesPawnCand.extend([[square, moveSquare] for moveSquare in findMoveSquaresPawn(board, playerTurn, enPassant, square)])
    movesPawnLegal = [move for move in movesPawnCand if isLegalMove(board, playerTurn, checkFlag, move)]
    movesPawnLegalCoord = [convertMoveCoord(move) for move in movesPawnLegal]
    movesPawnLegalCoord.sort()

    # Bishops
    movesBishopCand = []
    for square in squaresBishop:
        movesBishopCand.extend([[square, moveSquare] for moveSquare in findMoveSquaresBishop(board, playerTurn, square)])
    movesBishopLegal = [move for move in movesBishopCand if isLegalMove(board, playerTurn, checkFlag, move)]
    movesBishopLegalCoord = [convertMoveCoord(move) for move in movesBishopLegal]
    movesBishopLegalCoord.sort()

    # Knights
    movesKnightCand = []
    for square in squaresKnight:
        movesKnightCand.extend([[square, moveSquare] for moveSquare in findMoveSquaresKnight(board, playerTurn, square)])
    movesKnightLegal = [move for move in movesKnightCand if isLegalMove(board, playerTurn, checkFlag, move)]
    movesKnightLegalCoord = [convertMoveCoord(move) for move in movesKnightLegal]
    movesKnightLegalCoord.sort()

    # Rooks
    movesRookCand = []
    for square in squaresRook:
        movesRookCand.extend([[square, moveSquare] for moveSquare in findMoveSquaresRook(board, playerTurn, square)])
    movesRookLegal = [move for move in movesRookCand if isLegalMove(board, playerTurn, checkFlag, move)]
    movesRookLegalCoord = [convertMoveCoord(move) for move in movesRookLegal]
    movesRookLegalCoord.sort()

    # Queens
    movesQueenCand = []
    for square in squaresQueen:
        movesQueenCand.extend([[square, moveSquare] for moveSquare in findMoveSquaresQueen(board, playerTurn, square)])
    movesQueenLegal = [move for move in movesQueenCand if isLegalMove(board, playerTurn, checkFlag, move)]
    movesQueenLegalCoord = [convertMoveCoord(move) for move in movesQueenLegal]
    movesQueenLegalCoord.sort()

    # King
    movesKingCand = []
    for square in squaresKing:
        movesKingCand.extend([[square, moveSquare] for moveSquare in findMoveSquaresKing(board, playerTurn, canCastleKingside, canCastleQueenside, square)])
    movesKingLegal = [move for move in movesKingCand if isLegalMove(board, playerTurn, checkFlag, move)]
    movesKingLegalCoord = [convertMoveCoord(move) for move in movesKingLegal]
    movesKingLegalCoord.sort()

    # All pawns and pieces
    movesLegalCoord = movesPawnLegalCoord + movesBishopLegalCoord + movesKnightLegalCoord + movesRookLegalCoord + movesQueenLegalCoord + movesKingLegalCoord

    # Set checkmate and stalemate flags
    checkmateFlag = (len(movesLegalCoord) == 0) and checkFlag
    stalemateFlag = (len(movesLegalCoord) == 0) and not checkFlag

    # Print status
    printStatus(playerTurn, checkFlag, checkmateFlag, stalemateFlag)

    # Print moves
    print("Possible Moves:")
    printMovesLegalCoord("Pawn   | ", movesPawnLegalCoord)
    printMovesLegalCoord("Bishop | ", movesBishopLegalCoord)
    printMovesLegalCoord("Knight | ", movesKnightLegalCoord)
    printMovesLegalCoord("Rook   | ", movesRookLegalCoord)
    printMovesLegalCoord("Queen  | ", movesQueenLegalCoord)
    printMovesLegalCoord("King   | ", movesKingLegalCoord)
    print("")
    return

if __name__ == "__main__":
    main()
