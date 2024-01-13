rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line

import random

list = [rock, paper, scissors]
my_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if my_chose < 3 and  my_chose > 0:
    print(list[my_chose])
    computer_chose = random.randint(0,2)
    print("Computer chose:")
    print(list[computer_chose])

    if my_chose == 0 and computer_chose == 2:
        print("You win!")
    elif my_chose == 2 and computer_chose == 0:
        print("You lose!")
    elif my_chose == 1 and computer_chose == 0:
        print("You win!")
    elif my_chose == 0 and computer_chose == 1:
        print("You lose!")
    elif my_chose == 2 and computer_chose == 1:
        print("You win!")
    elif my_chose == 1 and computer_chose == 2:
        print("You lose!")
    elif my_chose == computer_chose:
        print("It's a draw!")
else:
    print("You typed an invalid number, you lose!")



