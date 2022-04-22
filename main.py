from coinflip_func import coin_game
from roulette_func import roulette_game
from slots_func import slots_game

def main():
    print('Welcome to my casino!')
    ans = None
    while ans not in (1, 2, 3):
        print('1. Play coinflip')
        print('2. Play roulette')
        print('3. Play slots')
        ans = int(input('What would you like to do?: '))
    match ans:
        case 1:
            coin_game()
        case 2:
            roulette_game()
        case 3:
            slots_game()
            

if __name__ == '__main__':
    main()