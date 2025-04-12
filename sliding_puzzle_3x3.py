# Name:     sliding_puzzle_3x3.py
# Purpose:  Solve the 3x3 sliding puzzle
# Author:   Brian Dumbacher

import random

# Name:        isPuzzleSolved
# Purpose:     Determine whether puzzle is solved
# Parameters:  puzzle (2D array)
# Returns:     True (puzzle is solved) or False (puzzle is not solved)

def isPuzzleSolved(puzzle):
    return puzzle == [["1", "2", "3"], ["4", "5", "6"], ["7", "8", " "]]

# Name:        getValidSlides
# Purpose:     Get list of valid slides
# Parameters:  puzzle (2D array)
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

# Name:        randomPuzzle
# Purpose:     Generate random puzzle
# Parameters:
# Returns:     puzzle (random 2D array)

def randomPuzzle():
    puzzle = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", " "]]
    numSlides = 0
    while isPuzzleSolved(puzzle) or numSlides < 50:
        random.seed()
        slides = getValidSlides(puzzle)
        slide = slides[random.randint(0, len(slides) - 1)]
        puzzle = updatePuzzle(puzzle, slide)
        numSlides += 1
    return puzzle

# Name:        printPuzzle
# Purpose:     Print puzzle in current state
# Parameters:  puzzle (2D array)
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

# Name:        isValidSlide
# Purpose:     Determine whether proposed slide is valid
# Parameters:  puzzle (2D array)
#              slideProposed (proposed slide)
# Returns:     True (proposed slide is valid) or False (proposed slide is invalid)

def isValidSlide(puzzle, slideProposed):
    return slideProposed in getValidSlides(puzzle)

# Name:        updatePuzzle
# Purpose:     Update puzzle based on valid slide
# Parameters:  puzzle (2D array)
#              slideValid (valid slide)
# Returns:     puzzle (updated 2D array)

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
# Purpose:     Print puzzle results
# Parameters:  numSlides (number of slides)
# Returns:

def printEndPuzzle(numSlides):
    print("==================================================")
    print("You solved the 3x3 sliding puzzle in {} slides.".format(numSlides))
    print("==================================================")
    print("")
    return

# Name:        solvePuzzle
# Purpose:     Solve a 3x3 sliding puzzle
# Parameters:
# Returns:

def solvePuzzle():
    # Parameters
    puzzle = randomPuzzle()
    solveFlag = False
    numSlides = 0
    
    # Slide loop
    while solveFlag == False:
        printPuzzle(puzzle)
        slide = ""
        while not isValidSlide(puzzle, slide):
            slide = input("Slide: ")
        numSlides += 1
        puzzle = updatePuzzle(puzzle, slide)
        solveFlag = isPuzzleSolved(puzzle)

    # Puzzle results
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
        solvePuzzle()
        newPuzzleInput = ""
        while newPuzzleInput not in ["n", "no", "y", "yes"]:
            newPuzzleInput = input("Another puzzle? (Y/N): ")
            newPuzzleInput = newPuzzleInput.lower()
        if newPuzzleInput in ["n", "no"]:
            loopFlag = False

    print("")
    return

if __name__ == "__main__":
    main()
