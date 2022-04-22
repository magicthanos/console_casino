import random
from time import sleep

#coinflip
class coinflip:
    flip_the_coin = random.choice([0, 1]) #heads(0) or tails(1)

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
 
#roulette
class roulette:
    #make a roullete dictionary
    dic = {
        0: 'green',
        1: 'red',
        2: 'black',
        3: 'red',
        4: 'black',
        5: 'red',
        6: 'black',
        7: 'red',
        8: 'black',
        9: 'red',
        10: 'black',
        11: 'red',
        12: 'black',
        13: 'red',
        14: 'black',
        15: 'red',
        16: 'black',
        17: 'red',
        18: 'black',
        19: 'red',
        20: 'black',
        21: 'red',
        22: 'black',
        23: 'red',
        24: 'black',
        25: 'red',
        26: 'black',
        27: 'red',
        28: 'black',
        29: 'red',
        30: 'black',
        31: 'red',
        32: 'black',
        33: 'red',
        34: 'black',
        35: 'red',
        36: 'black'
    }
    def __init__(self, dic):
        self.dic = dic
    rand_choice = lambda self : random.choice(list(self.dic)) #randomly chooses a roulette slot
    check_win = lambda self, choice : self.rand_choice(roulette) == choice #checks if the player won    

def roullete_game():
    ans = None
    while ans != 'color' and ans !='number':
        ans = input('Would you like to bet on a color or number?: ')
    match ans:
        case 'color':
            color_case()
        case 'number':
            number_case()    

def color_case():
    color = None
    while color != 'red' and color != 'black':
        color = input('What color would you like to bet on?: ')
    if color == roulette.dic[roulette.rand_choice(roulette)]:
        print('You won!')
    else:
        print('You lost!')

def number_case():
  number = None
  while 0<=number<=36:
        number = int(input('What number would you like to bet on?: '))
  if number == roulette.rand_choice(roulette):
        print('You won!')
  else:
        print('You lost!')

#slots
class slots:        
    choices = ['cherry', 'lemon', 'orange', 'plum', 'bar', 'bell', 'seven']
    def __init__(self, choices):
        self.choices = choices
    rand_choice = lambda self : random.choice(list(self.choices)) #randomly chooses a slot
    make_slot = lambda self : [self.rand_choice(slots) for x in range(3)] #makes a slot
    check_win = lambda slot : slot[0] == slot[1] == slot[2] #checks if the player won

def slots_game():
    slot_machine = slots.make_slot(slots)
    print(slot_machine[0], end=' ', flush=True)
    sleep(1)
    print(slot_machine[1], end=' ', flush=True)
    sleep(1)
    print(slot_machine[2])
    print('You won!' if slots.check_win(slot_machine) else 'You lost!')

if __name__ == '__main__':
    pass
else:
    print('Functions imported')