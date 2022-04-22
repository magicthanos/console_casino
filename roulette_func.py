import random
from money_system import ballance

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

def roulette_game(b):
    x = ballance.bet_money(b) #bet money
    if x: #if the bet was successful
      ans = None
      while ans != 'color' and ans !='number':
        ans = input('Would you like to bet on a color or number?: ')
      match ans:
        case 'color':
            color_case(b, x) #color case
        case 'number':
            number_case(b, x)  #number case  

def color_case(b, x):
    color = None
    while color not in ('red', 'black', 'green'):
        color = input('What color would you like to bet on?: ')
    if color == roulette.dic[roulette.rand_choice(roulette)]:
        print('You won!')
        b.add_money(x + x * 2) if color != 'green' else b.add_money(x + x * 10) #if the color is green, the bet is multiplied by 10
    else:
        print('You lost!')

def number_case(b, x):
  number = None
  while 0<=number<=36:
        number = int(input('What number would you like to bet on?: '))
  if number == roulette.rand_choice(roulette):
        print('You won!')
        b.add_money(x + x*2) if number != 0 else b.add_money(x + x*10) #if the number is 0, the bet is multiplied by 10
  else:
        print('You lost!')
        
if __name__ != '__main__':
  print('Roulette loaded')
    