#Name:     chess.py
#Purpose:  Execute chess moves

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

def validMoveStart(board, moveStart):
    validFlag = False
    if len(moveStart) == 2:
        if moveStart[0] in ["a","b","c","d","e","f","g","h"] and moveStart[1] in ["1","2","3","4","5","6","7","8"]:
            moveStartConvert = convertMove(moveStart)
            i = moveStartConvert[0]
            j = moveStartConvert[1]
            validFlag = (board[i][j] != "")
    return validFlag

def validMoveEnd(board, moveStart, moveEnd):
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

def main():
    
    #Global parameters
    row1 = ["wR","wN","wB","wQ","wK","wB","wN","wR"]
    row2 = ["wp","wp","wp","wp","wp","wp","wp","wp"]
    row3 = ["","","","","","","",""]
    row4 = ["","","","","","","",""]
    row5 = ["","","","","","","",""]
    row6 = ["","","","","","","",""]
    row7 = ["bp","bp","bp","bp","bp","bp","bp","bp"]
    row8 = ["bR","bN","bB","bQ","bK","bB","bN","bR"]
    board = [row1, row2, row3, row4, row5, row6, row7, row8]
    
    printBoard(board)
    print("White to move")
    moveStart = ""
    moveEnd = ""
    while not validMoveStart(board, moveStart):
        moveStart = input("Start square: ")
        moveStart = moveStart.lower()
    while not validMoveEnd(board, moveStart, moveEnd):
        moveEnd = input("End square: ")
        moveEnd = moveEnd.lower()
    board = updateBoard(board, moveStart, moveEnd)
    printBoard(board)

    return

if __name__ == "__main__":
    main()
