import random
import matplotlib
import matplotlib.pyplot as plt
import time

sample_size = 1000

starting_funds = 10000
wager_size = 100
wager_count = 100

simple_busts = 0.0
doubler_busts = 0.0
simple_profits = 0.0
doubler_profits = 0.0

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

def simpleBetter(funds, initial_wager, wager_count, color):
    global simple_busts
    global simple_profits
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
        value = 0
        simple_busts += 1
    # print 'Funds: ', value
    plt.plot(wX, vY, color) # k is black in matplotlib

    if value > funds:
        simple_profits += 1

def doublerBetter(funds, initial_wager, wager_count, color):
    global doubler_busts
    global doubler_profits
    value = funds
    wager = initial_wager

    wX = []
    vY = []

    current_wager = 1
    previous_wager = 'win'
    previous_wager_amount = initial_wager

    while current_wager <= wager_count:
        if previous_wager == 'win':
            # print 'we won the last wager, great'
            if rollDice():
                value += wager
                # print value
                wX.append(current_wager)
                vY.append(value)
            else:
                value -= wager
                previous_wager = 'loss'
                # print value
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)
                if value < 0:
                    # print 'We went broke after', current_wager, ' bets'
                    doubler_busts += 1
                    break
        elif previous_wager == 'loss':
            # print 'we lost the last one, so we will be smart and double'
            if rollDice():
                wager = previous_wager_amount * 2

                if (value - wager) < 0:
                    wager = value
                # print 'we won', wager
                value += wager
                # print value
                wager = initial_wager
                previous_wager = 'win'
                wX.append(current_wager)
                vY.append(value)
            else:
                wager = previous_wager_amount * 2
                # print 'we lost', wager
                if (value - wager) < 0:
                    wager = value
                value -= wager
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)
                if value <= 0:
                    value = 0
                    # print 'We went broke after ', current_wager, 'bets'
                    doubler_busts += 1
                    break
                # print value
                previous_wager = 'loss'

        current_wager += 1

    # print value
    plt.plot(wX, vY, color)
    if value > funds:
        doubler_profits += 1


xx = 0
broke_count = 0
#
# while xx < sample_size:
#     doublerBetter(starting_funds, wager_size, wager_count)
#     xx += 1

# print "death rate: ", broke_count/float(xx) * 100
# print "survival rate: ", 100 - (broke_count/float(xx) * 100)
#
# plt.axhline(0, color = 'r')
# plt.show()
x = 0
while x < sample_size:
    simpleBetter(starting_funds, wager_size, wager_count, 'k')
    doublerBetter(starting_funds, wager_size, wager_count, 'c')
    x += 1

print 'Simple Better bust chance: ', (simple_busts/sample_size) * 100.0
print 'Doubler Better bust chance: ', (doubler_busts/sample_size) * 100.0

print 'Simple Better profit chances: ', (simple_profits/sample_size) * 100.0
print 'Doubler Better profit chances: ', (doubler_profits/sample_size) * 100.0

plt.axhline(0, color='r')
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()