# Name:     spelling_bee.py
# Purpose:  Play Spelling Bee
# Author:   Brian Dumbacher
# Date:     May 26, 2025

import io
import random
import re

# Name:        cleanWord
# Purpose:     Clean word
# Parameters:  wordRaw (raw word)
# Returns:     wordClean (cleaned word)

def cleanWord(wordRaw):
    wordClean = wordRaw.upper()
    wordClean = re.sub("\s+", " ", wordClean)
    wordClean = wordClean.strip()
    return wordClean

# Name:        printPuzzle
# Purpose:     Print puzzle
# Parameters:  lettersNormal (list of normal letters)
#              letterCenter (center letter)
#              wordsValid (list of valid words)
# Returns:

def printPuzzle(lettersNormal, letterCenter, wordsValid):
    print("")
    print("        +---+        ")
    print("       /     \       ")
    print("      +   {}   +      ".format(lettersNormal[0]))
    print("  +---+       +---+  ")
    print(" /     \     /     \ ")
    print("+   {}   +---+   {}   +".format(lettersNormal[1], lettersNormal[2]))
    print("+       +---+       +")
    print(" \     /     \     / ")
    print("  +---+   {}   +---+  ".format(letterCenter))
    print("  +---+       +---+  ")
    print(" /     \     /     \ ")
    print("+   {}   +---+   {}   +".format(lettersNormal[3], lettersNormal[4]))
    print("+       +---+       +")
    print(" \     /     \     / ")
    print("  +---+   {}   +---+  ".format(lettersNormal[5]))
    print("      +       +      ")
    print("       \     /       ")
    print("        +---+        ")
    print("")
    print("Words found:")
    for word in wordsValid:
        print(word)
    print("")
    return

# Name:        settify
# Purpose:     Convert input list or string to set format
# Parameters:  listOrString (list or string)
# Returns:     Set version of input list or string

def settify(listOrString):
    return set(l for l in listOrString)

# Name:        isWordValid
# Purpose:     Determine whether word is valid
# Parameters:  dictionary (list of valid words)
#              lettersNormal (list of normal letters)
#              letterCenter (center letter)
#              word (proposed word)
# Returns:     True (word is valid) or False (word is invalid)

def isWordValid(dictionary, lettersNormal, letterCenter, word):
    lettersFull = [l for l in lettersNormal] + [letterCenter]
    return (len(word) >= 5) and (letterCenter in settify(word)) and (settify(word) <= settify(lettersFull)) and (word in dictionary)

# Name:        calcScore
# Purpose:     Calculate score for valid word
# Parameters:  lettersNormal (list of normal letters)
#              letterCenter (center letter)
#              wordValid (valid word)
# Returns:     3 (full score) or 1 (normal score)

def calcScore(lettersNormal, letterCenter, wordValid):
    lettersFull = lettersNormal + [letterCenter]
    return 3 if settify(wordValid) == settify(lettersFull) else 1

# Name:        printEndGame
# Purpose:     Print results of game
# Parameters:  wordsValid (list of valid words)
#              score (final score)
# Returns:

def printEndGame(wordsValid, score):
    print("")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   You found {} words.".format(len(wordsValid)))
    print("@@@   Your final score = {}.".format(score))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("")
    return

# Name:        main
# Purpose:     Play Spelling Bee
# Parameters:
# Returns:

def main():
    # Parameters
    dictionary = []
    f = io.open("spelling_bee_dictionary.txt", "r")
    for w in f:
        dictionary.append(cleanWord(w))
    f.close()
    wordsValid = []
    score = 0
    continueFlag = True
    lettersNormal = ["F", "I", "N", "O", "T", "U"]
    random.seed()
    random.shuffle(lettersNormal)
    letterCenter = "R"
    
    # Word loop
    while continueFlag == True:
        printPuzzle(lettersNormal, letterCenter, wordsValid)
        word = input("Word (q to quit): ")
        word = word.upper().strip()
        if word == "Q":
            continueFlag = False
        else:
            if isWordValid(dictionary, lettersNormal, letterCenter, word):
                wordsValid.append(word)
                wordsValid.sort()
                score += calcScore(lettersNormal, letterCenter, word)
    
    # Game results
    printEndGame(wordsValid, score)
    return

if __name__ == "__main__":
    main()
