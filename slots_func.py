import random
from time import sleep


#slots
class slots:
    choices = ['cherry', 'lemon', 'orange', 'plum', 'bar', 'bell', 'seven']

    def __init__(self, choices):
        self.choices = choices

    rand_choice = lambda self: random.choice(list(self.choices)
                                             )  #randomly chooses a slot
    make_slot = lambda self: [self.rand_choice(slots)
                              for x in range(3)]  #makes a slot
    check_win = lambda slot: slot[0] == slot[1] == slot[
        2]  #checks if the player won


def slots_game():
    slot_machine = slots.make_slot(slots)
    print(slot_machine[0], end=' ', flush=True)
    sleep(1)
    print(slot_machine[1], end=' ', flush=True)
    sleep(1)
    print(slot_machine[2])
    print('You won!' if slots.check_win(slot_machine) else 'You lost!')


if __name__ != '__main__':
    print('Slots loaded')