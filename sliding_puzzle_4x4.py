#Name:     sliding_puzzle_4x4.py
#Purpose:  Play the 4x4 sliding puzzle
#Author:   Brian Dumbacher

import random

def isPuzzleSolved(puzzle):
    return puzzle == [["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","15"," "]]

def slidesValid(puzzle):
    slides = []
    iBlank = 0
    jBlank = 0
    for i in [0,1,2,3]:
        for j in [0,1,2,3]:
            if puzzle[i][j] == " ":
                iBlank = i
                jBlank = j
    for i in [n for n in [iBlank-1,iBlank+1] if n in [0,1,2,3]]:
        slides.append(puzzle[i][jBlank])
    for j in [n for n in [jBlank-1,jBlank+1] if n in [0,1,2,3]]:
        slides.append(puzzle[iBlank][j])
    return slides

def randomPuzzle():
    puzzle = [["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","15"," "]]
    numSlides = 0
    while isPuzzleSolved(puzzle) or numSlides < 100:
        random.seed()
        slides = slidesValid(puzzle)
        slide = slides[random.randint(0, len(slides) - 1)]
        puzzle = updatePuzzle(puzzle, slide)
        numSlides += 1
    return puzzle

def pn(c):
    #pn short for print number
    if c in [" ","1","2","3","4","5","6","7","8","9"]:
        return " " + c
    return c

def printPuzzle(puzzle):
    print("")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@      @      @      @      @")
    print("@  " + pn(puzzle[0][0]) + "  @  " + pn(puzzle[0][1]) + "  @  " + pn(puzzle[0][2]) + "  @  " + pn(puzzle[0][3]) + "  @")
    print("@      @      @      @      @")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@      @      @      @      @")
    print("@  " + pn(puzzle[1][0]) + "  @  " + pn(puzzle[1][1]) + "  @  " + pn(puzzle[1][2]) + "  @  " + pn(puzzle[1][3]) + "  @")
    print("@      @      @      @      @")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@      @      @      @      @")
    print("@  " + pn(puzzle[2][0]) + "  @  " + pn(puzzle[2][1]) + "  @  " + pn(puzzle[2][2]) + "  @  " + pn(puzzle[2][3]) + "  @")
    print("@      @      @      @      @")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@      @      @      @      @")
    print("@  " + pn(puzzle[3][0]) + "  @  " + pn(puzzle[3][1]) + "  @  " + pn(puzzle[3][2]) + "  @  " + pn(puzzle[3][3]) + "  @")
    print("@      @      @      @      @")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("")
    return

def validSlide(puzzle, slide):
    return slide in slidesValid(puzzle)

def updatePuzzle(puzzle, slide):
    iBlank = 0
    jBlank = 0
    iSlide = 0
    jSlide = 0
    for i in [0,1,2,3]:
        for j in [0,1,2,3]:
            if puzzle[i][j] == " ":
                iBlank = i
                jBlank = j
            elif puzzle[i][j] == slide:
                iSlide = i
                jSlide = j
    puzzle[iBlank][jBlank] = slide
    puzzle[iSlide][jSlide] = " "
    return puzzle

def printEndPuzzle(numSlides):
    print("==================================================")
    print("You solved the 4x4 sliding puzzle in " + str(numSlides) + " slides.")
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
        while not validSlide(puzzle, slide):
            slide = input("Slide: ")
        numSlides += 1
        puzzle = updatePuzzle(puzzle, slide)
        solveFlag = isPuzzleSolved(puzzle)
    
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
        while newPuzzle not in ["n", "no", "y", "yes"]:
            newPuzzle = input("Another puzzle? Y/N: ")
            newPuzzle = newPuzzle.lower()
        if newPuzzle in ["n", "no"]:
            loopFlag = False
    print("")
    return

if __name__ == "__main__":
    main()
