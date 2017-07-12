import random

def rollDice():
    roll = random.randint(1,100)
    return roll

x = 0

while x < 100:
    result = rollDice()
    print result
    x += 1