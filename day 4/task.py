import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if choice not in [0, 1, 2]:
    print("Choose a valid number.")
    exit()

moves = [0, 1, 2]
comp_choice = random.choice(moves)

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose:")

if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
else:
    print(scissors)

if comp_choice == choice:
    print("It's a draw")
elif comp_choice == 0 & choice == 1 or comp_choice == 2 & choice == 0:
    print("You win!")
else:
    print("You lose")
