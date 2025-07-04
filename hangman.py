# Name:     hangman.py
# Purpose:  Play Hangman
# Author:   Brian Dumbacher
# Date:     June 19, 2025

import io
import random
import re

# Name:        cleanWord
# Purpose:     Clean word by converting it to uppercase and stripping whitespace
# Parameters:  wordRaw (raw word)
# Returns:     wordClean (cleaned word)

def cleanWord(wordRaw):
    wordClean = wordRaw.upper()
    wordClean = re.sub("\s+", " ", wordClean)
    wordClean = wordClean.strip()
    return wordClean

# Name:        printHangman
# Purpose:     Print Hangman in current state
# Parameters:  life (life total)
# Returns:

def printHangman(life):
    print("")
    if life == 0:
        print("    @@@@@@@@@@@@@@        ")
        print("    @@           |        ")
        print("    @@           |        ")
        print("    @@          _|_       ")
        print("    @@         (o_o)      ")
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
        print("    @@           |        ")
        print("    @@          _|_       ")
        print("    @@         (o_o)      ")
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
        print("    @@           |        ")
        print("    @@          _|_       ")
        print("    @@         (o_o)      ")
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
        print("    @@           |        ")
        print("    @@          _|_       ")
        print("    @@         (o_o)      ")
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
        print("    @@           |        ")
        print("    @@          _|_       ")
        print("    @@         (o_o)      ")
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
        print("    @@           |        ")
        print("    @@          _|_       ")
        print("    @@         (o_o)      ")
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
    elif life == 7:
        print("    @@@@@@@@@@@@@@        ")
        print("    @@                    ")
        print("    @@                    ")
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

# Name:        printIncorrectGuesses
# Purpose:     Print incorrect guesses
# Parameters:  wordSet (set of letters in target word)
#              guesses (list of guesses)
# Returns:

def printIncorrectGuesses(wordSet, guesses):
    text = "Incorrect: "
    for guess in guesses:
        if guess not in wordSet:
            text += guess.upper()
    print(text)
    print("")
    return

# Name:        printCorrectGuesses
# Purpose:     Print correct guesses
# Parameters:  word (target word)
#              guesses (list of guesses)
# Returns:

def printCorrectGuesses(word, guesses):
    text = "Word:     "
    for letter in word:
        if letter in guesses:
            text += " {}".format(letter.upper())
        else:
            text += " _"
    print(text)
    print("")
    return

# Name:        isValidGuess
# Purpose:     Determine whether guess is valid
# Parameters:  guess
# Returns:     True (guess is a letter) or False (guess is not a letter)

def isValidGuess(guess):
    return guess in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Name:        isNewGuess
# Purpose:     Determine whether guess is new
# Parameters:  guesses (list of guesses)
#              guess
# Returns:     True (guess is new) or False (guess is not new)

def isNewGuess(guesses, guess):
    return guess not in guesses

# Name:        isCorrectGuess
# Purpose:     Determine whether guess is correct
# Parameters:  wordSet (set of letters in target word)
#              guess
# Returns:     True (guess is correct) or False (guess is incorrect)

def isCorrectGuess(wordSet, guess):
    return guess in wordSet

# Name:        isGameWon
# Purpose:     Determine whether you have won
# Parameters:  wordSet (set of letters in target word)
#              guesses (list of guesses)
# Returns:     True (you have won) or False (you have not won)

def isGameWon(wordSet, guesses):
    return wordSet <= set(guesses)

# Name:        printEndGame
# Purpose:     Print results of game
# Parameters:  word (target word)
#              winFlag (Boolean value indicating whether you have won)
# Returns:

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

# Name:        playHangman
# Purpose:     Play a game of Hangman
# Parameters:  word (target word)
# Returns:

def playHangman(word):
    # Parameters
    wordSet = set(word)
    life    = 7
    guesses = []
    winFlag = False

    # Guess loop
    while life > 0 and winFlag == False:
        printHangman(life)
        printIncorrectGuesses(wordSet, guesses)
        printCorrectGuesses(word, guesses)
        guess = ""
        while not isValidGuess(guess) or not isNewGuess(guesses, guess):
            guess = input("Guess:     ")
            guess = guess.upper().strip()
        guesses.append(guess)
        if isCorrectGuess(wordSet, guess):
            winFlag = isGameWon(wordSet, guesses)
        else:
            life -= 1

    # Print end state
    printHangman(life)
    printIncorrectGuesses(wordSet, guesses)
    printCorrectGuesses(word, guesses)
    printEndGame(word, winFlag)
    return

# Name:        main
# Purpose:     Loop through multiple games of Hangman
# Parameters:
# Returns:

def main():
    # Global parameters
    words = []
    f = io.open("hangman_words.txt", "r")
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
        newGameInput = ""
        while newGameInput not in ["Y", "YES", "N", "NO"]:
            newGameInput = input("Another game? (Y/N):  ")
            newGameInput = newGameInput.upper().strip()
        if newGameInput in ["Y", "YES"]:
            gameCounter = (gameCounter + 1) % len(words)
        elif newGameInput in ["N", "NO"]:
            loopFlag = False

    print("")
    return

if __name__ == "__main__":
    main()
