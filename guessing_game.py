# Python Web Development Techdegree
# Project 1 - Number Guessing Game
# --------------------------------
# For this first project we will be using Workspaces. 
# Note: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you #fork the snapshot of this workspace.

import random

def start_game(best_attempt = 1000000):
    attempt = 0
    guess = int()

    # Psuedo-code Hints
    # When the program starts, we want to:
    # ------------------------------------
    # 1. Display an intro/welcome message to the player.
    print("Welcome")
    print("Can you beat the best attempt:" + str(best_attempt))

    # 2. Store a random number as the answer/solution.
    answer = random.randint(0, 10)

    # 3. Continuously prompt the player for a guess.
    # a. If the guess greater than the solution, display to the player "It's lower".
    # b. If the guess is less than the solution, display to the player "It's higher"

    while True:
        attempt = attempt + 1
        try:
            guess = int(input("give a number "))
        except ValueError:
            print("Try again, it's a number: ")
            continue
        if guess == answer:
            break
        if guess < 0:
            print("out of the scope, try again: ")
            continue
        if guess > 10:
            print("out of the scope, try again: ")
            continue
        if guess < answer and guess >= 0:
            print("It's higher ")
            continue
        if guess > answer and guess <= 10: 
            print("It's lower ")
            continue 

    # 4. Once the guess is correct, stop looping, inform the user they "Got it"
    # and show how many attempts it took them to get the correct number.

    if attempt < best_attempt:
        best_attempt = attempt
    
    print('Got it! It took you ' + str(attempt) + ' attempt(s)')
            
    # 5. Let the player know the game is ending, or something that indicates the game is over.
    print("Game is over")

    # ( You can add more features/enhancements if you'd like to. )
    try_again(best_attempt)

def try_again(best_attempt):
    again = input('Do you want to play again? ')
    if again.upper() == 'YES':
        start_game(best_attempt)
    if again.upper() == 'NO':
        print('Thanks for playing') 
    else:
        print('Wrong input! Try again.')
        try_again(best_attempt)
    
# Kick off the program by calling the start_game function.
start_game()
