# Name:     connect_four.py
# Purpose:  Play connect four
# Author:   Brian Dumbacher

import random

# Name:        printBoard
# Purpose:     Print the board to the screen
# Parameters:  board (2D list)
# Returns:

def printBoard(board):
    ANSI_BLACK     = "\x1b[30m"
    ANSI_RED_BOLD  = "\x1b[1;31m"
    ANSI_BLUE_BOLD = "\x1b[1;34m"
    ANSI_GREY      = "\x1b[37m"
    ANSI_END       = "\x1b[0m"
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
# Purpose:     Determine whether the proposed move is valid
# Parameters:  board (2D list)
#              move (proposed move)
# Returns:     True (move is valid) or False (move is invalid)

def isValidMove(board, move):
    return True if move in ["1", "2", "3", "4", "5", "6", "7"] and board[5][int(move) - 1] == " " else False

# Name:        updateBoard
# Purpose:     Update the board
# Parameters:  board (2D list)
#              move (valid move)
#              player ("c" or "h")
# Returns:     updated board (2D list)

def updateBoard(board, move, player):
    j = int(move) - 1
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
    # Rows
    for i in [0, 1, 2, 3, 4, 5]:
        for j in [0, 1, 2, 3]:
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                return True
    # Columns
    for j in [0, 1, 2, 3, 4, 5, 6]:
        for i in [0, 1, 2]:
            if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
                return True
    # SW-NE Diagonals
    for j in [0, 1, 2, 3]:
        for i in [0, 1, 2]:
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                return True
    # SE-NW Diagonals
    for j in [3, 4, 5, 6]:
        for i in [0, 1, 2]:
            if board[i][j] == player and board[i+1][j-1] == player and board[i+2][j-2] == player and board[i+3][j-3] == player:
                return True
    return False

# Name:        isWinningMove
# Purpose:     Determine whether move is winning for given player
# Parameters:  board (2D list)
#              move (valid move)
#              player ("c" or "h")
# Returns:     True (move is winning) or False (move is not winning)

def isWinningMove(board, move, player):
    boardWin = [[" " for j in range(7)] for i in range(6)]
    for i in [0, 1, 2, 3, 4, 5]:
        for j in [0, 1, 2, 3, 4, 5, 6]:
            boardWin[i][j] = board[i][j]
    boardWin = updateBoard(boardWin, move, player)
    return isGameWon(boardWin, player)

# Name:        isLosingMove
# Purpose:     Determine whether move is losing for given player
# Parameters:  board (2D list)
#              move (valid move)
#              player ("c" or "h")
# Returns:     True (move is losing) or False (move is not losing)

def isLosingMove(board, move, player):
    if player == "c":
        playerOpp = "h"
    elif player == "h":
        playerOpp = "c"
    
    boardNew = [[" " for j in range(7)] for i in range(6)]
    for i in [0, 1, 2, 3, 4, 5]:
        for j in [0, 1, 2, 3, 4, 5, 6]:
            boardNew[i][j] = board[i][j]
    boardNew = updateBoard(boardNew, move, player)
    
    validMovesNew = [move for move in ["1", "2", "3", "4", "5", "6", "7"] if isValidMove(boardNew, move)]
    for move in validMovesNew:
        if isWinningMove(boardNew, move, playerOpp):
            return True
    return False

# Name:        getMoveComputer
# Purpose:     Get computer player's move
# Parameters:  board (2D list)
#              moveHuman (last human move)
# Returns:     computerMove (computer player's move)

def getMoveComputer(board, moveHuman):
    # Classify valid moves
    validMoves = [move for move in ["1", "2", "3", "4", "5", "6", "7"] if isValidMove(board, move)]
    winningMoves = []
    otherMoves = []
    losingMoves = []
    for move in validMoves:
        if isWinningMove(board, move, "c"):
            winningMoves.append(move)
        elif isLosingMove(board, move, "c"):
            losingMoves.append(move)
        else:
            otherMoves.append(move)
    random.seed()
    # Randomly choose winning move
    if len(winningMoves) > 0:
        random.shuffle(winningMoves)
        computerMove = winningMoves[0]
    # Randomly choose other move
    elif len(otherMoves) > 0:
        random.shuffle(otherMoves)
        computerMove = otherMoves[0]
    # Randomly choose losing move
    else:
        random.shuffle(losingMoves)
        computerMove = losingMoves[0]
    return computerMove

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
    mssg = ""
    if winHuman:
        mssg = "You win!"
    elif winComputer:
        mssg = "You lose."
    else:
        mssg = "Tie game."
    n = len(mssg)
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
    board = [[" " for j in range(7)] for i in range(6)]
    winHuman = False
    winComputer = False
    boardFull = False
        
    # Move loop
    while (not winHuman) and (not winComputer) and (not boardFull):
        printBoard(board)
        # Human move
        moveHuman = ""
        while not isValidMove(board, moveHuman):
            moveHuman = input("Your move (column #): ")
        board = updateBoard(board, moveHuman, "h")
        winHuman = isGameWon(board, "h")
        # Computer move
        if not winHuman:
            moveComputer = getMoveComputer(board, moveHuman)        
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
        while newGameInput not in ["n", "no", "y", "yes"]:
            newGameInput = input("Another game? (Y/N): ")
            newGameInput = newGameInput.lower()
        if newGameInput in ["n", "no"]:
            loopFlag = False
    print("")
    return

if __name__ == "__main__":
    main()
