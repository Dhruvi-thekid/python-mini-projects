import random
from random import shuffle

def shuffle_list(game):
    random.shuffle(game)
    return game

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input ("Pick a Number 0,1 or 2:")
    return int(guess)

def check_guess(game, guess):
    if game[guess] == '0':
        print ("You found the Ball!")
        return
    else:
        print ("Sorry, Game Over. Try again next time")

game = ['','0','']
mix = shuffle_list(game)
guess = player_guess()
check_guess(mix, guess)
