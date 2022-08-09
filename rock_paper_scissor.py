import random
import sys

def computer_choice():
    game_list = ['rock', 'paper', 'scissor']
    final_computer_choice = random.choice(game_list)
    return final_computer_choice


def gamer_choice():
    print ("Call your shot:  \'rock\', \'paper\', \'scissor\'")
    user_input = input('>')
    if 'rock' in user_input or 'paper' in user_input or 'scissor' in user_input:
        x = user_input
        print ("Your choice: ", x)
        y = computer_choice()
        print ("Computer's choice: ", y)
        game_start (y,x)
    else:
        print ("Invalid option.. try again")
        return gamer_choice()

def go_again(loop):
    print (loop)
    if 'y' in loop or 'n' in loop: 
        if loop == 'y':
            gamer_choice()
        else:
            print ("Goodbye! have a nice day!")
            exit(0)
    else:
        print ("Invalid entry.... you will have to restart gamne if you want to have another go")
        exit(1)
        

def game_start(a,b):
    if a == b:
        print ("Game is draw, would you like to go again? Type \'y\' or \'n\' ")
        user_loop = input('>')
        go_again(user_loop)
    elif a == 'rock' and b == 'paper':
        print ("You win!, would you like to go again? Type \'y\' or \'n\' ")
        user_loop = input('>')
        go_again(user_loop)
    elif a == 'paper' and b == 'rock':
        print ("Computer wins, would you like to go again? Type \'y\' or \'n\'")
        user_loop = input('>')
        go_again(user_loop)
    elif a == 'scissor' and b == 'paper':
        print ("Computer wins, would you like to go again? Type \'y\' or \'n\'")
        user_loop = input('>')
        go_again(user_loop)
    elif a == 'paper' and b == 'scissor':
        print ("You win!, would you like to go again? Type \'y\' or \'n\'")
        user_loop = input('>')
        go_again(user_loop)
    elif a == 'scissor' and b == 'rock':
        print ("You win! would you like to go again? Type \'y\' or \'n\' ")
        user_loop = input('>')
        go_again(user_loop)
    elif a == 'rock' and b == 'scissor':
        print ("Computer wins! would you like to go again? Type \'y\' or \'n\' ")
        user_loop = input('>')
        go_again(user_loop)
    else:
        exit(1)



gamer_choice()