import random
import matplotlib
import matplotlib.pyplot as plt

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

    wX = []
    vY = []

    current_wager = 1

    while current_wager <= wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager

        wX.append(current_wager)
        vY.append(value)
        current_wager += 1

    if value < 0:
        value = "broke"
    # print 'Funds: ', value
    plt.plot(wX, vY)

x = 0
while x < 100:
    simpleBetter(10000, 100, 10000)
    x += 1

plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()