import random

rock = '''
    _______
---'  _____)
      (_____)
      (_____)
      (____)
---'__(___)
'''

paper = '''
    _______
---'  _____)_____
           ______)
           ________)
          _______)
---.__________)
'''

scissors = '''
    _______
---'  _____)_____
           ______)
           ________)
      (____)
---'__(___)
'''
game_images = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Papper or 2 for Scissors.\n"))

if user_choice >=3 or user_choice <0:
    print("You tyoed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose {computer_choice}")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice < user_choice:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif computer_choice == user_choice:
        print("It's a draw")