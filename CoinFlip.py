import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    coinFlips = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            coinFlips.append('C')
        else:
            coinFlips.append('S')

    cantidad_secas = 0
    cantidad_caras = 0

    for x in range(len(coinFlips)):
        if coinFlips[x] == 'C':
            cantidad_secas = 0
            cantidad_caras += 1
        if coinFlips[x] == 'S':
            cantidad_caras = 0
            cantidad_secas += 1

        if cantidad_secas == 6 or cantidad_caras == 6:
            numberOfStreaks += 1


    # Code that checks if there is a streak of 6 heads or tails in a row.

print('Chance of streak: %s%%' % (numberOfStreaks / 100))