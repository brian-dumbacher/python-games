#Name:     chess.py
#Purpose:  Execute chess moves

def printBoard(board):
    print("")
    for i in [7,6,5,4,3,2,1,0]:
        print(" " + str(i+1) + " | ", end="")
        for j in [0,1,2,3,4,5,6,7]:
            square = " "
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

    return

if __name__ == "__main__":
    main()
