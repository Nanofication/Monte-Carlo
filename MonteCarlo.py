import random
import matplotlib
import matplotlib.pyplot as plt
import time

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


def doublerBetter(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    wX = []
    vY = []

    current_wager = 1
    previous_wager = 'win'
    previous_wager_amount = initial_wager

    while current_wager <= wager_count:
        if previous_wager == 'win':
            print 'we won the last wager, great'
            if rollDice():
                value += wager
                print value
                wX.append(current_wager)
                vY.append(value)
            else:
                value -= wager
                previous_wager = 'loss'
                print value
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)
                if value < 0:
                    print 'We went broke after', current_wager, ' bets'
                    break
        elif previous_wager == 'loss':
            print 'we lost the last one, so we will be smart and double'
            if rollDice():
                wager = previous_wager_amount * 2
                print 'we won', wager
                value += wager
                print value
                wager = initial_wager
                previous_wager = 'win'
                wX.append(current_wager)
                vY.append(value)
            else:
                wager = previous_wager_amount * 2
                print 'we lost', wager
                value -= wager
                if value < 0:
                    print 'We went broke after ', current_wager, 'bets'
                    break
                print value
                previous_wager = 'loss'

                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)
        current_wager += 1

    print value
    plt.plot(wX, vY)

doublerBetter(10000,100,1000)
plt.show()
time.sleep(555)

x = 0
while x < 100:
    simpleBetter(10000, 100, 10000)
    x += 1

plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()