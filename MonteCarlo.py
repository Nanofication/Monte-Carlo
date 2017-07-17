import random
import matplotlib
import matplotlib.pyplot as plt
import time


simple_profits = 0.0
doubler_profits = 0.0

simple_busts = 0.0
doubler_busts = 0.0

multiple_busts = 0.0
multiple_profits = 0.0

lower_bust = 31.235

higher_profit = 63.208

sample_size = 1000 # Constant
starting_funds = 10000 # Constant


wager_size = 100 # Switch up
wager_count = 1000 # Switch up

da_busts = 0.0
da_profits = 0.0
da_sample_size = 100000
ret = 0.0

random_multiple = random.uniform(0.1, 10.0)


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

def rollDiceFair():
    roll = random.randint(1,100)

    if roll <= 50:
        # print roll, 'roll was 1-50, you lose. Play again!'
        return False
    elif roll > 50:
        # print roll, 'roll was 51 - 99. You win! *Pretty lights flash* Play more!'
        return True


def dAlembert(funds, initial_wager, wager_count):
    global ret
    global da_busts
    global da_profits

    value = funds
    wager = initial_wager
    current_wager = 1
    previous_wager = 'win'
    previous_wager_amount = initial_wager

    while current_wager <= wager_count:
        if previous_wager == 'win':
            if wager == initial_wager:
                pass
            else:
                wager -= initial_wager

            # print 'current wage:', wager, 'value', value

            if rollDiceFair():
                value += wager
                # print 'We won, current value', value
                previous_wager_amount = wager
            else:
                value -= wager
                previous_wager = 'loss'
                # print 'We lost, current value', value
                previous_wager_amount = wager

                if value <= 0:
                    da_busts += 1
                    break
        elif previous_wager == 'loss':
            wager = previous_wager_amount + initial_wager
            if (value - wager) <= 0:
                wager = value

            # print "Lost the last wager, current wager:", wager, 'value', value

            if rollDiceFair():
                value += wager
                # print "We won current value: ", value
                previous_wager_amount = wager
                previous_wager = 'win'
            else:
                value -= wager
                # print "We lost, current value:", value
                previous_wager_amount = wager

                if value <= 0:
                    da_busts += 1
                    break
        current_wager += 1

    if value > funds:
        da_profits += 1
    # print value
    ret += value


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

def multipleBetter(funds, initial_wager, wager_count):
    global multiple_busts
    global multiple_profits

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
                    multiple_busts += 1
                    break
        elif previous_wager == 'loss':
            # print 'we lost the last one, so we will be smart and double'
            if rollDice():
                wager = previous_wager_amount * random_multiple

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
                wager = previous_wager_amount * random_multiple
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
                    multiple_busts += 1
                    break
                # print value
                previous_wager = 'loss'

        current_wager += 1

    # print value
    # plt.plot(wX, vY, color)
    if value > funds:
        multiple_profits += 1


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


dAlembert(starting_funds, wager_size, wager_count)


while True:
    # wager_size = 100  # Switch up
    # wager_count = 1000  # Switch up
    wager_size = random.uniform(1.0,1000.0)
    wager_count = random.uniform(10, 10000)

    da_busts = 0.0
    da_profits = 0.0
    da_sample_size = 10000
    ret = 0.0
    counter = 1

    while counter <= da_sample_size:
        dAlembert(starting_funds, wager_size, wager_count)
        counter += 1

    roi = ret - (da_sample_size * starting_funds)
    total_invested = da_sample_size * starting_funds
    percent_roi = (roi/total_invested) * 100.0

    wager_size_percent = (wager_size/starting_funds) * 100.0

    if percent_roi > 1:
        print '______________________________________'
        print "Total invested: ", da_sample_size * starting_funds
        print "Total Return:", ret
        print "ROI", ret - (da_sample_size * starting_funds)
        print "Bust Rate:", (da_busts/da_sample_size) * 100.0
        print "Profit Rate:", (da_profits/da_sample_size) * 100.0
        print "Wager Size:", wager_size
        print "Wager Count:", wager_count
        print "Wager size percentage:", wager_size_percent

        saveFile = open('monte-carlo-liberal.csv','a')
        saveLine = '\n' + str(percent_roi) + ',' + str(wager_size_percent) + ',' + str(wager_count) + ',g'
        saveFile.write(saveLine)
        saveFile.close()

    elif percent_roi < -1:
        print '______________________________________'
        print "Total invested: ", da_sample_size * starting_funds
        print "Total Return:", ret
        print "ROI", ret - (da_sample_size * starting_funds)
        print "Bust Rate:", (da_busts / da_sample_size) * 100.0
        print "Profit Rate:", (da_profits / da_sample_size) * 100.0
        print "Wager Size:", wager_size
        print "Wager Count:", wager_count
        print "Wager size percentage:", wager_size_percent

        saveFile = open('monte-carlo-liberal.csv', 'a')
        saveLine = "\n" + str(percent_roi) + "," + str(wager_size_percent) + "," + str(wager_count) + ',r'
        saveFile.write(saveLine)
        saveFile.close()

# while True:
#     multiple_busts = 0.0
#     multiple_profits = 0.0
#
#     multiple_sample_sizes = 100000
#     current_sample = 1
#
#     random_multiple = random.uniform(0.1, 10.0)
#
#     while current_sample <= multiple_sample_sizes:
#         multipleBetter(starting_funds, wager_size, wager_count)
#         current_sample += 1
#
#     if ((multiple_busts/multiple_sample_sizes) * 100.0 < lower_bust) and \
#         ((multiple_profits/multiple_sample_sizes) * 100.0 > higher_profit):
#         print '##################################'
#         print "Found a winner, the multiple was: ", random_multiple
#         print "Lower bust to beat",lower_bust
#         print 'Higher profit rate to beat', higher_profit
#         print "Bust rate:",(multiple_busts/multiple_sample_sizes)*100.0
#         print "Profit rate:",(multiple_profits/multiple_sample_sizes) * 100.0
#         print '##################################'
#     # else:
#     #     print '##################################'
#     #     print "Found a loser, the multiple was: ", random_multiple
#     #     print "Lower bust to beat", lower_bust
#     #     print 'Higher profit rate to beat', higher_profit
#     #     print "Bust rate:", (multiple_busts / multiple_sample_sizes) * 100.0
#     #     print "Profit rate:", (multiple_profits / multiple_sample_sizes) * 100.0
#     #     print '##################################'
#
