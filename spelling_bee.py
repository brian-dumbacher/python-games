#Name:     spelling_bee.py
#Purpose:  Play the spelling bee game

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
    print("Words:")
    for word in words:
        print(word)
    print("")
    return

def settify(listOrString):
    return set([c for c in listOrString])

def wordValid(lettersReg, letterCenter, word):
    return (len(word) >= 5 and letterCenter in settify(word)) and (settify(word) <= settify(lettersReg.append(letterCenter)))

def printEndPuzzle(words):
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
        if word in ["Q","QUIT","EXIT"]:
            continueFlag = False
        else:
            if wordValid(lettersReg, letterCenter, word):
                words.append(word)
    
    printEndPuzzle(words)
    return

if __name__ == "__main__":
    main()
