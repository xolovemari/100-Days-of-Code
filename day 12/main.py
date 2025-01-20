import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

number = random.randint(1, 100)

def guesses():
    guess = int(input("Make a guess: "))

    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print(f"You got it! The answer was {number}.")
        return True
    return False

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5    
else:
    print("Invalid input, please try again.")
    exit()

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    if guesses():
        break
    if attempts != 1:
        print("Guess again.")
    attempts -= 1

if attempts == 0:
    print("You've run out of guesses. Refresh the page to run again.")