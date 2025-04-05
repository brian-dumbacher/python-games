#Name:     hangman.py
#Purpose:  Play hangman
#Author:   Brian Dumbacher

import codecs
import re
import random

def cleanWord(w):
    w = w.lower()
    w = re.sub("\s+", " ", w);
    return w.strip()

def printHangman(life):
    print("")
    if life == 0:
        print("    @@@@@@@@@@@@@@        ")
        print("    @@           |        ")
        print("    @@          _|_       ")
        print("    @@         (*_*)      ")
        print("    @@          _|_       ")
        print("    @@   <<----(   )---->>")
        print("    @@          ( )       ")
        print("    @@          ( )       ")
        print("    @@         // \\\\    ")
        print("    @@        //   \\\\   ")
        print("    @@       <<     >>    ")
        print("    @@                    ")
        print("@@@@@@@@@@                ")
    elif life == 1:
        print("    @@@@@@@@@@@@@@        ")
        print("    @@           |        ")
        print("    @@          _|_       ")
        print("    @@         (*_*)      ")
        print("    @@          _|_       ")
        print("    @@   <<----(   )---->>")
        print("    @@          ( )       ")
        print("    @@          ( )       ")
        print("    @@         //         ")
        print("    @@        //          ")
        print("    @@       <<           ")
        print("    @@                    ")
        print("@@@@@@@@@@                ")
    elif life == 2:
        print("    @@@@@@@@@@@@@@        ")
        print("    @@           |        ")
        print("    @@          _|_       ")
        print("    @@         (*_*)      ")
        print("    @@          _|_       ")
        print("    @@   <<----(   )---->>")
        print("    @@          ( )       ")
        print("    @@          ( )       ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("@@@@@@@@@@                ")
    elif life == 3:
        print("    @@@@@@@@@@@@@@        ")
        print("    @@           |        ")
        print("    @@          _|_       ")
        print("    @@         (*_*)      ")
        print("    @@          _|_       ")
        print("    @@   <<----(   )      ")
        print("    @@          ( )       ")
        print("    @@          ( )       ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("@@@@@@@@@@                ")
    elif life == 4:
        print("    @@@@@@@@@@@@@@        ")
        print("    @@           |        ")
        print("    @@          _|_       ")
        print("    @@         (*_*)      ")
        print("    @@          _|_       ")
        print("    @@         (   )      ")
        print("    @@          ( )       ")
        print("    @@          ( )       ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("@@@@@@@@@@                ")
    elif life == 5:
        print("    @@@@@@@@@@@@@@        ")
        print("    @@           |        ")
        print("    @@          _|_       ")
        print("    @@         (*_*)      ")
        print("    @@          _|_       ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("@@@@@@@@@@                ")
    elif life == 6:
        print("    @@@@@@@@@@@@@@        ")
        print("    @@           |        ")
        print("    @@          _|_       ")
        print("    @@         (*_*)      ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("@@@@@@@@@@                ")
    elif life == 7:
        print("    @@@@@@@@@@@@@@        ")
        print("    @@           |        ")
        print("    @@           |        ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("    @@                    ")
        print("@@@@@@@@@@                ")
    print("")
    return

def printIncorrectGuesses(wordSet, guesses):
    text = "Incorrect: "
    for guess in guesses:
        if guess not in wordSet:
            text += guess.upper()
    print(text)
    print("")
    return

def printWord(word, guesses):
    text = "Word:     "
    for letter in word:
        if letter in guesses:
            text += " {}".format(letter.upper())
        else:
            text += " _"
    print(text)
    print("")
    return

def isValidGuess(guess):
    return guess in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def isNewGuess(guesses, guess):
    return guess not in guesses

def isCorrectGuess(wordSet, guess):
    return guess in wordSet

def isGameWon(wordSet, guesses):
    return wordSet <= set(guesses)

def printEndGame(word, winFlag):
    print("========================================")
    if winFlag:
        print("The word was indeed {}".format(word.upper()))
        print("You win!")
    else:
        print("I'm sorry. The word was {}".format(word.upper()))
        print("You lose.")
    print("========================================")
    print("")
    return

def playHangman(word):
    # Parameters
    winFlag = False
    life = 7
    guesses = []
    wordSet = set([l for l in word])
    
    # Guess loop
    while life > 0 and winFlag == False:
        printHangman(life)
        printIncorrectGuesses(wordSet, guesses)
        printWord(word, guesses)
        guess = ""
        while not isValidGuess(guess) or not isNewGuess(guesses, guess):
            guess = input("Guess:     ")
            guess = guess.lower()
        guesses.append(guess)
        if isCorrectGuess(wordSet, guess):
            winFlag = isGameWon(wordSet, guesses)
        else:
            life -= 1
    
    printHangman(life)
    printIncorrectGuesses(wordSet, guesses)
    printWord(word, guesses)
    printEndGame(word, winFlag)
    return

def main():
    # Global parameters
    words = []
    f = codecs.open("hangman_words.txt", "r")
    for w in f:
        words.append(cleanWord(w))
    f.close()
    random.seed()
    random.shuffle(words)
    gameCounter = 0
    loopFlag = True
    
    # Game loop
    while loopFlag:
        playHangman(words[gameCounter])
        gameCounter += 1
        if gameCounter == len(words):
            gameCounter = 0
        newGameInput = ""
        while newGameInput not in ["n", "no", "y", "yes"]:
            newGameInput = input("Another game? Y/N: ")
            newGameInput = newGameInput.lower()
        if newGameInput in ["n", "no"]:
            loopFlag = False
    print("")
    return

if __name__ == "__main__":
    main()
