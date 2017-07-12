import random

def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        # print roll, 'roll was 100, you lose. What are the odds?! Play again!'
        return False
    elif roll <= 50:
        # print roll, 'roll was 1-50, you lose. Play again!'
        return False
    elif 100 > roll > 50:
        # print roll, 'roll was 51 - 99. You win! *Pretty lights flash* Play more!'
        return True

def simpleBetter(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    current_wager = 0

    while current_wager < wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager
        current_wager += 1
    print 'Funds: ', value

x = 0
while x < 100:
    simpleBetter(10000, 100, 100)
    x += 1