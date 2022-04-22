from functions import coin_game, roullete_game, slots_game

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
            roullete_game()
        case 3:
            slots_game()
            

if __name__ == '__main__':
    main()