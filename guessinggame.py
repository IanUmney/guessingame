import random

guessCount = 0
guessLimit = 6
words = ["orange", "person", "noun", "money", "tiger", "people"]


def singlePlayer():
    global guessCount, guessLimit, words
    
    word = random.choice(words)
    while guessCount < guessLimit:
        attempt = input("Enter a guess: ")
        if attempt == word:
            exit(f"You guessed it in {guessCount+1} tries!")
        else:
            print(f"Incorrect. Try again. You have {guessLimit-guessCount-1} tries left.")
            guessCount += 1


def multiPlayer():
    global guessCount, guessLimit

    word = input("please enter the word you want player 2 to guess: ")
    while guessCount < guessLimit:
        attempt = input("Enter a guess: ")
        if attempt == word:
            exit(f"You guessed it in {guessCount+1} tries!")
        else:
            print(f"Incorrect. Try again. You have {guessLimit-guessCount-1} tries left.")
            guessCount += 1


def main():
    playercount = input("""This is a two player guessing game. 
Player 1 will input the word and player 2 will try to guess it! 

    - If you want to play this singleplayer enter 'singleplayer'
    - If you want to play multiplayer, enter 'multiplayer'

Mode Selection: """)

    if playercount == "singleplayer":
        singlePlayer()
    elif playercount == "multiplayer":
        multiPlayer()
    else:
        exit("Incorrect play mode selected.")

if __name__=="__main__":
    main()

