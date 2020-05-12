"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import math

def start_game():
    print("Welcome to the Number Guessing Game!")
    random_number = math.ceil((random.random()*9)+1)
    guesses = 0
    guess_list=[]

    while guesses<10: 
        try:
            guess = int(input("Please guess a number between 1 and 10. "))
            if guess > 10 or guess < 1:
                print("You have to choose a number between 1 and 10.")
                guesses +=1
            if guess < random_number:
                print("Your guess was too low.")
                guesses+=1
            if guess > random_number: 
                print("Your guess was too high.")
                guesses+=1
            if guess == random_number: 
                print(" {} was the right number!".format(random_number))
                guesses+=1
                print("Thank you for playing.")
                print("You got it in {} guesses.".format(guesses))
                guess_list.append(guesses)
                break
        except ValueError: 
            print("You need to enter a number!") 
    
    play_again=input("Would you like to play again? Yes/No ")
    if play_again == "Yes":
        print("The best score is {} . See if you can beat it! ".format(min(guess_list)))
        start_game()
    else: 
        print("End of Game.")

     
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

# Kick off the program by calling the start_game function.
start_game()