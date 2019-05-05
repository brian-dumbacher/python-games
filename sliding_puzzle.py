#Name:     sliding_puzzle.py
#Purpose:  Solve the 3x3 sliding puzzle

import random

def randomPuzzle():
    nums = [n for n in range(0, 9)]
    mix = nums
    while mix != nums:
        random.seed()
        random.shuffle(mix)
    return [mix[0:3],mix[3:6],mix[6:9]]

def numToString(num):
    s = ""
    if num == 0:
        s = " "
    else:
        s = str(num)
    return s

def printPuzzle(puzzle):
    print("")
    print("@@@@@@@@@@@@@")
    print("@   @   @   @")
    print("@ " + numToString(puzzle[0][0]) + " @ " + numToString(puzzle[0][1]) + " @ " + numToString(puzzle[0][2]) + " @")
    print("@   @   @   @")
    print("@@@@@@@@@@@@@")
    print("@   @   @   @")
    print("@ " + numToString(puzzle[1][0]) + " @ " + numToString(puzzle[1][1]) + " @ " + numToString(puzzle[1][2]) + " @")
    print("@   @   @   @")
    print("@@@@@@@@@@@@@")
    print("@   @   @   @")
    print("@ " + numToString(puzzle[2][0]) + " @ " + numToString(puzzle[2][1]) + " @ " + numToString(puzzle[2][2]) + " @")
    print("@   @   @   @")
    print("@@@@@@@@@@@@@")
    print("")
    return

def invalidSlide(puzzle, slide):
    slidesValid = []
    iZero = 0
    jZero = 0
    for i in [0,1,2]:
        for j in [0,1,2]:
            if puzzle[i][j] == 0:
                iZero = i
                jZero = j
    for i in [n for n in [iZero-1,iZero+1] if n in [0,1,2]]:
        slidesValid.append(str(puzzle[i][jZero]))
    for j in [n for n in [jZero-1,jZero+1] if n in [0,1,2]]:
        slidesValid.append(str(puzzle[iZero][j]))
    return slide not in slidesValid

def updatePuzzle(puzzle, slide):
    iZero = 0
    jZero = 0
    iSlide = 0
    jSlide = 0
    for i in [0,1,2]:
        for j in [0,1,2]:
            if puzzle[i][j] == 0:
                iZero = i
                jZero = j
            elif str(puzzle[i][j]) == slide:
                iSlide = i
                jSlide = j
    puzzle[iZero][jZero] = int(slide)
    puzzle[iSlide][jSlide] = 0
    return puzzle

def solvePuzzle(puzzle):
    return puzzle == [[1,2,3],[4,5,6],[7,8,0]]

def printEndPuzzle(numSlides):
    print("==================================================")
    print("You solved the puzzle in " + str(numSlides) + " slides.")
    print("Congratulations!")
    print("==================================================")
    print("")
    return

def playPuzzle(puzzleStart):
    
    #Parameters
    solveFlag = False
    puzzle = puzzleStart
    numSlides = 0
    
    #Slide loop
    while solveFlag == False:
        printPuzzle(puzzle)
        slide = ""
        while invalidSlide(puzzle, slide):
            slide = input("Slide: ")
        numSlides = numSlides + 1
        puzzle = updatePuzzle(puzzle, slide)
        solveFlag = solvePuzzle(puzzle)
    
    printPuzzle(puzzle)
    printEndPuzzle(numSlides)
    
    return

def main():
    
    #Global parameters
    loopFlag = True
    
    #Game loop
    while loopFlag:
        puzzleStart = randomPuzzle()
        playPuzzle(puzzleStart)
        newPuzzle = ""
        while newPuzzle not in ["n", "y"]:
            newPuzzle = input("Another puzzle? Y/N: ")
            newPuzzle = newPuzzle.lower()
        if newPuzzle == "n":
            loopFlag = False
    print("")
    
    return

if __name__ == "__main__":
    main()
