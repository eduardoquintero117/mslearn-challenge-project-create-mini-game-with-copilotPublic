#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print("Hello welcome to the rock, paper, scissors minigame")
# create a rock, paper or scissors minigame
# create a random number generator
# import the random library
import random
# create a function that takes in a number and returns a string
# if the number is 0, return "rock"
# if the number is 1, return "paper"
# if the number is 2, return "scissors"
# otherwise, return "invalid input"


def number_to_choice(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "paper"
    elif number == 2:
        return "scissors"
    else:
        return "invalid input"


#Create a function that retrieves a string and returns a string, checks three options "rock"o "paper"o"scissors" and if not, returns an invalid option.
# if the string is "rock", return ""
# if the string is "paper", return ""
# if the string is "scissors", return ""
# otherwise, return "invalid input"

def choice_to_number(choice):
    if choice == "rock" or choice == "paper" or choice == "scissors" :
        return ""
    else:
        print("----->invalid input")


#operation or in python simbol ||

# create a function that takes in two string and returns a string

# if the first string is "rock" and the second string is "paper", return "you loses"
# if the first string is "rock" and the second string is "scissors", return "you wins"

# if the first string is "paper" and the second string is "rock", return "you wins"
# if the first string is "paper" and the second string is "scissors", return "you loses"

# if the first string is "scissors" and the second string is "rock", return "you loses"
# if the first string is "scissors" and the second string is "paper", return "you wins"

# if the first string is the same as the second string, return "tie"


def choice_to_outcome(choice1, choice2):

    if choice1 == "rock" and choice2 == "paper":
        return "you loses"
    elif choice1 == "rock" and choice2 == "scissors":
        return "you wins"
    elif choice1 == "paper" and choice2 == "rock":
        return "you wins"
    elif choice1 == "paper" and choice2 == "scissors":
        return "you loses"
    elif choice1 == "scissors" and choice2 == "rock":
        return "you loses"
    elif choice1 == "scissors" and choice2 == "paper":
        return "you wins"
    elif choice1 == choice2:
        return "tie"
    else:
        return "invalid input"
    

#Create a loop that prompts the user to enter one of three options rock, paper, or scissors via the terminal
#If the option is not valid, ask again, enter any of the three options
#Keep a tally of victories and defeats and show it at the end of each game
# and at the end of the game ask the user if they want to play if the answer is no the loop ends
# otherwise, the loop continues



 
# create a variable called user_score and set it to 0
# create a variable called computer_score and set it to 0


user_score = 0
computer_score = 0
# create a variable called play_again and set it to "yes"

play_again = "yes"
# create a loop that continues while play_again is "yes"
# create a variable called user_choice and prompt the user to enter "rock", "paper" or "scissors" via the terminal
# create a variable called computer_choice and set it to a random number between 0 and 2
# create a variable called outcome and set it to the return value of choice_to_outcome with user_choice and computer_choice as arguments
# print "you chose: " and the value of user_choice
# print "computer chose: " and the value of computer_choice
# print the value of outcome
# if outcome is "you wins", increment the value of user_score by 1
# if outcome is "you loses", increment the value of computer_score by 1
# print "you: " and the value of user_score
# print "computer: " and the value of computer_score
# prompt the user to enter "yes" or "no" via the terminal and store the value in play_again

while play_again == "yes":
    print("\n")
    #The player can choose one of the three options "rock", "paper" or "scissors"
    #The player must be warned if they enter an invalid option.
    print("choose one of the three options ")
    user_choice = input(" rock, paper or scissors: ")
    user_choice = user_choice.lower()
    choice_to_number(user_choice)
    #The computer must choose one of the three options "rock", "paper" or "scissors" at random.
    computer_choice = random.randint(0, 2)
    outcome = choice_to_outcome(user_choice, number_to_choice(computer_choice))
    print("you chose: " + user_choice)
    print("computer chose: " + number_to_choice(computer_choice))
    print(outcome)
    if outcome == "you wins":
        user_score += 1
    elif outcome == "you loses":
        computer_score += 1
    print("\n")
    print("you: " + str(user_score))
    print("computer: " + str(computer_score))
    #aswer user if he wants to play again
    print("you want to play again?")

    play_again = input("yes or no: ").lower()
    # salto de linea en python
    print("\n")

    



















