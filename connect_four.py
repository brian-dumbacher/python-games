# Name:     connect_four.py
# Purpose:  Play connect four
# Author:   Brian Dumbacher

import random

# Name:        printBoard
# Purpose:     Print the board to the screen
# Parameters:  board (2D list)
# Returns:

def printBoard(board):
    ansiGREY = "\x1b[90m"
    ansiBLUE = "\x1b[94m"
    ansiTEAL = "\x1b[96m"
    ansiEND  = "\x1b[0m"
    print("")
    for i in [5, 4, 3, 2, 1, 0]:
        print("{}   |{}".format(ansiTEAL, ansiEND), end="")
        for j in [0, 1, 2, 3, 4, 5, 6]:
            if board[i][j] == " ":
                square = "{}.{}".format(ansiGREY, ansiEND)
            elif board[i][j] == "h":
                square = "o"
            elif board[i][j] == "c":
                square = "{}x{}".format(ansiBLUE, ansiEND)
            print(" {}".format(square), end="")
        print("")
    print("{}     -------------{}".format(ansiTEAL, ansiEND))
    print("{}     1 2 3 4 5 6 7{}".format(ansiTEAL, ansiEND))
    print("")
    return

# Name:        isValidMove
# Purpose:     Determine whether move is valid given the board
# Parameters:  board (2D list)
#              move
# Returns:     True (move is valid) or False (move is invalid)

def isValidMove(board, move):
    return True if move in ["1", "2", "3", "4", "5", "6", "7"] and board[5][int(move) - 1] == " " else False

# Name:        updateBoard
# Purpose:     Update the board
# Parameters:  board (2D list)
#              move
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
#              move
#              player ("c" or "h")
# Returns:     True (move is winning) or False (move is not winning)

def isWinningMove(board, move, player):
    row6Win = [" ", " ", " ", " ", " ", " ", " "]
    row5Win = [" ", " ", " ", " ", " ", " ", " "]
    row4Win = [" ", " ", " ", " ", " ", " ", " "]
    row3Win = [" ", " ", " ", " ", " ", " ", " "]
    row2Win = [" ", " ", " ", " ", " ", " ", " "]
    row1Win = [" ", " ", " ", " ", " ", " ", " "]
    boardWin = [row1Win, row2Win, row3Win, row4Win, row5Win, row6Win]
    for i in [0, 1, 2, 3, 4, 5]:
        for j in [0, 1, 2, 3, 4, 5, 6]:
            boardWin[i][j] = board[i][j]
    boardWin = updateBoard(boardWin, move, player)
    return isGameWon(boardWin, player)

# Name:        isLosingMove
# Purpose:     Determine whether move is losing for given player
# Parameters:  board (2D list)
#              move
#              player ("c" or "h")
# Returns:     True (move is losing) or False (move is not losing)

def isLosingMove(board, move, player):
    if player == "c":
        playerOpp = "h"
    elif player == "h":
        playerOpp = "c"
    
    row6New = [" ", " ", " ", " ", " ", " ", " "]
    row5New = [" ", " ", " ", " ", " ", " ", " "]
    row4New = [" ", " ", " ", " ", " ", " ", " "]
    row3New = [" ", " ", " ", " ", " ", " ", " "]
    row2New = [" ", " ", " ", " ", " ", " ", " "]
    row1New = [" ", " ", " ", " ", " ", " ", " "]
    boardNew = [row1New, row2New, row3New, row4New, row5New, row6New]
    for i in [0, 1, 2, 3, 4, 5]:
        for j in [0, 1, 2, 3, 4, 5, 6]:
            boardNew[i][j] = board[i][j]
    boardNew = updateBoard(boardNew, move, player)
    
    columns = ["1", "2", "3", "4", "5", "6", "7"]
    validMovesNew = [move for move in columns if isValidMove(boardNew, move)]
    for move in validMovesNew:
        if isWinningMove(boardNew, move, playerOpp):
            return True
    return False

# Name:        getMoveComputer
# Purpose:     Get computer player's move
# Parameters:  board (2D list)
#              moveHuman
# Returns:     computerMove (computer player's move)

def getMoveComputer(board, moveHuman):
    # Classify valid moves
    columns = ["1", "2", "3", "4", "5", "6", "7"]
    validMoves = [move for move in columns if isValidMove(board, move)]
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
    print("==================================================")
    if winHuman:
        print("You win!")
    elif winComputer:
        print("You lose.")
    else:
        print("Tie game.")
    print("==================================================")
    print("")
    return

# Name:        playConnectFour
# Purpose:     Play a game of Connect Four
# Parameters:
# Returns:

def playConnectFour():
    # Board setup
    row6 = [" ", " ", " ", " ", " ", " ", " "]
    row5 = [" ", " ", " ", " ", " ", " ", " "]
    row4 = [" ", " ", " ", " ", " ", " ", " "]
    row3 = [" ", " ", " ", " ", " ", " ", " "]
    row2 = [" ", " ", " ", " ", " ", " ", " "]
    row1 = [" ", " ", " ", " ", " ", " ", " "]
    board = [row1, row2, row3, row4, row5, row6]
    winHuman = False
    winComputer = False
    boardFull = False
        
    # Move loop
    while (not winHuman) and (not winComputer) and (not boardFull):
        printBoard(board)
        # Human move
        moveHuman = ""
        while not isValidMove(board, moveHuman):
            moveHuman = input("Column: ")
        board = updateBoard(board, moveHuman, "h")
        winHuman = isGameWon(board, "h")
        # Computer move
        if not winHuman:
            moveComputer = getMoveComputer(board, moveHuman)        
            board = updateBoard(board, moveComputer, "c")
            winComputer = isGameWon(board, "c")
            boardFull = isBoardFull(board)
    
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
        newGame = ""
        while newGame not in ["n", "no", "y", "yes"]:
            newGame = input("Another game? Y/N: ")
            newGame = newGame.lower()
        if newGame in ["n", "no"]:
            loopFlag = False
    print("")
    return

if __name__ == "__main__":
    main()
