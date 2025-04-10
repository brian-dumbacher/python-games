# Name:     spelling_bee.py
# Purpose:  Play the spelling bee game
# Author:   Brian Dumbacher

import codecs
import random
import re

# Name:        cleanWord
# Purpose:     Clean word
# Parameters:  word
# Returns:     wordClean (cleaned word)

def cleanWord(word):
    wordClean = word.upper()
    wordClean = re.sub("\s+", " ", wordClean)
    wordClean = wordClean.strip()
    return wordClean

# Name:        printPuzzle
# Purpose:     Print puzzle
# Parameters:  lettersReg (list of regular letters)
#              letterCenter (center letter)
#              words (list of words)
# Returns:

def printPuzzle(lettersReg, letterCenter, words):
    print("")
    print("        +---+        ")
    print("       /     \       ")
    print("      +   {}   +      ".format(lettersReg[0]))
    print("  +---+       +---+  ")
    print(" /     \     /     \ ")
    print("+   {}   +---+   {}   +".format(lettersReg[1], lettersReg[2]))
    print("+       +---+       +")
    print(" \     /     \     / ")
    print("  +---+   {}   +---+  ".format(letterCenter))
    print("  +---+       +---+  ")
    print(" /     \     /     \ ")
    print("+   {}   +---+   {}   +".format(lettersReg[3], lettersReg[4]))
    print("+       +---+       +")
    print(" \     /     \     / ")
    print("  +---+   {}   +---+  ".format(lettersReg[5]))
    print("      +       +      ")
    print("       \     /       ")
    print("        +---+        ")
    print("")
    print("Words found:")
    for word in words:
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
#              lettersReg (list of regular letters)
#              letterCenter (center letter)
#              word (proposed word)
# Returns:     True (word is valid) or False (word is invalid)

def isWordValid(dictionary, lettersReg, letterCenter, word):
    lettersFull = [l for l in lettersReg] + [letterCenter]
    return (len(word) >= 5) and (letterCenter in settify(word)) and (settify(word) <= settify(lettersFull)) and (word in dictionary)

# Name:        calcScore
# Purpose:     Calculate score for valid word
# Parameters:  lettersReg (list of regular letters)
#              letterCenter (center letter)
#              word (valid word)
# Returns:     3 (full score) or 1 (normal score)

def calcScore(lettersReg, letterCenter, word):
    lettersFull = lettersReg + [letterCenter]
    return 3 if settify(word) == settify(lettersFull) else 1

# Name:        printEndGame
# Purpose:     Print results of game
# Parameters:  words (list of valid words)
#              score (total score)
# Returns:

def printEndGame(words, score):
    print("")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@   You found {} words.".format(len(words)))
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
    f = codecs.open("spelling_bee_dictionary.txt", "r")
    for w in f:
        dictionary.append(cleanWord(w))
    f.close()
    words = []
    score = 0
    continueFlag = True
    lettersReg = ["F", "I", "N", "O", "T", "U"]
    random.seed()
    random.shuffle(lettersReg)
    letterCenter = "R"
    
    # Word loop
    while continueFlag == True:
        printPuzzle(lettersReg, letterCenter, words)
        word = input("Word (q to quit): ")
        word = word.lower()
        word = word.strip()
        if word == "q":
            continueFlag = False
        else:
            if isWordValid(dictionary, lettersReg, letterCenter, word):
                words.append(word)
                words.sort()
                score += calcScore(lettersReg, letterCenter, word)
    
    # Game results
    printEndGame(words, score)
    return

if __name__ == "__main__":
    main()
