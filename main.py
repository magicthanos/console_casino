from coinflip_func import coin_game
from roulette_func import roulette_game
from slots_func import slots_game
from money_system import ballance

def main():
    b = ballance()
    print('Welcome to my casino!')
    ans = None
    while b.money <= 0:
        b.money = int(input('Add starting amount of money: '))
    while ans != 5:
        casino_choices(b, ans)

def casino_choices(b, ans):
    while ans not in (1, 2, 3, 4, 5):
        print('     1. Play coinflip')
        print('     2. Play roulette')
        print('     3. Play slots')
        print('     4. Ballance')
        print('     5. Exit')
        ans = int(input('What would you like to do?: '))
    match ans:
        case 1:
            coin_game(b) if b.money >= 1 else print('You do not have enough money to play coinflip')
        case 2:
            roulette_game(b) if b.money >= 1 else print('You do not have enough money to play roulette')
        case 3:
            slots_game(b) if b.money >= 1 else print('You do not have enough money to play slots')
        case 4:
            b.options()
        case 5:
            exit()
            
            

if __name__ == '__main__':
    main()