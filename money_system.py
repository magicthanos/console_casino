class ballance:

    def __init__(self):
        self.money = 0

    def add_money(self, money: int = 0):
        self.money += money

    def remove_money(self, money: int = 0):
        self.money -= money

    show_money = lambda self : print(f'Balance {self.money}')
    
    def bet_money(self): #bet money only if you have enough
        x = int(input('How much money would you like to bet?: '))
        if self.money >= x:
            self.remove_money(x)
            return x
        print('You do not have enough money to bet that much')
        return 0 #return 0 so the other functions can see if the bet was successful

    def options(self): #this is the main menu
        ans = None
        while ans not in (1, 2):
            print('   1. Add money')
            print('   2. Show money')
            ans = int(input('What would you like to do?: '))
        match ans:
            case 1:
                money = int(input(('How much money would you like to add?: ')))
                self.add_money(money)
            case 2:
                self.show_money()

if __name__ != '__main__':
    print('Ballance loaded')
