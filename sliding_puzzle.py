#Name:     sliding_puzzle.py
#Purpose:  Play the 3x3 sliding puzzle

import random

def isPuzzleSolved(puzzle):
    return puzzle == [["1","2","3"],["4","5","6"],["7","8"," "]]

def slidesValid(puzzle):
    slides = []
    iBlank = 0
    jBlank = 0
    for i in [0,1,2]:
        for j in [0,1,2]:
            if puzzle[i][j] == " ":
                iBlank = i
                jBlank = j
    for i in [n for n in [iBlank-1,iBlank+1] if n in [0,1,2]]:
        slides.append(puzzle[i][jBlank])
    for j in [n for n in [jBlank-1,jBlank+1] if n in [0,1,2]]:
        slides.append(puzzle[iBlank][j])
    return slides

def randomPuzzle():
    puzzle = [["1","2","3"],["4","5","6"],["7","8"," "]]
    numSlides = 0
    while isPuzzleSolved(puzzle) or numSlides < 50:
        random.seed()
        slides = slidesValid(puzzle)
        slide = slides[random.randint(0, len(slides) - 1)]
        puzzle = updatePuzzle(puzzle, slide)
        numSlides = numSlides + 1
    return puzzle

def printPuzzle(puzzle):
    print("")
    print("@@@@@@@@@@@@@@@@@@@")
    print("@     @     @     @")
    print("@  " + puzzle[0][0] + "  @  " + puzzle[0][1] + "  @  " + puzzle[0][2] + "  @")
    print("@     @     @     @")
    print("@@@@@@@@@@@@@@@@@@@")
    print("@     @     @     @")
    print("@  " + puzzle[1][0] + "  @  " + puzzle[1][1] + "  @  " + puzzle[1][2] + "  @")
    print("@     @     @     @")
    print("@@@@@@@@@@@@@@@@@@@")
    print("@     @     @     @")
    print("@  " + puzzle[2][0] + "  @  " + puzzle[2][1] + "  @  " + puzzle[2][2] + "  @")
    print("@     @     @     @")
    print("@@@@@@@@@@@@@@@@@@@")
    print("")
    return

def validSlide(puzzle, slide):
    return slide in slidesValid(puzzle)

def updatePuzzle(puzzle, slide):
    iBlank = 0
    jBlank = 0
    iSlide = 0
    jSlide = 0
    for i in [0,1,2]:
        for j in [0,1,2]:
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
        while not validSlide(puzzle, slide):
            slide = input("Slide: ")
        numSlides = numSlides + 1
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
        while newPuzzle not in ["n", "y"]:
            newPuzzle = input("Another puzzle? Y/N: ")
            newPuzzle = newPuzzle.lower()
        if newPuzzle == "n":
            loopFlag = False
    print("")
    return

if __name__ == "__main__":
    main()
