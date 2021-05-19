import random

computer_choise = random.choice(["scissors", "rock", "paper"])
print('pc chose ' + computer_choise)

user_choise = input('Do you want - rock, paper or scissors?\n')

if computer_choise == user_choise:
    print('TIE')
elif user_choise == 'rock' and computer_choise == 'scissors':
    print('WIN')
elif user_choise == 'scissors' and computer_choise == 'paper':
    print('WIN')
else:
    print('You loose computer wins')
