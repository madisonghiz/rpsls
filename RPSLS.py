# Rock, paper, scissor, lizard, Spock game against the computer. Mini project 1 in Coursera Intro. to Interactive Programming in Python course. 

import random

def name_to_number(name):
    if name == "rock":
        name = 0
    if name == "Spock":
        name = 1
    if name == "paper":
        name = 2
    if name == "lizard":
        name = 3
    if name == "scissors":
        name = 4

    return name

def number_to_name(number):
    if number == 0:
        return "rock"
    if number == 1:
        return "Spock"
    if number == 2:
        return "paper"
    if number == 3:
        return "lizard" 
    if number == 4:
        return "scissors"


def rpsls(player_choice):

    print ("\n")
    print ("You have chosen " + player_choice)

    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5,1)
    
    comp_choice = str(number_to_name(comp_number))

    print ("Computer has chosen " + comp_choice)

    dif = (player_number - comp_number) % 5

    if dif == 0:
        print ("You have tied! Try again.")

    elif dif == 1:
        print ("Player has won!")

    elif dif == 2: 
        print ("Player has won!")

    elif dif == 3:
        print ("Player has lost!")
    
    elif dif == 4:
        print ("Player has lost!")

    else:

        print ("Wrong input")



user_input = input('User input: ')
print (rpsls(user_input))