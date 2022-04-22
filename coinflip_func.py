import random


#coinflip
class coinflip:
    flip_the_coin = random.choice([0, 1])  #heads(0) or tails(1)


def coin_game():
    coin = None
    while coin != 0 and coin != 1:
        coin = int(input('Heads or tails?: '))
        coin_condition(coin)


def coin_condition(coin):
    if coin == coinflip.flip_the_coin:
        print('You won!')
    else:
        print('You lost!')


if __name__ != '__main__':
    print('Coinflip loaded')