# Name:     sliding_puzzle_3x3.py
# Purpose:  Play the 3x3 sliding puzzle
# Author:   Brian Dumbacher
# Date:     June 30, 2025

import random

# Name:        isPuzzleSolved
# Purpose:     Determine whether puzzle is solved
# Parameters:  puzzle (2D list)
# Returns:     True (puzzle is solved) or False (puzzle is not solved)

def isPuzzleSolved(puzzle):
    return puzzle == [["1", "2", "3"], ["4", "5", "6"], ["7", "8", " "]]

# Name:        getValidSlides
# Purpose:     Get valid slides
# Parameters:  puzzle (2D list)
# Returns:     slidesValid (list of valid slides)

def getValidSlides(puzzle):
    slidesValid = []
    iBlank = 0
    jBlank = 0
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            if puzzle[i][j] == " ":
                iBlank = i
                jBlank = j
    for i in [n for n in [iBlank-1, iBlank+1] if n in [0, 1, 2]]:
        slidesValid.append(puzzle[i][jBlank])
    for j in [n for n in [jBlank-1, jBlank+1] if n in [0, 1, 2]]:
        slidesValid.append(puzzle[iBlank][j])
    return slidesValid

# Name:        getRandomPuzzle
# Purpose:     Generate random 3x3 sliding puzzle
# Parameters:
# Returns:     puzzle (2D list)

def getRandomPuzzle():
    puzzle = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", " "]]
    numSlides = 0
    while isPuzzleSolved(puzzle) or numSlides < 50:
        random.seed()
        slides = getValidSlides(puzzle)
        slide  = slides[random.randint(0, len(slides) - 1)]
        puzzle = updatePuzzle(puzzle, slide)
        numSlides += 1
    return puzzle

# Name:        printPuzzle
# Purpose:     Print puzzle in its current state
# Parameters:  puzzle (2D list)
# Returns:

def printPuzzle(puzzle):
    print("")
    print("@@@@@@@@@@@@@@@@@@@")
    print("@     @     @     @")
    print("@  {}  @  {}  @  {}  @".format(puzzle[0][0], puzzle[0][1], puzzle[0][2]))
    print("@     @     @     @")
    print("@@@@@@@@@@@@@@@@@@@")
    print("@     @     @     @")
    print("@  {}  @  {}  @  {}  @".format(puzzle[1][0], puzzle[1][1], puzzle[1][2]))
    print("@     @     @     @")
    print("@@@@@@@@@@@@@@@@@@@")
    print("@     @     @     @")
    print("@  {}  @  {}  @  {}  @".format(puzzle[2][0], puzzle[2][1], puzzle[2][2]))
    print("@     @     @     @")
    print("@@@@@@@@@@@@@@@@@@@")
    print("")
    return

# Name:        isSlideValid
# Purpose:     Determine whether candidate slide is valid
# Parameters:  puzzle (2D list)
#              slideCand (candidate slide)
# Returns:     True (candidate slide is valid) or False (candidate slide is invalid)

def isSlideValid(puzzle, slideCand):
    return slideCand in getValidSlides(puzzle)

# Name:        updatePuzzle
# Purpose:     Update puzzle with valid slide
# Parameters:  puzzle (2D list)
#              slideValid (valid slide)
# Returns:     puzzle (updated 2D list)

def updatePuzzle(puzzle, slideValid):
    iBlank = 0
    jBlank = 0
    iSlide = 0
    jSlide = 0
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            if puzzle[i][j] == " ":
                iBlank = i
                jBlank = j
            elif puzzle[i][j] == slideValid:
                iSlide = i
                jSlide = j
    puzzle[iBlank][jBlank] = slideValid
    puzzle[iSlide][jSlide] = " "
    return puzzle

# Name:        printEndPuzzle
# Purpose:     Print end of puzzle
# Parameters:  numSlides (number of slides)
# Returns:

def printEndPuzzle(numSlides):
    print("==================================================")
    print("You solved the 3x3 sliding puzzle in {} slide{}.".format(numSlides, "s" * (numSlides > 1)))
    print("==================================================")
    print("")
    return

# Name:        playPuzzle
# Purpose:     Play 3x3 sliding puzzle
# Parameters:  puzzleStart (starting puzzle as a 2D list)
# Returns:

def playPuzzle(puzzleStart):
    # Parameters
    solveFlag = False
    puzzle    = puzzleStart
    numSlides = 0
    
    # Slide loop
    while solveFlag == False:
        printPuzzle(puzzle)
        slide = ""
        while not isSlideValid(puzzle, slide):
            slide = input("Slide:  ")
        numSlides += 1
        puzzle    = updatePuzzle(puzzle, slide)
        solveFlag = isPuzzleSolved(puzzle)
    
    printPuzzle(puzzle)
    printEndPuzzle(numSlides)
    return

# Name:        main
# Purpose:     Loop through multiple 3x3 sliding puzzles
# Parameters:
# Returns:

def main():
    # Loop flag
    loopFlag = True
    
    # Puzzle loop
    while loopFlag:
        puzzleStart = getRandomPuzzle()
        playPuzzle(puzzleStart)
        newPuzzle = ""
        while newPuzzle not in ["N", "NO", "Y", "YES"]:
            newPuzzle = input("Another 3x3 sliding puzzle? (Y/N):  ")
            newPuzzle = newPuzzle.upper().strip()
        if newPuzzle in ["N", "NO"]:
            loopFlag = False

    print("")
    return

if __name__ == "__main__":
    main()
