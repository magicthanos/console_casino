from functions import coin_game, roullete_game
import random
from time import sleep

def main():
    print('Welcome to my casino!')
    ans = None
    while ans != 1 and ans != 2:
        print('1. Play a coinflip')
        print('2. Play a roulette')
        ans = int(input('What would you like to do?: '))
    match ans:
        case 1:
            coin_game()
        case 2:
            roullete_game()

if __name__ == '__main__':
    main()