#Name:     hangman.py
#Purpose:  Play a game of hangman

import codecs
import re
import random

def cleanWord(word):
    word = word.lower()
    word = re.sub("\s+", " ", word);
    return word.strip()

def printHangman(life):
    if life == 0:
        print("    @@@@@@@@@@@@@@        ")
        print("    @@           |        ")
        print("    @@          _|_       ")
        print("    @@         (*_*)      ")
        print("    @@          _|_       ")
        print("    @@   <<----(   )---->>")
        print("    @@          ( )       ")
        print("    @@          ( )       ")
        print("    @@         // \\      ")
        print("    @@        //   \\     ")
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

def printGuesses(guesses):
    text = "Guesses: "
    for guess in guesses.sort():
        text = text + guess.upper()
    print(text)
    print("")
    return

def printWord(word, guesses):
    text = ""
    for letter in word:
        if letter in guesses:
            text = text + letter.upper()
        else:
            text = text + "?"
    print(text)
    print("")
    return

def correctGuess(word, guess):
    correctFlag = False
    for letter in word:
        if letter == guess:
            correctFlag = True
    return correctFlag

def gameWon(word, guesses):
    wordSet = set()
    for letter in word:
        wordSet.add(letter)
    guessesSet = set(guesses)
    return wordSet == guessesSet

def main():
    
    #Read in words
    words = []
    f = codes.open("hangman_words.txt", "r")
    for w in f:
        words.append(cleanWord(w))
    f.close()
    
    #Parameters
    winFlag = False
    life = 7
    guesses = []
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    word = words[random.randint(0, len(words) - 1)]
    
    while life > 0 and winFlag = False:
        printHangman(life)
        printGuesses(guesses)
        printWord(word, guesses)
        guess = ""
        while guess not in letters and guess not in guesses:
            guess = input("Next guess: ")
            guess = guess.lower()
        guesses.append(guess)
        if correctGuess(word, guess):
            winFlag = gameWon(word, guesses)
        else:
            life = life - 1
    
    print("The word was " + word.upper())
    if winFlag:
        print("You win!")
    else:
        print("You lose.")
    return

if __name__ == "__main__":
    main()
