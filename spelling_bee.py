#Name:     spelling_bee.py
#Purpose:  Play the spelling bee game
#Author:   Brian Dumbacher

import codecs
import random
import re

def cleanWord(w):
    w = w.upper()
    w = re.sub("\s+", " ", w);
    return w.strip()

def printPuzzle(lettersReg, letterCenter, words):
    print("")
    print("        +---+        ")
    print("       /     \       ")
    print("      +   " + lettersReg[0] + "   +      ")
    print("  +---+       +---+  ")
    print(" /     \     /     \ ")
    print("+   " + lettersReg[1] + "   +---+   " + lettersReg[2] + "   +")
    print("+       +---+       +")
    print(" \     /     \     / ")
    print("  +---+   " + letterCenter + "   +---+  ")
    print("  +---+       +---+  ")
    print(" /     \     /     \ ")
    print("+   " + lettersReg[3] + "   +---+   " + lettersReg[4] + "   +")
    print("+       +---+       +")
    print(" \     /     \     / ")
    print("  +---+   " + lettersReg[5] + "   +---+  ")
    print("      +       +      ")
    print("       \     /       ")
    print("        +---+        ")
    print("")
    print("Words found:")
    for word in words:
        print(word)
    print("")
    return

def settify(listOrString):
    return set(l for l in listOrString)

def wordValid(dictionary, lettersReg, letterCenter, word):
    lettersFull = [l for l in lettersReg] + [letterCenter]
    return (len(word) >= 5) and (letterCenter in settify(word)) and (settify(word) <= settify(lettersFull)) and (word in dictionary)

def getScore(lettersReg, letterCenter, word):
    lettersFull = [l for l in lettersReg]
    lettersFull.append(letterCenter)
    return 3 if settify(word) == settify(lettersFull) else 1

def printScore(words, score):
    print("")
    print("==================================================")
    print("You found " + str(len(words)) + " words.")
    print("Your score is " + str(score) + ".")
    print("==================================================")
    print("")
    return

def main():
    #Parameters
    dictionary = []
    f = codecs.open("spelling_bee_dictionary.txt", "r")
    for w in f:
        dictionary.append(cleanWord(w))
    f.close()
    words = []
    score = 0
    continueFlag = True
    lettersReg = ["F","I","N","O","T","U"]
    random.seed()
    random.shuffle(lettersReg)
    letterCenter = "R"
    
    #Slide loop
    while continueFlag == True:
        printPuzzle(lettersReg, letterCenter, words)
        word = input("Word (q to quit): ")
        word = word.upper()
        word = word.strip()
        if word in ["Q", "QUIT"]:
            continueFlag = False
        else:
            if wordValid(dictionary, lettersReg, letterCenter, word):
                words.append(word)
                words.sort()
                score += getScore(lettersReg, letterCenter, word)
    
    #Print score
    printScore(words, score)
    return

if __name__ == "__main__":
    main()
