import random as rand

def rollDie(sides):
    return rand.randint(1, sides)

print(rollDie(6))
print(rollDie(20))
print(rollDie(100))