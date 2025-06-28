# Name:     connect_four.py
# Purpose:  Play Connect Four
# Author:   Brian Dumbacher
# Date:     May 24, 2025

import copy
import random

# Name:        printBoard
# Purpose:     Print board in current state
# Parameters:  board (2D list)
# Returns:

def printBoard(board):
    # ANSI escape codes
    ANSI_BLACK     = "\x1b[30m"
    ANSI_RED_BOLD  = "\x1b[1;31m"
    ANSI_BLUE_BOLD = "\x1b[1;34m"
    ANSI_GREY      = "\x1b[37m"
    ANSI_END       = "\x1b[0m"

    # Print board
    print("")
    for i in [5, 4, 3, 2, 1, 0]:
        print("{}   |{}".format(ANSI_BLACK, ANSI_END), end="")
        for j in [0, 1, 2, 3, 4, 5, 6]:
            if board[i][j] == " ":
                square = "{}.{}".format(ANSI_GREY, ANSI_END)
            elif board[i][j] == "h":
                square = "{}o{}".format(ANSI_BLUE_BOLD, ANSI_END)
            elif board[i][j] == "c":
                square = "{}x{}".format(ANSI_RED_BOLD, ANSI_END)
            print(" {}".format(square), end="")
        print("")
    print("{}     -------------{}".format(ANSI_BLACK, ANSI_END))
    print("{}     1 2 3 4 5 6 7{}".format(ANSI_BLACK, ANSI_END))
    print("")

    return

# Name:        isValidMove
# Purpose:     Determine whether candidate move is valid
# Parameters:  board (2D list)
#              moveCand (candidate move)
# Returns:     True (candidate move is valid) or False (candidate move is invalid)

def isValidMove(board, moveCand):
    return True if moveCand in ["1", "2", "3", "4", "5", "6", "7"] and board[5][int(moveCand) - 1] == " " else False

# Name:        updateBoard
# Purpose:     Update the board after valid move
# Parameters:  board (2D list)
#              moveValid (valid move)
#              player ("c" or "h")
# Returns:     updated board (2D list)

def updateBoard(board, moveValid, player):
    j = int(moveValid) - 1
    for i in [0, 1, 2, 3, 4, 5]:
        if board[i][j] == " ":
            board[i][j] = player
            break

    return board

# Name:        isGameWon
# Purpose:     Determine whether the given player has won the game
# Parameters:  board (2D list)
#              player ("c" or "h")
# Returns:     True (player has won) or False (player has not won)

def isGameWon(board, player):
    # Check rows
    for i in [0, 1, 2, 3, 4, 5]:
        for j in [0, 1, 2, 3]:
            if (board[i][j] == player) and (board[i][j+1] == player) and (board[i][j+2] == player) and (board[i][j+3] == player):
                return True

    # Check columns
    for j in [0, 1, 2, 3, 4, 5, 6]:
        for i in [0, 1, 2]:
            if (board[i][j] == player) and (board[i+1][j] == player) and (board[i+2][j] == player) and (board[i+3][j] == player):
                return True

    # Check SW-NE diagonals
    for j in [0, 1, 2, 3]:
        for i in [0, 1, 2]:
            if (board[i][j] == player) and (board[i+1][j+1] == player) and (board[i+2][j+2] == player) and (board[i+3][j+3] == player):
                return True

    # Check SE-NW diagonals
    for j in [3, 4, 5, 6]:
        for i in [0, 1, 2]:
            if (board[i][j] == player) and (board[i+1][j-1] == player) and (board[i+2][j-2] == player) and (board[i+3][j-3] == player):
                return True

    return False

# Name:        isWinningMove
# Purpose:     Determine whether move is winning for given player
# Parameters:  board (2D list)
#              moveValid (valid move)
#              player ("c" or "h")
# Returns:     True (move is winning) or False (move is not winning)

def isWinningMove(board, moveValid, player):
    # Update board with valid move
    boardNew = copy.deepcopy(board)
    boardNew = updateBoard(boardNew, moveValid, player)

    return isGameWon(boardNew, player)

# Name:        isLosingMove
# Purpose:     Determine whether move is losing for given player
# Parameters:  board (2D list)
#              moveValid (valid move)
#              player ("c" or "h")
# Returns:     True (move is losing) or False (move is not losing)

def isLosingMove(board, moveValid, player):
    # Opponent
    if player == "c":
        playerOpp = "h"
    elif player == "h":
        playerOpp = "c"

    # Update board with valid move
    boardNew = copy.deepcopy(board)
    boardNew = updateBoard(boardNew, moveValid, player)
    
    # Determine opponent's valid moves and check whether at least one is winning
    validMovesNew = [moveCand for moveCand in ["1", "2", "3", "4", "5", "6", "7"] if isValidMove(boardNew, moveCand)]
    for moveValidNew in validMovesNew:
        if isWinningMove(boardNew, moveValidNew, playerOpp):
            return True

    return False

# Name:        getComputerMove
# Purpose:     Get computer player's move
# Parameters:  board (2D list)
#              moveHuman (last human move)
# Returns:     moveComputer (computer player's move)

def getComputerMove(board):
    # Classify valid moves as winning, neutral, or losing
    validMoves   = [moveCand for moveCand in ["1", "2", "3", "4", "5", "6", "7"] if isValidMove(board, moveCand)]
    winningMoves = []
    neutralMoves = []
    losingMoves  = []
    for move in validMoves:
        if isWinningMove(board, move, "c"):
            winningMoves.append(move)
        elif isLosingMove(board, move, "c"):
            losingMoves.append(move)
        else:
            neutralMoves.append(move)

    # Set random seed
    random.seed()

    # Randomly choose a winning move
    if len(winningMoves) > 0:
        random.shuffle(winningMoves)
        moveComputer = winningMoves[0]

    # Else, randomly choose a neutral move
    elif len(neutralMoves) > 0:
        random.shuffle(neutralMoves)
        moveComputer = neutralMoves[0]

    # Else, randomly choose a losing move
    else:
        random.shuffle(losingMoves)
        moveComputer = losingMoves[0]

    return moveComputer

# Name:        isBoardFull
# Purpose:     Check whether the board is full
# Parameters:  board (2D list)
# Returns:     True (the board is full) or False (the board is not full)

def isBoardFull(board):
    for j in [0, 1, 2, 3, 4, 5, 6]:
        if board[5][j] == " ":
            return False

    return True

# Name:        printEndGame
# Purpose:     Print results of game
# Parameters:  winHuman (Boolean value indicating whether the human player won)
#              winComputer (Boolean value indicating whether the computer player won)
# Returns:

def printEndGame(winHuman, winComputer):
    # Message
    mssg = ""
    if winHuman:
        mssg = "You win!"
    elif winComputer:
        mssg = "You lose."
    else:
        mssg = "Tie game."
    n = len(mssg)

    # Print message
    print("@" * (n + 12))
    print("@@@   {}   @@@".format(mssg))
    print("@" * (n + 12))
    print("")

    return

# Name:        playConnectFour
# Purpose:     Play a game of Connect Four
# Parameters:
# Returns:

def playConnectFour():
    # Board setup
    board       = [[" " for j in range(7)] for i in range(6)]
    winHuman    = False
    winComputer = False
    boardFull   = False
        
    # Move loop
    while (not winHuman) and (not winComputer) and (not boardFull):
        # Print board
        printBoard(board)

        # Human move
        moveHuman = ""
        while not isValidMove(board, moveHuman):
            moveHuman = input("Your move (column #):  ")
            moveHuman = moveHuman.strip()
        board = updateBoard(board, moveHuman, "h")
        winHuman = isGameWon(board, "h")

        # Computer move
        if not winHuman:
            moveComputer = getComputerMove(board)        
            board = updateBoard(board, moveComputer, "c")
            winComputer = isGameWon(board, "c")
            boardFull = isBoardFull(board)

    # Game results
    printBoard(board)
    printEndGame(winHuman, winComputer)
    return

# Name:        main
# Purpose:     Loop through multiple games of Connect Four
# Parameters:
# Returns:

def main():
    # Parameters
    loopFlag = True

    # Game loop
    while loopFlag:
        playConnectFour()
        newGameInput = ""
        while newGameInput not in ["Y", "YES", "N", "NO"]:
            newGameInput = input("Another game? (Y/N):  ")
            newGameInput = newGameInput.upper().strip()
        if newGameInput in ["N", "NO"]:
            loopFlag = False

    print("")
    return

if __name__ == "__main__":
    main()
