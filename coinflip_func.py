import random
from money_system import ballance


#coinflip
class coinflip:
    flip_the_coin = random.choice([0, 1])  #heads(0) or tails(1)


def coin_game(b):
    x = ballance.bet_money(b)
    if x:
        coin = None
        while coin != 0 and coin != 1:
            coin = int(input('Heads or tails?: '))
            coin_condition(coin, b, x)


def coin_condition(coin, b, x):
    if coin == coinflip.flip_the_coin:
        print('You won!')
        b.add_money(x + x * 2)
    else:
        print('You lost!')


if __name__ != '__main__':
    print('Coinflip loaded')