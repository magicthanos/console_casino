class ballance:

    def __init__(self, money: int = 0):
        self.money = money

    def add_money(self, money: int = 0) -> int:
        self.money += money

    def remove_money(self, money: int = 0) -> int:
        self.money -= money


if __name__ != '__main__':
    print('Ballance loaded')
