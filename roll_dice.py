import random

roll = random.randint(1, 6)

guess = int(input('Guess the dice roll: \n'))

print('The computer rolled a ' + str(roll))

if roll == guess:
    print("Correct! They rolled a " + str(roll))
else:
    print('wrong')
