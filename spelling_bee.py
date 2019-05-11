#Name:     spelling_bee.py
#Purpose:  Play the spelling bee game
#Author:   Brian Dumbacher

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
    return set([l for l in listOrString])

def wordValid(lettersReg, letterCenter, word):
    lettersFull = [l for l in lettersReg]
    lettersFull.append(letterCenter)
    return (len(word) >= 5) and (letterCenter in settify(word)) and (settify(word) <= settify(lettersFull))

def printScore(words):
    print("")
    print("==================================================")
    print("You found " + str(len(words)) + " words.")
    print("==================================================")
    print("")
    return

def main():
    #Parameters
    continueFlag = True
    lettersReg = ["T","O","U","F","N","I"]
    letterCenter = "R"
    words = []
    
    #Slide loop
    while continueFlag == True:
        printPuzzle(lettersReg, letterCenter, words)
        word = input("Word: ")
        word = word.upper()
        word = word.strip()
        if word in ["E","EX","EXI","EXIT","S","ST","STO","STOP","Q","QU","QUI","QUIT"]:
            continueFlag = False
        else:
            if wordValid(lettersReg, letterCenter, word):
                words.append(word)
    
    #Print end
    printScore(words)
    return

if __name__ == "__main__":
    main()
