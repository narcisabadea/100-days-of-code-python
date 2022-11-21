# Make a rock, paper, scissors game.

import random 

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

#Write your code below this line 👇

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

options = [rock, paper, scissors]

pc_option = random.randint(0, 2)
user_option = options[user_input]

print(user_option)
print('Computer chose:', options[pc_option])

if user_input == 0:
    if pc_option == 1:
        print("You win")
    elif pc_option == 2:
        print("Computer wins")
    else:
        print("Nobody wins")
elif user_input == 1:
    if pc_option == 0:
        print("You win")
    elif pc_option == 2:
        print("Computer wins")
    else:
        print("Nobody wins")
elif user_input == 2:
    if pc_option == 0:
        print("You win")
    elif pc_option == 2:
        print("Computer wins")
    else:
        print("Nobody wins")
else:
    print("Please enter a valid value")

