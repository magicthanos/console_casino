import random
from money_system import ballance


#coinflip
class coinflip:
    flip_the_coin = random.choice(
        ('heads', 'tails'))  #randomly chooses heads or tails


def coin_game(b):
    x = ballance.bet_money(b)  #bet money
    if x:  #if the bet was successful
        coin = None
        while coin not in ('heads', 'tails'):
            coin = input('Heads or tails?: ')
        coin_condition(coin, b, x)


def coin_condition(coin, b, x):
    if coin == coinflip.flip_the_coin:
        print('You won!')
        b.add_money(x + x * 2)
    else:
        print('You lost!')


if __name__ != '__main__':
    print('Coinflip loaded')